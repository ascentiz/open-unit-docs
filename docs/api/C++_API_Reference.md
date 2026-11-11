# C++ API Reference (`client.hpp`)

返回主目录：[README](./README.md)

本模块提供与 `bodyos-daemon` 通信的 C++ 客户端接口。适用于需要极高性能的实时控制场景。

```cpp
#include <bodyos/app/client.hpp>
#include <bodyos/ipc/ipc_protocol.hpp>
```

---

## 1. 初始化与生命周期

```cpp
explicit BodyClient(const std::string& sock_path);
~BodyClient();
```

*   **参数**：`sock_path` 通常为 `bodyos::ipc::DEFAULT_SOCK_PATH`（即 `/run/bodyos/bodyos.sock`）。
*   **异常**：如果 Socket 连接失败或创建失败，会抛出 `BodyOsError` 异常。
*   **析构**：`~BodyClient()` 会自动停止内部的后台推流线程，并安全关闭底层 Socket 句柄。

---

## 2. 系统与状态

| 接口签名 | 详细说明 |
| :--- | :--- |
| `bool link_is_connected() const` | 检查底层物理硬件（如 STM32/驱动器）是否在线。如果连续 1.5 秒未收到任何模块心跳，判定为断开。 |
| `bool request_work_mode(WorkMode mode)` | 申请切换工作模式。<br>• `NONE`: 初始状态（拒绝一切读写）<br>• `DATA_COLLECT`: 仅采集（拒绝控制写入）<br>• `AZ_CONTROL`: AZ 设备接管（`gait_mode=0`）<br>• `USER_CONTROL`: 用户直控（`gait_mode=1`） |
| `WorkMode get_work_mode() const` | 查询当前守护进程所处的工作模式。 |

> **⚠️ 安全提示**：申请 `USER_CONTROL` 或 `AZ_CONTROL` 模式时，底层会强制进行安全停机（失能电机）并切换步态控制权。如果链路不通，申请会被 daemon 拒绝并返回 `false`。

---

## 3. 驱动器高频控制

以下接口建议在 1000Hz 控制循环中调用，底层采用单向发送机制，绝不阻塞主线程。

| 接口签名 | 详细说明 |
| :--- | :--- |
| `void set_motor_enable(bool enable, uint8_t node_mask = 0x0F)` | 电机使能/失能。`node_mask` 为位掩码：<br>`0x01`左髋, `0x02`右髋, `0x04`左膝, `0x08`右膝，`0x0F` 代表全部。 |
| `void set_torque(uint8_t node_mask, const float nm[4])` | 下发力矩 (Nm)。<br>**限幅**：`[-2.0, 2.0]`。 |
| `void set_velocity(uint8_t node_mask, const float turn_s[4])` | 下发速度 (圈/秒)。<br>**限幅**：`[-40.0, 40.0]`。 |
| `void set_position(uint8_t node_mask, const float turn[4])` | 下发位置 (圈)。<br>**限幅**：`[-32.0, 32.0]`。 |

### 步态与固件
| 接口签名 | 详细说明 |
| :--- | :--- |
| `void set_gait_mode(uint8_t mode)` | 0 = 底层算法接管，1 = 用户直接接管。 |
| `uint8_t get_gait_mode()` | 读取底层步态模式控制方式，0 = 底层算法接管，1 = 用户直接接管。 |
| `std::string get_firmware_version()` | 获取底层控制器的固件版本号。 |

---

## 4. 传感器数据获取（极速）

```cpp
std::optional<AllSensors> latest_sensors() const;
```

*   **特性**：**微秒级返回，无 IPC 网络开销**。内部采用懒加载机制，首次调用会自动拉起后台推流线程（与底层 100Hz 数据同步）。
*   **返回**：成功返回 `AllSensors` 结构体快照，断线或初始化中返回 `std::nullopt`。
*   **使用场景**：完美契合 1000Hz 主控循环，直接在内存中读取最新的传感器缓存，不阻塞。
*   **注意**：如果你发现读取到的 `link_state == 0`，说明物理硬件掉线，此时返回的数据是最后一次的有效快照。

---

## 5. 驱动器配置读写

| 接口签名 | 详细说明 |
| :--- | :--- |
| `void clear_error(uint8_t node_mask = 0x0F)` | 清除驱动器故障状态。 |
| `void save_config()` | 将当前配置保存到驱动器 Flash。 |
| `uint32_t read_config(DriverConfigIndex idx)` | 读取驱动器配置的 32 位原始值（如读取 `CONTROL_MODE`）。 |
| `void write_config_int(DriverConfigIndex idx, int32_t value)` | 写入整型配置。**注**：目前 SDK 出于安全考虑，仅开放写入 `CONTROL_MODE`。 |
| `void write_config_float(DriverConfigIndex idx, float value)` | 写入浮点型配置。**注**：目前 SDK 出于安全考虑，未开放。 |
| `void set_motor_control_mode(DriverControlMode mode)` | **智能配置**：先读取当前模式，不一致才下发，下发后自动回读验证。支持 `CURRENT`、`VELOCITY`、`POSITION_FILTER` 等。 |

---

## 6. BLE 助力与专家控制

SDK 提供了两套接口：**增量接口**（推荐）与**全量结构体接口**。

### 6.1 增量接口（强烈推荐，安全且无需了解结构体）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `void update_ble_assist(mode, scene, level, pause)` | 增量更新助力参数。内部自动拉取当前底层心跳作为基准，只修改传入的参数，未传的参数保留原值。 |
| `void update_ble_boost(uint8_t active)` | 增量更新 Boost 模式（0=启动，1=关闭）。 |
| `void update_ble_expert(mode, smooth, base, speed...)` | 增量更新专家模式参数。 |

### 6.2 全量下发结构体接口（底层透传，不推荐，需了解详细结构体细节）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `std::optional<BleAsistSetReqAck> ble_set_assist(const BleAsistSetReqAck& req)` | 全量下发助力参数，会阻塞等待硬件回 ACK 结构体。 |
| `std::optional<BleBootModeReqAck> ble_set_boost(const BleBootModeReqAck& req)` | 全量下发Boost参数，会阻塞等待硬件回 ACK 结构体。 |
| `std::optional<BleExpertModeReqAck> ble_set_expert(const BleExpertModeReqAck& req)` | 全量下发专家模式参数，会阻塞等待硬件回 ACK 结构体。 |

### 全量拉取
| 接口签名 | 详细说明 |
| :--- | :--- |
| `std::optional<BleExpertModeParamGetAck> ble_get_expert()` | 从硬件拉取全量的专家参数。 |

### 6.3 状态缓存读取（非阻塞）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `std::optional<BleAsistSetReqAck> fetch_ble_assist_status()` | 极速读取当前缓存的助力设置状态，不触发底层 CAN 事务。 |
| `std::optional<BleAsistSetReqAck> fetch_ble_boost_status()` | 极速读取当前缓存的Boost设置状态，不触发底层 CAN 事务。 |
| `std::optional<BleAsistSetReqAck> fetch_ble_expert_status()` | 极速读取当前缓存的专家模式设置状态，不触发底层 CAN 事务。 |

---

## 7. 报警与故障监控

| 接口签名 | 详细说明 |
| :--- | :--- |
| `uint32_t get_ble_alarms() const` | 获取 32 位报警掩码（如 CAN 通信断开、电机过温等）。 |
| `std::string get_ble_alarms_string() const` | 将掩码转为人类可读的报警文本（如 `L_HIP_OVER_TEMP | DRIVER_PROTECT`）。 |
| `bool has_critical_alarms() const` | 检查是否存在高危报警。**建议在 1000Hz 控制循环中调用，若为 true 应立即执行急停逻辑**。 |
| `uint16_t get_motor_status(uint8_t motor_id) const` | 获取指定电机（1~4）的 16 位状态字。 |
| `std::string get_motor_status_string(uint8_t motor_id) const` | 解析电机状态字（如 `SWITCHED_ON | TARGET_REACHED`）。 |
| `bool has_motor_fatal_error(uint8_t motor_id) const` | 检查指定电机是否包含编码器离线、过流、过压等致命故障。 |

---

## 8. 异步数据录制

| 接口签名 | 详细说明 |
| :--- | :--- |
| `void start_record(const CsvRecordConfig& cfg)` | 启动后台异步录制。支持文件大小滚动、最大文件数限制、录制时长限制。内部边写边用 Gzip 压缩。 |
| `void record_sensors(const AllSensors& s)` | 将当前传感器快照推入队列（非阻塞）。 |
| `void stop_record()` | 停止录制，通知后台线程将队列数据安全落盘。 |

> **💡 提示**：`CsvRecorder` 在写入单文件达到 `max_file_size` 或调用 `stop()` 时，会自动在后台将 `.csv` 转码为 `.csv.gz` 压缩文件，大幅节省设备存储空间。
