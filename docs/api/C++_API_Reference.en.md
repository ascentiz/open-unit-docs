# C++ API Reference (`client.hpp`)

[← Back to the BodyOS SDK Developer Guide](./README.md)

This module provides the C++ client interface for communicating with `bodyos-daemon`. It is intended for real-time control scenarios that require very high performance.

```cpp
#include <bodyos/app/client.hpp>
#include <bodyos/ipc/ipc_protocol.hpp>
```

---

## 1. Initialization and Lifecycle

```cpp
explicit BodyClient(const std::string& sock_path);
~BodyClient();
```

- **Parameter**: `sock_path` is normally `bodyos::ipc::DEFAULT_SOCK_PATH` (`/run/bodyos/bodyos.sock`).
- **Exception**: A failed socket connection or socket creation throws `BodyOsError`.
- **Destructor**: `~BodyClient()` automatically stops the internal background streaming thread and safely closes the underlying socket handle.

---

## 2. System and Status

| Interface | Description |
| :--- | :--- |
| `bool link_is_connected() const` | Checks whether the underlying physical hardware, such as the STM32/controller, is online. The link is considered disconnected if no module heartbeat is received for 1.5 consecutive seconds. |
| `bool request_work_mode(WorkMode mode)` | Requests a work-mode change.<br>• `NONE`: Initial state; all reads and writes are rejected<br>• `DATA_COLLECT`: Data collection only; control writes are rejected<br>• `AZ_CONTROL`: AZ device takes control (`gait_mode=0`)<br>• `USER_CONTROL`: Direct user control (`gait_mode=1`) |
| `WorkMode get_work_mode() const` | Returns the daemon's current work mode. |

> **⚠️ Safety notice**: When `USER_CONTROL` or `AZ_CONTROL` is requested, the lower layer performs a forced safe stop, disables the motors, and switches gait-control ownership. If the link is unavailable, the daemon rejects the request and returns `false`.

---

## 3. High-Frequency Motor Control

These interfaces are intended for use in a 1000 Hz control loop. The lower layer uses one-way transmission and never blocks the main thread.

| Interface | Description |
| :--- | :--- |
| `void set_motor_enable(bool enable, uint8_t node_mask = 0x0F)` | Enables or disables motors. `node_mask` is a bit mask:<br>`0x01` left hip, `0x02` right hip, `0x04` left knee, `0x08` right knee; `0x0F` selects all motors. |
| `void set_torque(uint8_t node_mask, const float nm[4])` | Sends torque commands in Nm.<br>**Limit**: `[-2.0, 2.0]`. |
| `void set_velocity(uint8_t node_mask, const float turn_s[4])` | Sends velocity commands in revolutions per second.<br>**Limit**: `[-40.0, 40.0]`. |
| `void set_position(uint8_t node_mask, const float turn[4])` | Sends position commands in revolutions.<br>**Limit**: `[-32.0, 32.0]`. |

### Gait and Firmware

| Interface | Description |
| :--- | :--- |
| `void set_gait_mode(uint8_t mode)` | `0` = lower-level algorithm controls the system; `1` = direct user control. |
| `uint8_t get_gait_mode()` | Returns the gait-control mode: `0` = lower-level algorithm; `1` = direct user control. |
| `std::string get_firmware_version()` | Returns the firmware version of the lower-level controller. |

---

## 4. Fast Sensor Data Access

```cpp
std::optional<AllSensors> latest_sensors() const;
```

- **Behavior**: Returns in microseconds with **no IPC network overhead**. The implementation is lazy: the first call automatically starts the background streaming thread, synchronized with the lower-level 100 Hz data stream.
- **Return value**: Returns an `AllSensors` structure snapshot on success, or `std::nullopt` while disconnected or initializing.
- **Use case**: Suitable for a 1000 Hz main control loop because it reads the latest sensor cache directly from memory without blocking.
- **Note**: If `link_state == 0`, the physical hardware is offline and the returned data is the last valid snapshot.

---

## 5. Motor Configuration Read/Write

| Interface | Description |
| :--- | :--- |
| `void clear_error(uint8_t node_mask = 0x0F)` | Clears motor-controller fault states. |
| `void save_config()` | Saves the current configuration to the motor controller's flash memory. |
| `uint32_t read_config(DriverConfigIndex idx)` | Reads the raw 32-bit value of a motor-controller setting, such as `CONTROL_MODE`. |
| `void write_config_int(DriverConfigIndex idx, int32_t value)` | Writes an integer setting. **Note**: For safety, the SDK currently allows writes only to `CONTROL_MODE`. |
| `void write_config_float(DriverConfigIndex idx, float value)` | Writes a floating-point setting. **Note**: This interface is currently disabled for safety. |
| `void set_motor_control_mode(DriverControlMode mode)` | **Validated configuration**: Reads the current mode first, sends a change only when needed, and reads it back automatically for verification. Supports `CURRENT`, `VELOCITY`, `POSITION_FILTER`, and other modes. |

---

## 6. BLE Assist and Expert Control

The SDK provides two interface groups: **incremental interfaces** (recommended) and **full-structure interfaces**.

### 6.1 Incremental Interfaces (Strongly Recommended)

These interfaces are safer and do not require knowledge of the complete data structures.

| Interface | Description |
| :--- | :--- |
| `void update_ble_assist(mode, scene, level, pause)` | Incrementally updates assist parameters. The current lower-level heartbeat is retrieved as the baseline; only supplied parameters are changed, while omitted parameters retain their original values. |
| `void update_ble_boost(uint8_t active)` | Incrementally updates Boost mode (`0` = start, `1` = stop). |
| `void update_ble_expert(mode, smooth, base, speed...)` | Incrementally updates expert-mode parameters. |

### 6.2 Full-Structure Write Interfaces

These low-level pass-through interfaces are not recommended unless you understand the complete structures.

| Interface | Description |
| :--- | :--- |
| `std::optional<BleAsistSetReqAck> ble_set_assist(const BleAsistSetReqAck& req)` | Sends the complete assist-parameter structure and blocks until the hardware returns an ACK structure. |
| `std::optional<BleBootModeReqAck> ble_set_boost(const BleBootModeReqAck& req)` | Sends the complete Boost-parameter structure and blocks until the hardware returns an ACK structure. |
| `std::optional<BleExpertModeReqAck> ble_set_expert(const BleExpertModeReqAck& req)` | Sends the complete expert-mode structure and blocks until the hardware returns an ACK structure. |

### Full Read

| Interface | Description |
| :--- | :--- |
| `std::optional<BleExpertModeParamGetAck> ble_get_expert()` | Retrieves the complete set of expert parameters from the hardware. |

### 6.3 Cached Status Reads (Non-Blocking)

| Interface | Description |
| :--- | :--- |
| `std::optional<BleAsistSetReqAck> fetch_ble_assist_status()` | Reads the current cached assist-setting status without triggering a lower-level CAN transaction. |
| `std::optional<BleAsistSetReqAck> fetch_ble_boost_status()` | Reads the current cached Boost-setting status without triggering a lower-level CAN transaction. |
| `std::optional<BleAsistSetReqAck> fetch_ble_expert_status()` | Reads the current cached expert-mode status without triggering a lower-level CAN transaction. |

---

## 7. Alarm and Fault Monitoring

| Interface | Description |
| :--- | :--- |
| `uint32_t get_ble_alarms() const` | Returns the 32-bit alarm mask, including conditions such as CAN communication loss and motor overtemperature. |
| `std::string get_ble_alarms_string() const` | Converts the mask to human-readable alarm text, such as `L_HIP_OVER_TEMP \| DRIVER_PROTECT`. |
| `bool has_critical_alarms() const` | Checks for critical alarms. **Call this in the 1000 Hz control loop; if it returns `true`, execute emergency-stop logic immediately.** |
| `uint16_t get_motor_status(uint8_t motor_id) const` | Returns the 16-bit status word for motor 1–4. |
| `std::string get_motor_status_string(uint8_t motor_id) const` | Parses a motor status word into text such as `SWITCHED_ON \| TARGET_REACHED`. |
| `bool has_motor_fatal_error(uint8_t motor_id) const` | Checks whether the specified motor has a fatal fault such as encoder offline, overcurrent, or overvoltage. |

---

## 8. Asynchronous Data Recording

| Interface | Description |
| :--- | :--- |
| `void start_record(const CsvRecordConfig& cfg)` | Starts background asynchronous recording. Supports file-size rotation, maximum file count, and duration limits, with Gzip compression during recording. |
| `void record_sensors(const AllSensors& s)` | Enqueues the current sensor snapshot without blocking. |
| `void stop_record()` | Stops recording and tells the background thread to flush queued data safely to disk. |

> **💡 Tip**: When a single file reaches `max_file_size`, or when `stop()` is called, `CsvRecorder` automatically converts `.csv` to compressed `.csv.gz` in the background, significantly reducing storage use.
