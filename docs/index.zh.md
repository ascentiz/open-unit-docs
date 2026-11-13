# BodyOS 开发者文档

本网站说明 BodyOS 外骨骼开发系统的组成、用户开发边界和 SDK 接口。系统由 Exo Belt、B-core Pi 1、BodyOS SDK 与封装的 Exoskeleton Unit 四部分组成。

!!! warning "安全提示"
    运行控制类示例前，请确认设备状态、通信链路与急停措施，并由熟悉设备的人员按已批准的操作流程执行。`direct_motor_control` 会直接向电机发送控制指令，必须特别谨慎。

## 文档地图

### [系统组成与开发边界](product/overview.md)

先了解四个组成部分之间的关系，以及用户可以接触的机械、硬件和软件边界。Exoskeleton Unit 的内部硬件和驱动处于封装状态，用户在 B-core Pi 1 上通过 BodyOS SDK/API 获取数据和下发控制。

### [机械结构：Exo Belt](product/exo-belt.md)

查看 Exo Belt 的机械结构、装配与佩戴文档框架。具体尺寸、材料、载荷和装配步骤将在团队确认后补充。

### [硬件：B-core Pi 1](product/b-core-pi-1.md)

查看 B-core Pi 1 的系统角色、开发工作流，以及硬件架构、供电、连接和板卡接口文档框架。

### BodyOS SDK

- [SDK 开发者手册](api/README.md)：了解 `bodyos-daemon + 客户端双 Socket` 架构、核心特性、部署、快速接入与常见问题。
- **API Reference**
    - [C++ API](api/C++_API_Reference.md)：查看 `BodyClient` 的生命周期、控制、传感器、配置、BLE、报警与录制接口。
    - [Python API](api/Python_API_Reference.md)：查看 Python 客户端的工作模式、控制、传感器、配置、BLE、报警与录制接口。
- [Integration Libraries（规划中）](api/integration-libraries.md)：后续提供第三方传感器和外部设备的集成库与适配说明。

### [官方示例](api/Examples_Guide.md)

阅读 C++ 与 Python 双版本的四个官方示例：

- `sensor_read_record`：传感器读取与异步录制
- `body_assist_control`：BLE 助力模式控制
- `body_expert_control`：专家参数调整
- `direct_motor_control`：底层电机直接控制

## 建议阅读顺序

1. 先阅读 [系统组成与开发边界](product/overview.md)，明确可访问范围。
2. 根据需要查看 [Exo Belt](product/exo-belt.md) 与 [B-core Pi 1](product/b-core-pi-1.md) 框架页。
3. 阅读 [SDK 开发者手册](api/README.md)，理解运行架构并完成部署。
4. 在 **API Reference** 中根据项目语言选择 [C++ API](api/C++_API_Reference.md) 或 [Python API](api/Python_API_Reference.md)。
5. 需要接入第三方传感器或设备时，查看 [Integration Libraries](api/integration-libraries.md) 的交付状态。
6. 最后参考 [官方示例](api/Examples_Guide.md) 完成首个可运行程序。

## 当前文档范围

BodyOS SDK 的正式技术内容来自开发团队提供的四份中文 Markdown 文档。Exo Belt 与 B-core Pi 1 当前只发布经过确认的系统定位和文档框架；未知机械参数、硬件规格、引脚与连接方式统一标记为待确认，不根据旧资料推断。
