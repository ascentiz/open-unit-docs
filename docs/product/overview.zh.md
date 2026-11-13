# 系统组成与开发边界

BodyOS 开发系统由四个部分组成：外骨骼腰带（Exo Belt）、B-core Pi 1、BodyOS SDK 和 Exoskeleton Unit。开发者可接触并使用 B-core Pi 1 与公开 SDK/API；Exoskeleton Unit 的内部硬件、设备驱动和执行逻辑保持封装。

## 四个组成部分

| 组成部分 | 定位 | 当前文档范围 |
| --- | --- | --- |
| Exo Belt | 外骨骼腰带及其机械承载结构 | 机械结构、装配、佩戴与负载边界；具体参数待补充 |
| B-core Pi 1 | 用户可接触的计算与控制入口 | 硬件架构、供电、连接和板卡接口；具体参数待补充 |
| BodyOS SDK | 面向开发者的访问层 | SDK 架构、C++/Python API 与官方示例；Python SDK 后续通过 `.whl` 分发 |
| Exoskeleton Unit | 封装的设备执行单元 | 内部硬件和设备驱动不向用户开放，负责设备本地驱动与最终安全约束执行 |

## 用户可访问路径

```text
开发者应用
    │
    │  在 B-core Pi 1 上运行
    ▼
BodyOS SDK / 公开 API
    │
    │  获取状态与传感器数据 / 下发控制请求
    ▼
Exoskeleton Unit（封装）
    │
    └── 内部硬件、设备驱动与最终执行逻辑不向用户开放
```

开发者的标准工作路径是：在 B-core Pi 1 上部署并运行应用，通过 BodyOS SDK 调用公开 API，从 Exoskeleton Unit 获取数据或向其发送控制请求。开发者不需要、也不能直接访问 Exoskeleton Unit 的内部驱动和硬件实现。

## 开发者可以做什么

- 在 B-core Pi 1 上安装和运行经过支持的 SDK 与应用。
- 通过公开 API 获取 Exoskeleton Unit 提供的状态和传感器数据。
- 在公开 API、安全模式与参数约束范围内发送控制请求。
- 参考 C++、Python API 和官方示例实现自己的应用逻辑。

## 封装边界

- Exoskeleton Unit 的内部硬件架构不作为用户开发接口。
- Exoskeleton Unit 的设备驱动、固件实现和内部通信细节不向用户开放。
- 用户不得绕过 BodyOS SDK/API 直接控制封装单元。
- 控制请求是否执行，以及最终执行时的安全约束，由封装单元和已发布的软件接口共同保障。

!!! note "文档状态"
    本页描述产品组成和开发边界。具体机械尺寸、电气规格、接口定义与支持矩阵将在开发团队确认后补充；未确认信息不会作为正式参数发布。

## 继续阅读

- [机械结构：Exo Belt](exo-belt.md)
- [硬件：B-core Pi 1](b-core-pi-1.md)
- [SDK 开发者手册](../api/README.md)
