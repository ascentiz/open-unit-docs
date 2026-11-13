# Python API Reference (`client.py`)

[← 返回 BodyOS SDK 开发者手册](./README.md)

本模块提供一个零第三方依赖的纯 Socket 通信客户端，并在内部使用了 `ctypes` 完美对齐 C++ 的底层内存结构，实现了极高性能的数据解析。此外，Python 端还提供了更符合脚本习惯的高级增量接口与自动重连机制。

```python
from bodyos import BodyClient, WorkMode, CsvRecordConfig
```

---

## 1. 初始化与生命周期

```python
client = BodyClient(sock_path="/run/bodyos/bodyos.sock")
```
*   **参数**：`sock_path` 默认为守护进程的本地控制 Socket 路径。
*   **异常**：如果连接失败，会抛出 `BodyOsError`。
*   **资源释放**：支持上下文管理器，推荐使用 `with BodyClient() as client:`，或者在使用完毕后调用 `client.close()`，以确保内部的后台推流线程被安全停止。

---

## 2. 系统与工作模式

| 接口签名 | 详细说明 |
| :--- | :--- |
| `bool link_is_connected()` | 检查底层物理硬件（如 STM32）是否在线。连续 1.5 秒无数据判定为掉线。 |
| `bool request_work_mode(mode: WorkMode)` | 申请切换工作模式。<br>• `WorkMode.NONE`: 初始状态<br>• `WorkMode.DATA_COLLECT`: 仅采集（拒绝控制）<br>• `WorkMode.AZ_CONTROL`: AZ设备接管<br>• `WorkMode.USER_CONTROL`: 用户直控 |
| `WorkMode get_work_mode()` | 查询当前守护进程所处的工作模式。 |

> **⚠️ 安全提示**：如果底层物理链路断连（`link_state = 0`），申请切换模式可能会被 daemon 拒绝并返回 `False`。

---

## 3. 驱动器高频控制

Python 端的控制接口极其简单。所有传入的 `list` 长度如果不足 4 个，SDK 会自动补齐为 `0.0`。底层采用非阻塞发送机制，完美契合 1000Hz 的主控循环。

| 接口签名 | 详细说明 |
| :--- | :--- |
| `set_motor_enable(enable: bool, node_mask: int = 0x0F)` | 电机使能/失能。`node_mask` 掩码，`0x0F` 代表全部 4 个电机。 |
| `set_torque(node_mask: int, torques: List[float])` | 下发力矩 (Nm)。<br>**限幅**：`[-2.0, 2.0]`。 |
| `set_velocity(node_mask: int, speeds: List[float])` | 下发速度 (圈/秒)。<br>**限幅**：`[-40.0, 40.0]`。 |
| `set_position(node_mask: int, positions: List[float])` | 下发位置 (圈)。<br>**限幅**：`[-32.0, 32.0]`。 |

### 步态与固件
| 接口签名 | 详细说明 |
| :--- | :--- |
| `set_gait_mode(mode: int)` | 0 = 底层算法接管，1 = 用户直接接管。 |
| `int get_gait_mode()` | 读取底层步态模式控制方式，0 = 底层算法接管，1 = 用户直接接管。 |
| `str get_firmware_version()` | 获取底层控制器的固件版本号。 |

---

## 4. 传感器读取与断线重连

```python
sensors = client.latest_sensors()
if sensors and sensors.link_state == 1:
    print(f"IMU Yaw: {sensors.data.imu.yaw}")
```

*   **极速读取**：`latest_sensors()` 直接从本地内存读取快照，耗时在微秒级，**没有任何网络 I/O 开销**。
*   **推流懒加载**：首次调用该接口时，SDK 会在后台自动建立推流连接，并启动独立线程持续更新本地缓存。
*   **自动重连**：如果 daemon 进程重启或网络断开，后台线程会在每 1 秒尝试重连 `bodyos_stream.sock`，恢复后 `link_state` 会自动变为 `1`。
*   **数据结构**：返回的 `AllSensors` 对象中的 `data` 字段是一个嵌套的 `dataclass`，您可以直接使用 `.data.imu.yaw`、`.data.motors[0].speed` 等符合直觉的属性访问。

---

## 5. 驱动器配置读写
| 接口签名 | 详细说明 |
| :--- | :--- |
| `clear_error(node_mask: int = 0x0F)` | 清除驱动器故障状态。 |
| `save_config()` | 将当前配置保存到驱动器 Flash。 |
| `int read_config(idx: DriverConfigIndex)` | 读取驱动器配置的 32 位原始值（如读取 `CONTROL_MODE`）。 |
| `write_config_int(idx: DriverConfigIndex, value: int)` | 写入整型配置。**注**：目前 SDK 出于安全考虑，仅开放写入 `CONTROL_MODE`。 |
| `write_config_float(DriverConfigIndex idx, value: float)` | 写入浮点型配置。**注**：目前 SDK 出于安全考虑，未开放。 |
| `set_motor_control_mode(mode: DriverControlMode)` | **智能配置**：先读取当前模式，不一致才下发，下发后自动回读验证。支持 `CURRENT`、`VELOCITY`、`POSITION_FILTER` 等。 |

---

## 6. BLE 高级增量控制（特色接口）

与 C++ 全量结构体不同，Python 端封装了极其友好的增量接口。**用户只需修改关心的字段，底层自动对比并合并**，有效防止未传字段被意外清零。

### 6.1 增量下发（强烈推荐，安全且无需了解结构体）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `update_ble_assist(mode, scene, level, active)` | 增量更新助力参数。例如：`update_ble_assist(level=50)` 仅改变挡位，模式与场景保留。 |
| `update_ble_boost(active: int)` | 增量更新 Boost 模式（0=启动，1=关闭）。 |
| `update_ble_expert(mode, smooth, base, speed, freq, resp, coeff)` | 增量更新专家模式参数。首次调用会自动静默拉取底层全量参数作为基准。 |

### 6.2 状态缓存读取（极速）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `fetch_ble_assist_status()` | 极速读取当前助力状态缓存（非阻塞），返回 `BleAsistSetReqAck` 或 `None`。 |
| `fetch_ble_boost_status()` | 极速读取 Boost 状态缓存。 |
| `fetch_ble_expert_status()` | 极速读取专家模式状态缓存。 |

### 6.3 全量下发（不推荐使用，需了解详细结构体细节）
| 接口签名 | 详细说明 |
| :--- | :--- |
| `Optional[BleAsistSetReqAck] ble_set_assist(req: BleAsistSetReqAck)` | 全量下发助力参数，会阻塞等待硬件回 ACK 结构体。 |
| `Optional[BleBootModeReqAck] ble_set_boost(req: BleBootModeReqAck)` | 全量下发Boost参数，会阻塞等待硬件回 ACK 结构体。 |
| `Optional[BleExpertModeReqAck] ble_set_expert(req: BleExpertModeReqAck)` | 全量下发专家模式参数，会阻塞等待硬件回 ACK 结构体。 |

### 全量拉取
| 接口签名 | 详细说明 |
| :--- | :--- |
| `ble_get_expert()` | 主动向底层硬件发起 CAN 事务，拉取一次全量专家参数。 |

---

## 7. 报警与电机状态监控

| 接口签名 | 详细说明 |
| :--- | :--- |
| `get_ble_alarms() -> int` | 获取 32 位报警掩码。 |
| `get_ble_alarms_string() -> str` | 将掩码转为可读字符串（如 `L_HIP_CAN_ERR | R_KNEE_OVER_TEMP`）。 |
| `has_critical_alarms() -> bool` | 检查是否存在高危报警。**建议在主控循环中调用，若为 true 应立即执行急停。** |
| `get_motor_status(motor_id: int) -> int` | 获取指定电机（1~4）的 16 位状态字。 |
| `get_motor_status_string(motor_id: int) -> str` | 解析电机状态字（如 `SWITCHED_ON | TARGET_REACHED`）。 |
| `has_motor_fatal_error(motor_id: int) -> bool` | 检查指定电机是否包含编码器离线、过流、过压等致命故障。 |

---

## 8. 异步 CSV 压缩录制

Python 端内置了异步双缓冲队列，录制操作绝不会阻塞主控循环。

```python
from bodyos import CsvRecordConfig

# 1. 配置录制参数
cfg = CsvRecordConfig(
    dir_path="/tmp/bodyos_data",
    file_prefix="sensor_log",
    max_file_size=10 * 1024 * 1024, # 单文件 10MB 滚动
    max_files=5,                    # 最多保留 5 个文件
    duration_sec=60                 # 录制 60 秒后自动停止
)

# 2. 开始录制（立刻返回）
client.start_record(cfg)

# 3. 在主循环中投递数据（微秒级非阻塞）
client.record_sensors(sensors)

# 4. 停止录制（通知后台线程安全落盘并压缩）
client.stop_record()
```

> **💡 提示**：调用 `stop_record()` 后，后台线程会自动把遗留的 `.csv` 文件使用 Zlib Gzip 压缩为 `.csv.gz` 格式，并删除原文件，以节省设备存储。
