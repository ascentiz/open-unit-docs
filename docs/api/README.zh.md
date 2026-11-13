# BodyOS SDK v2.0.0 开发者手册

欢迎使用 BodyOS SDK。它是 BodyOS 面向开发者提供的开发工具包，支持通过 B-core Pi 1 获取外骨骼数据、下发控制请求，并集成第三方传感器与外部设备。

## 🌟 核心架构
BodyOS 基于 **“守护进程 + 客户端双 Socket”** 架构，彻底解决高频控制与大数据推流之间的资源竞争问题：
*   **bodyos-daemon**：独占底层物理总线（UART/CAN/SPI），负责维持 1000Hz 的高频控制循环、硬件状态缓存、健康监控与物理按键响应。内部采用**异步发送队列**，高频控制指令不阻塞 IPC 处理线程。
*   **应用层 (SDK)**：通过本地 Unix Domain Socket 与 daemon 通信，支持 C++ 与 Python。实现了控制指令的**瞬间入队非阻塞下发**与 100Hz 的高频传感器推流（非阻塞被动接收）。控制通道与数据通道完全隔离，客户端内部通过**独立后台发送线程**保障 Socket 流不被交错。

## ⚡ 核心特性
*   **双 Socket 隔离**：控制指令不阻塞推流，高频推流采用“慢客户端主动丢弃”机制，保护底层实时性。
*   **全链路异步发送**：客户端 `tx_worker` 线程与 daemon 侧 `CanFdTransport` 发送队列协同工作，高频控制（1000Hz）在主线程仅触发“入队”操作（微秒级），绝不阻塞。
*   **防爆队列机制**：无论客户端还是 daemon，当控制队列积压时，自动丢弃最旧的**控制类**指令（保留配置指令），确保机器人永远执行最新指令。
*   **同步请求防错乱**：对于读配置等需要同步应答的请求，内部通过 `req_id` 与 `msg_type` 双重校验，自动丢弃 Socket 中残留的旧包（Stale Packet），防止时序错乱。
*   **安全模式切换**：提供“只读采集”、“AZ闭环控制”、“用户直控”三种模式，互斥访问，防止飞车。
*   **极速缓存读取**：`latest_sensors()` 直接从内存获取快照，微秒级返回，完美契合 1000Hz 主控循环。
*   **物理按键联动**：支持外接 GPIO 按键，实现模式与档位的物理切换（独立线程，不被 CAN 总线超时阻塞）。
*   **高性能异步录制**：内置基于 Gzip 异步压缩的 CSV 录制器，零丢帧、不卡顿主循环。
*   **硬件异常兜底**：底层硬件无响应时，daemon 自动重试（默认 3 次，每次 800ms），最终向应用层返回安全默认值（如 `0`），防止上层业务崩溃。

## 🚀 快速开始

### 1. 部署守护进程
在目标设备（如树莓派 CM5）上，将 `bin/` 和 `config/` 拷贝至系统目录，并启动后台服务：
```bash
sudo cp bin/* /usr/local/bin/
sudo cp config/bodyos-daemon.service /etc/systemd/system/
sudo cp config/logrotate.bodyos /etc/logrotate.d
sudo systemctl daemon-reload
sudo systemctl enable --now bodyos-daemon
```
*日志默认保存在 `/var/log/bodyos/bodyos.log`，支持自动轮转与 Gzip 压缩。*

### 2. C++ 项目集成
在 `CMakeLists.txt` 中配置并引入：
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

### 3. Python 项目集成
将 `python/bodyos` 放入你的项目路径中，或直接 `pip install .`
```python
from bodyos import BodyClient, WorkMode

client = BodyClient()
client.request_work_mode(WorkMode.DATA_COLLECT)
sensors = client.latest_sensors()
if sensors:
    print(f"IMU Yaw: {sensors.data.imu.yaw}")
```

## 📚 详细文档导航
为了实现更好的阅读体验，核心接口说明与示例代码已拆分至以下独立文档，请点击查阅：

*   📘 **[C++ API 完整参考 (client.hpp)](./C++_API_Reference.md)**
    *   包含工作模式、电机高频控制（力矩/速度/位置）、配置读写、BLE 参数下发等底层接口。
*   📗 **[Python API 完整参考 (client.py)](./Python_API_Reference.md)**
    *   包含高级增量接口（自动合并状态）、异步录制、自动重连与内存对齐解析机制。
*   🚀 **[官方示例代码详解 (Examples)](./Examples_Guide.md)**
    *   包含 C++ 与 Python 双版本的 `sensor_read_record`、`body_assist_control` 等 4 个核心 Demo 的深入解析与安全机制讲解。

## ❓ 常见问题 (FAQ)

**Q: 申请工作模式时报错 `BodyOS Error: Daemon returned error code: 1`？**
A: 这通常意味着底层物理硬件链路不通（`link_state = 0`）。请检查 CAN 总线或串口线是否接好，或者等待底层硬件心跳上电稳定后再向 daemon 申请。

**Q: 高频下发控制指令时，为什么主程序不会卡死？**
A: SDK 内部实现了**全链路异步发送队列**。C++/Python 客户端调用 `set_torque()` 等高频接口时，仅执行“微秒级”的内存入队操作，真正的 Socket I/O 由后台独立线程（`tx_worker`）完成。即使 daemon 或底层总线拥堵，主控制循环也绝不会被阻塞。

**Q: 程序在退出时（如按 Ctrl+C）发生卡死或抛出 `IPC response mismatch`？**
A: 这是旧版的问题，现已彻底修复。客户端 `request()` 函数引入了**陈旧包过滤机制**，会自动丢弃 Socket 缓冲区中历史残留的 ACK 包，并带有 3 秒超时保护。退出阶段的停车指令会真实等待 daemon 回应，若底层硬件死机，也会在 3 秒后安全兜底退出，绝不会无限卡死。

**Q: 为什么数据没有压缩成 .csv.gz？**
A: 录制器在调用 `stop_record()` 后会启动后台 Gzip 线程。如果程序退出太快，后台线程可能来不及跑完。建议在 `stop_record()` 后加上 `sleep(500ms)` 等待压缩完成，或者在 daemon 的 systemd 配置中设置 `KillMode=process` 让子线程有时间收尾。

**Q: 如果底层 CAN 硬件彻底死机，程序会怎样？**
A: daemon 底层的 `transact_raw` 默认进行 3 次重试（每次超时 800ms），若依然失败，daemon 会捕获异常并向客户端返回兜底值（例如读取配置失败时返回 `0`）。客户端的同步读操作会在 3 秒超时后退出重试，而高频控制指令则因为有防爆队列保护，会自动丢弃发送失败或积压的旧指令，系统绝不会发生整体卡死。
