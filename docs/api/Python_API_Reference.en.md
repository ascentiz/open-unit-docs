# Python API Reference (`client.py`)

[← Back to the BodyOS SDK Developer Guide](./README.md)

This module provides a pure-socket client with no third-party dependencies. Internally, it uses `ctypes` to match the underlying C++ memory layout exactly, enabling high-performance data parsing. The Python client also provides script-friendly incremental interfaces and automatic reconnection.

```python
from bodyos import BodyClient, WorkMode, CsvRecordConfig
```

---

## 1. Initialization and Lifecycle

```python
client = BodyClient(sock_path="/run/bodyos/bodyos.sock")
```

- **Parameter**: `sock_path` defaults to the daemon's local control socket path.
- **Exception**: A failed connection raises `BodyOsError`.
- **Resource cleanup**: The client supports context management. Use `with BodyClient() as client:` when possible, or call `client.close()` after use to stop the background streaming thread safely.

---

## 2. System and Work Modes

| Interface | Description |
| :--- | :--- |
| `bool link_is_connected()` | Checks whether the underlying physical hardware, such as the STM32, is online. The link is considered disconnected after 1.5 seconds without data. |
| `bool request_work_mode(mode: WorkMode)` | Requests a work-mode change.<br>• `WorkMode.NONE`: Initial state<br>• `WorkMode.DATA_COLLECT`: Data collection only; control is rejected<br>• `WorkMode.AZ_CONTROL`: AZ device takes control<br>• `WorkMode.USER_CONTROL`: Direct user control |
| `WorkMode get_work_mode()` | Returns the daemon's current work mode. |

> **⚠️ Safety notice**: If the underlying physical link is disconnected (`link_state = 0`), the daemon may reject a mode-change request and return `False`.

---

## 3. High-Frequency Motor Control

The Python control interfaces are intentionally simple. If an input `list` contains fewer than four values, the SDK automatically pads it with `0.0`. The lower layer uses non-blocking transmission, making these interfaces suitable for a 1000 Hz main control loop.

| Interface | Description |
| :--- | :--- |
| `set_motor_enable(enable: bool, node_mask: int = 0x0F)` | Enables or disables motors. `node_mask` is a bit mask; `0x0F` selects all four motors. |
| `set_torque(node_mask: int, torques: List[float])` | Sends torque commands in Nm.<br>**Limit**: `[-2.0, 2.0]`. |
| `set_velocity(node_mask: int, speeds: List[float])` | Sends velocity commands in revolutions per second.<br>**Limit**: `[-40.0, 40.0]`. |
| `set_position(node_mask: int, positions: List[float])` | Sends position commands in revolutions.<br>**Limit**: `[-32.0, 32.0]`. |

### Gait and Firmware

| Interface | Description |
| :--- | :--- |
| `set_gait_mode(mode: int)` | `0` = lower-level algorithm controls the system; `1` = direct user control. |
| `int get_gait_mode()` | Returns the gait-control mode: `0` = lower-level algorithm; `1` = direct user control. |
| `str get_firmware_version()` | Returns the firmware version of the lower-level controller. |

---

## 4. Sensor Reads and Reconnection

```python
sensors = client.latest_sensors()
if sensors and sensors.link_state == 1:
    print(f"IMU Yaw: {sensors.data.imu.yaw}")
```

- **Fast reads**: `latest_sensors()` reads a snapshot directly from local memory in microseconds, with **no network I/O overhead**.
- **Lazy streaming**: On the first call, the SDK establishes the streaming connection in the background and starts an independent thread that continuously updates the local cache.
- **Automatic reconnection**: If the daemon restarts or the connection is lost, the background thread attempts to reconnect to `bodyos_stream.sock` once per second. After recovery, `link_state` automatically returns to `1`.
- **Data structure**: The `data` field of the returned `AllSensors` object is a nested `dataclass`. Access values directly through intuitive properties such as `.data.imu.yaw` and `.data.motors[0].speed`.

---

## 5. Motor Configuration Read/Write

| Interface | Description |
| :--- | :--- |
| `clear_error(node_mask: int = 0x0F)` | Clears motor fault status. |
| `save_config()` | Saves the current configuration to the motor controller's flash memory. |
| `int read_config(idx: DriverConfigIndex)` | Reads a raw 32-bit motor configuration value, such as `CONTROL_MODE`. |
| `write_config_int(idx: DriverConfigIndex, value: int)` | Writes an integer configuration value. **Note**: For safety, the SDK currently allows writes only to `CONTROL_MODE`. |
| `write_config_float(DriverConfigIndex idx, value: float)` | Writes a floating-point configuration value. **Note**: This interface is currently disabled for safety. |
| `set_motor_control_mode(mode: DriverControlMode)` | **Validated configuration**: Reads the current mode first, sends a change only when needed, and reads it back automatically for verification. Supports `CURRENT`, `VELOCITY`, `POSITION_FILTER`, and other modes. |

---

## 6. Advanced Incremental BLE Control

Unlike the C++ full-structure interfaces, the Python client provides convenient incremental operations. **Users change only the fields they need; the lower layer compares and merges the state automatically**, preventing omitted fields from being cleared accidentally.

### 6.1 Incremental Updates (Strongly Recommended)

These interfaces are safer and do not require knowledge of the complete data structures.

| Interface | Description |
| :--- | :--- |
| `update_ble_assist(mode, scene, level, active)` | Incrementally updates assist parameters. For example, `update_ble_assist(level=50)` changes only the assist level while preserving the mode and scene. |
| `update_ble_boost(active: int)` | Incrementally updates Boost mode (`0` = start, `1` = stop). |
| `update_ble_expert(mode, smooth, base, speed, freq, resp, coeff)` | Incrementally updates expert-mode parameters. On the first call, the client silently retrieves the complete lower-level parameter set as the baseline. |

### 6.2 Cached Status Reads

| Interface | Description |
| :--- | :--- |
| `fetch_ble_assist_status()` | Reads the current cached assist status without blocking; returns `BleAsistSetReqAck` or `None`. |
| `fetch_ble_boost_status()` | Reads the cached Boost status. |
| `fetch_ble_expert_status()` | Reads the cached expert-mode status. |

### 6.3 Full Updates (Not Recommended)

These interfaces require detailed knowledge of the complete data structures.

| Interface | Description |
| :--- | :--- |
| `Optional[BleAsistSetReqAck] ble_set_assist(req: BleAsistSetReqAck)` | Sends the complete assist-parameter structure and blocks while waiting for the hardware ACK structure. |
| `Optional[BleBootModeReqAck] ble_set_boost(req: BleBootModeReqAck)` | Sends the complete Boost-parameter structure and blocks while waiting for the hardware ACK structure. |
| `Optional[BleExpertModeReqAck] ble_set_expert(req: BleExpertModeReqAck)` | Sends the complete expert-mode structure and blocks while waiting for the hardware ACK structure. |

### Full Read

| Interface | Description |
| :--- | :--- |
| `ble_get_expert()` | Starts a CAN transaction with the underlying hardware and retrieves the complete expert-parameter set. |

---

## 7. Alarm and Motor-Status Monitoring

| Interface | Description |
| :--- | :--- |
| `get_ble_alarms() -> int` | Returns the 32-bit alarm mask. |
| `get_ble_alarms_string() -> str` | Converts the mask to a readable string, such as `L_HIP_CAN_ERR \| R_KNEE_OVER_TEMP`. |
| `has_critical_alarms() -> bool` | Checks for critical alarms. **Call this in the main control loop; if it returns `true`, execute an emergency stop immediately.** |
| `get_motor_status(motor_id: int) -> int` | Returns the 16-bit status word for motor 1–4. |
| `get_motor_status_string(motor_id: int) -> str` | Parses the motor status word, for example `SWITCHED_ON \| TARGET_REACHED`. |
| `has_motor_fatal_error(motor_id: int) -> bool` | Checks whether a motor has a fatal fault such as encoder disconnection, overcurrent, or overvoltage. |

---

## 8. Asynchronous Compressed CSV Recording

The Python client includes an asynchronous double-buffered queue, so recording never blocks the main control loop.

```python
from bodyos import CsvRecordConfig

# 1. Configure recording parameters
cfg = CsvRecordConfig(
    dir_path="/tmp/bodyos_data",
    file_prefix="sensor_log",
    max_file_size=10 * 1024 * 1024, # Rotate at 10 MB per file
    max_files=5,                    # Keep at most 5 files
    duration_sec=60                 # Stop automatically after 60 seconds
)

# 2. Start recording (returns immediately)
client.start_record(cfg)

# 3. Enqueue data in the main loop (non-blocking, microsecond-level)
client.record_sensors(sensors)

# 4. Stop recording (flush and compress safely in the background)
client.stop_record()
```

> **💡 Tip**: After `stop_record()` is called, the background thread automatically compresses remaining `.csv` files into `.csv.gz` with Zlib Gzip and removes the original files to reduce storage use.
