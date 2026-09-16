# 平台介绍

本文档覆盖实体设备、硬件及面向开发者的软件工具包。

| 组成部分 | 文档范围 |
| --- | --- |
| Exo Belt | 机械结构、装配与佩戴 |
| B-core Pi 1 | 硬件架构、供电、连接及板卡接口 |
| BodyOS SDK | 通过 `.whl` 软件包分发的 Python SDK |
| Exoskeleton Unit | 设备本地驱动与最终安全约束执行 |

BodyOS 不是完整的操作系统。安装 wheel 是安装 Python 软件包，而不是刷写设备系统镜像或固件。

## 下一步

- 准备[首次运行](setup-and-first-run.md)。
- 阅读 [SDK 安装与配置](../sdk/installation-and-configuration.md)。
- 了解[架构与安全边界](../sdk/architecture-and-safety-boundary.md)。

!!! note "早期平台"
    SDK 包名、支持的运行时、设备兼容性及最终 API 必须依据实际发布版本编写。现有代码示例在验证之前仍属于概念示例。
