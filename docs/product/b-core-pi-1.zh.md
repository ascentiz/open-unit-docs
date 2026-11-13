# 硬件：B-core Pi 1

B-core Pi 1 是用户可接触的计算与控制入口。开发者在 B-core Pi 1 上部署应用，通过 BodyOS SDK/API 从 Exoskeleton Unit 获取数据并发送控制请求。

!!! info "当前状态"
    本页为硬件文档框架。板卡规格、供电参数、连接器定义、引脚、操作系统版本和环境限制均需等待硬件或开发团队确认。

## 在系统中的作用

B-core Pi 1 位于开发者应用与封装的 Exoskeleton Unit 之间：

```text
开发者应用（B-core Pi 1）
        ↕
BodyOS SDK / 公开 API
        ↕
Exoskeleton Unit（封装）
```

开发者不直接访问 Exoskeleton Unit 的内部驱动。数据读取和控制均应通过已发布的 BodyOS SDK/API 完成。

## 开发者工作流

1. 按经过确认的说明为 B-core Pi 1 供电并连接外骨骼系统。
2. 在 B-core Pi 1 上准备受支持的软件运行环境。
3. 安装或部署 BodyOS SDK；Python SDK 后续通过 `.whl` 文件分发。
4. 运行数据读取或控制应用。
5. 通过 SDK/API 接收 Exoskeleton Unit 数据，或在安全约束内发送控制请求。

## 硬件架构

| 待补充项目 | 需要的资料 | 当前状态 |
| --- | --- | --- |
| 计算核心 | 处理器、内存与存储规格 | 待硬件团队提供 |
| 系统架构图 | 主要器件、总线和接口关系 | 待提供 |
| 支持环境 | 操作系统、架构与版本要求 | 待开发确认 |
| 外形与安装 | 尺寸、重量、固定方式 | 待确认 |
| 环境条件 | 工作温度、存储温度与防护要求 | 待确认 |

## 供电

以下信息补齐前，不应自行推断或接线：

- 输入电压与允许范围
- 典型及峰值功耗
- 电源连接器型号与极性
- 上电、断电和复位顺序
- 过流、反接与异常断电保护

## 连接与板卡接口

后续接口章节至少应包含：

- 与 Exoskeleton Unit 的外部连接方式
- 与 Exo Belt 的安装及线缆关系
- 网络、调试与存储接口
- 用户可用的板卡接口及用途
- 连接器编号、方向、引脚和电气限制
- 禁止用户使用或保留的接口

## 软件部署入口

具体安装命令以开发团队交付的软件包为准。当前 SDK 架构、API 和示例见：

- [SDK 开发者手册](../api/README.md)
- [C++ API](../api/C++_API_Reference.md)
- [Python API](../api/Python_API_Reference.md)
- [官方示例](../api/Examples_Guide.md)

## 安全与封装边界

- 仅使用文档明确开放的供电、连接器和板卡接口。
- 不通过未公开接口绕过 BodyOS SDK/API 控制 Exoskeleton Unit。
- 未确认供电和引脚定义前，不进行自行接线或带电调试。
- Exoskeleton Unit 的内部硬件、驱动和固件不属于 B-core Pi 1 用户开发范围。

## 关联页面

- [系统组成与开发边界](overview.md)
- [机械结构：Exo Belt](exo-belt.md)
