# BodyOS SDK v2.0.0 Developer Guide

Welcome to BodyOS SDK, the developer toolkit provided by BodyOS. It enables applications on B-core Pi 1 to obtain exoskeleton data, send control requests, and integrate third-party sensors and external devices.

## 🌟 Core Architecture

BodyOS uses a **daemon + dual client socket** architecture to eliminate resource contention between high-frequency control and high-volume data streaming:

- **bodyos-daemon**: Exclusively owns the underlying physical buses (UART/CAN/SPI) and maintains the 1000 Hz high-frequency control loop, hardware-state cache, health monitoring, and physical-button response. An internal **asynchronous transmit queue** prevents high-frequency control commands from blocking the IPC processing thread.
- **Application layer (SDK)**: Communicates with the daemon through local Unix domain sockets and supports both C++ and Python. Control commands are enqueued instantly and non-blockingly, while 100 Hz sensor streams are received passively without blocking. Control and data channels are completely isolated, and an **independent background transmit thread** inside the client prevents interleaving of socket streams.

## ⚡ Core Features

- **Dual-socket isolation**: Control commands do not block streaming. High-frequency streaming actively drops data for slow clients to protect low-level real-time performance.
- **End-to-end asynchronous transmission**: The client `tx_worker` thread works with the daemon-side `CanFdTransport` transmit queue. At 1000 Hz, the main thread only enqueues control commands in microseconds and never blocks.
- **Bounded-queue protection**: When a client or daemon control queue builds up, the oldest **control** commands are discarded automatically while configuration commands are retained, ensuring that the robot always acts on the latest command.
- **Synchronized request validation**: Requests that require synchronous replies, such as configuration reads, validate both `req_id` and `msg_type`. Stale packets remaining in the socket are discarded automatically to prevent timing mismatches.
- **Safe mode switching**: Provides three mutually exclusive modes—data collection only, AZ closed-loop control, and direct user control—to prevent conflicting control ownership.
- **Fast cached reads**: `latest_sensors()` returns an in-memory snapshot in microseconds, making it suitable for a 1000 Hz main control loop.
- **Physical-button integration**: Supports external GPIO buttons for physical mode and level switching in an independent thread that is not blocked by CAN bus timeouts.
- **High-performance asynchronous recording**: Includes an asynchronous Gzip-compressed CSV recorder that does not drop frames or stall the main loop.
- **Hardware-failure fallback**: If the underlying hardware does not respond, the daemon retries automatically (three times by default, with an 800 ms timeout per attempt) and eventually returns a safe default such as `0` to the application, preventing an upper-layer crash.

## 🚀 Quick Start

### 1. Deploy the Daemon

On the target device, such as a Raspberry Pi CM5, copy `bin/` and `config/` into the system directories and start the background service:

```bash
sudo cp bin/* /usr/local/bin/
sudo cp config/bodyos-daemon.service /etc/systemd/system/
sudo cp config/logrotate.bodyos /etc/logrotate.d
sudo systemctl daemon-reload
sudo systemctl enable --now bodyos-daemon
```

*Logs are stored in `/var/log/bodyos/bodyos.log` by default, with automatic rotation and Gzip compression.*

### 2. Integrate a C++ Project

Configure and link the package in `CMakeLists.txt`:

```cmake
find_package(bodyos REQUIRED)
target_link_libraries(your_app PRIVATE bodyos::app)
```

```cpp
#include <bodyos/app/client.hpp>
#include <bodyos/ipc/ipc_protocol.hpp>

int main() {
    bodyos::BodyClient client(bodyos::ipc::DEFAULT_SOCK_PATH);
    client.request_work_mode(bodyos::WorkMode::DATA_COLLECT);
    auto sensors = client.latest_sensors();
    // ...
}
```

### 3. Integrate a Python Project

Place `python/bodyos` on your project path, or run `pip install .` directly.

```python
from bodyos import BodyClient, WorkMode

client = BodyClient()
client.request_work_mode(WorkMode.DATA_COLLECT)
sensors = client.latest_sensors()
if sensors:
    print(f"IMU Yaw: {sensors.data.imu.yaw}")
```

## 📚 Detailed Documentation

The core API descriptions and example code are split into the following documents:

- 📘 **[Complete C++ API Reference (`client.hpp`)](./C++_API_Reference.md)**
    - Covers work modes, high-frequency motor control (torque/velocity/position), configuration read/write operations, BLE parameter updates, and other low-level interfaces.
- 📗 **[Complete Python API Reference (`client.py`)](./Python_API_Reference.md)**
    - Covers high-level incremental interfaces with automatic state merging, asynchronous recording, automatic reconnection, and memory-aligned parsing.
- 🚀 **[Official Example Guide](./Examples_Guide.md)**
    - Provides detailed explanations and safety mechanisms for four core demos, including C++ and Python versions of `sensor_read_record` and `body_assist_control`.

## ❓ Frequently Asked Questions

**Q: Why does requesting a work mode return `BodyOS Error: Daemon returned error code: 1`?**

A: This usually means the underlying physical hardware link is unavailable (`link_state = 0`). Check the CAN bus or serial cable, or wait for the hardware heartbeat to stabilize after power-on before requesting a mode from the daemon.

**Q: Why does the main program remain responsive while sending high-frequency control commands?**

A: The SDK implements an **end-to-end asynchronous transmit queue**. When the C++ or Python client calls a high-frequency interface such as `set_torque()`, it only performs an in-memory enqueue operation that takes microseconds. Actual socket I/O is handled by an independent background `tx_worker` thread. Even if the daemon or underlying bus is congested, the main control loop does not block.

**Q: Why did older versions hang or raise `IPC response mismatch` during exit, for example after pressing Ctrl+C?**

A: This issue has been fixed. The client `request()` function now filters stale packets, automatically discarding historical ACK packets left in the socket buffer, and applies a three-second timeout. The stop command during shutdown waits for a real daemon reply; if the underlying hardware is unresponsive, the program still exits safely after three seconds rather than hanging indefinitely.

**Q: Why was the data not compressed into `.csv.gz`?**

A: The recorder starts a background Gzip thread after `stop_record()` is called. If the program exits too quickly, that thread may not finish. Add `sleep(500ms)` after `stop_record()` to allow compression to complete, or set `KillMode=process` in the daemon's systemd configuration so child threads have time to finish.

**Q: What happens if the underlying CAN hardware becomes completely unresponsive?**

A: The daemon's low-level `transact_raw` retries three times by default, with an 800 ms timeout per attempt. If all attempts fail, the daemon catches the exception and returns a fallback value to the client—for example, `0` when a configuration read fails. A synchronous client read exits and retries after a three-second timeout, while high-frequency control commands are protected by the bounded queue, which automatically discards failed or accumulated old commands. The overall system does not hang.
