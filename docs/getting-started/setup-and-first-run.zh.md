# 环境准备与首次运行

!!! warning "待补充"
    尚未提供实际 SDK wheel 文件及已验证的连接说明。本页定义入门顺序，不是可以直接执行的硬件操作流程。

## 准备步骤

1. 确认设备版本及适用的[装配与佩戴](../mechanical/assembly-and-fit.md)说明。
2. 按照已批准的[供电与连接](../hardware/power-and-connection.md)流程操作。
3. 获取正式发布的 wheel，并在 [SDK 安装](../sdk/installation-and-configuration.md)说明中确认 Python 与平台兼容性。
4. 按照[基本使用](../sdk/basic-usage.md)导入实际软件包、连接设备并检查状态。
5. 先读取遥测，再尝试有界命令；不得绕过[安全边界](../sdk/architecture-and-safety-boundary.md)。

## 首次运行验收

- 记录硬件、固件、SDK 及 Python 版本。
- 确认软件包可导入，且识别的是目标设备。
- 在不请求运动的情况下读取状态及新鲜遥测。
- 关闭连接，确认最终状态安全。

正式版本可用后，在本页补充已验证的命令、预期输出及失败处理。早期[首次会话](first-session.md)仅作为概念参考，不是已验证的 SDK 测试。
