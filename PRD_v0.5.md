# BodyOS 开发者文档 PRD v0.5

日期：2026-11-13
状态：当前实施基线

## 1. 背景

开发团队提供的四份中文 Markdown 文档是 BodyOS SDK、C++ API、Python API 与官方示例的正式技术来源。同时，完整开发系统还包含 Exo Belt、B-core Pi 1 与封装的 Exoskeleton Unit。文档站既要保留机械和用户可接触硬件的入口，也要明确哪些能力属于封装范围，避免用户误以为可以直接访问外骨骼单元内部硬件或驱动。

## 2. 产品目标

- 说明 Exo Belt、B-core Pi 1、BodyOS SDK 与 Exoskeleton Unit 的组成关系。
- 明确用户在 B-core Pi 1 上通过 BodyOS SDK/API 获取数据和下发控制。
- 明确 Exoskeleton Unit 的内部硬件、设备驱动和固件实现不向用户开放。
- 为 Exo Belt 机械结构和 B-core Pi 1 硬件建立可持续补充的正式页面框架。
- 保留开发团队交付的四份 SDK 文档作为接口事实来源。
- 提供与中文结构一致的英文翻译，通过“中 / EN”在对应页面间切换。
- 排除旧版 Wiki 中未经确认的机械、硬件和产品参数。

## 3. 系统组成

| 组成部分 | 用户可见范围 | 文档状态 |
| --- | --- | --- |
| Exo Belt | 机械结构、装配与佩戴 | 框架已建立，具体资料待确认 |
| B-core Pi 1 | 硬件架构、供电、连接与板卡接口 | 框架已建立，具体资料待确认 |
| BodyOS SDK | SDK 架构、API、示例与 Python `.whl` 分发 | 四份开发原稿已接入；`.whl` 交付细节待确认 |
| Exoskeleton Unit | 对外提供受控的数据与控制能力 | 内部硬件、驱动和固件实现封装，不向用户开放 |

## 4. 用户开发路径

```text
开发者应用
    │
    │ 在 B-core Pi 1 上运行
    ▼
BodyOS SDK / 公开 API
    │
    ├── 获取 Exoskeleton Unit 的状态与传感器数据
    └── 向 Exoskeleton Unit 下发受控的控制请求
    ▼
Exoskeleton Unit（内部硬件与驱动封装）
```

用户不直接访问 Exoskeleton Unit 内部硬件、驱动、固件或未公开的内部通信接口。

## 5. 正式内容来源

### 5.1 SDK 技术原稿

| 文档 | 页面职责 |
| --- | --- |
| `docs/api/README.zh.md` | SDK 架构、特性、部署、快速开始、FAQ |
| `docs/api/C++_API_Reference.zh.md` | C++ API 参考 |
| `docs/api/Python_API_Reference.zh.md` | Python API 参考 |
| `docs/api/integration-libraries.zh.md` | 第三方传感器与外部设备集成库规划 |
| `docs/api/Examples_Guide.zh.md` | C++/Python 官方示例 |

### 5.2 产品框架页

| 文档 | 页面职责 |
| --- | --- |
| `docs/product/overview.zh.md` | 四个组成部分及开发边界 |
| `docs/product/exo-belt.zh.md` | Exo Belt 机械文档框架 |
| `docs/product/b-core-pi-1.zh.md` | B-core Pi 1 硬件文档框架 |

每个正式页面同时维护 `.zh.md` 与 `.en.md`。框架页只写已确认事实。具体规格缺失时必须显示“待确认”，不得引用旧版 Wiki 的推断内容补空；英文版不得新增中文事实来源中没有的技术承诺。

## 6. 信息架构

```text
BodyOS 开发者文档
├── 首页
├── 产品与硬件
│   ├── 系统组成与开发边界
│   ├── 机械结构：Exo Belt
│   └── 硬件：B-core Pi 1
├── BodyOS SDK
│   ├── SDK 开发者手册
│   ├── API Reference
│   │   ├── C++ API
│   │   └── Python API
│   └── Integration Libraries（规划中）
└── 官方示例
```

## 7. 页面要求

### 7.1 系统组成与开发边界

- 展示四个组成部分及各自职责。
- 展示从 B-core Pi 1 经 SDK/API 到 Exoskeleton Unit 的用户访问路径。
- 明确封装边界和禁止绕过的访问方式。

### 7.2 机械结构：Exo Belt

- 预留机械组成、结构图、装配、佩戴、适配、限制和维护章节。
- 未确认的尺寸、材料、载荷、活动范围和紧固要求不得给出数值。

### 7.3 硬件：B-core Pi 1

- 预留硬件架构、供电、连接、板卡接口、安装与环境要求章节。
- 说明用户应用和 SDK 的运行位置，以及与 Exoskeleton Unit 的访问关系。
- 未确认的电压、功耗、连接器、引脚和操作系统版本不得给出数值。

### 7.4 BodyOS SDK

- 保留开发原稿的接口、枚举、参数、频率、错误行为和安全说明。
- Python `.whl` 到位后补充准确的文件名、版本、依赖与安装命令。
- C++ 与 Python API 统一归入 API Reference。
- Integration Libraries 页面承接第三方传感器和外部设备集成能力；正式交付前保持“规划中”状态。

## 8. 非本期范围

- Exoskeleton Unit 内部硬件设计、设备驱动源码、固件实现和内部通信细节。
- 未经中文事实来源支持、会改变技术含义的英文扩写。
- 未经确认的机械、电气、引脚、环境与兼容性参数。
- 旧版 Research、Tutorials、Integrations 和通用 Troubleshooting 目录。

## 9. 验收标准

- 网站导航只包含首页、产品与硬件、BodyOS SDK 和官方示例四组入口。
- 9 个中文页面和 9 个英文页面可以正常打开并被搜索。
- 语言切换显示“中 / EN”，并进入当前页面的对应语言版本。
- Exo Belt 与 B-core Pi 1 页面明确标注当前框架状态和待确认项。
- 系统组成页清楚表达 B-core Pi 1 → SDK/API → Exoskeleton Unit 的访问路径。
- 旧版机械、硬件及其他目录不进入构建和搜索结果。
- 严格构建、站内链接、锚点、搜索范围和移动端显示检查通过。
