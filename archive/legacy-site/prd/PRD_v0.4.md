# [历史归档] BodyOS SDK 开发者文档 PRD v0.4

日期：2026-11-13
状态：当前实施基线

## 1. 背景

旧版 Wiki 的目录和内容主要由前期讨论、个人资料与假设整理而成，覆盖 Getting Started、Mechanical、Hardware、Integrations、Troubleshooting 等多个栏目。开发团队目前实际交付并可作为技术依据的资料只有四份中文 Markdown 文档，因此需要推翻旧版发布架构，建立一个来源清晰、范围可控的 SDK 文档站。

## 2. 产品目标

- 让开发者快速理解 BodyOS SDK v2.0.0 的运行架构与部署方式。
- 分别提供可检索的 C++ 与 Python API 参考。
- 集中呈现四个官方示例及其安全机制。
- 保证网站上的技术内容可以追溯到开发团队原稿。
- 保留旧资料的历史记录，但不让它们进入当前导航、搜索与发布结果。

## 3. 正式内容来源

| 文档 | 页面职责 |
| --- | --- |
| `docs/api/README.md` | SDK 架构、特性、部署、快速开始、FAQ |
| `docs/api/C++_API_Reference.md` | C++ API 参考 |
| `docs/api/Python_API_Reference.md` | Python API 参考 |
| `docs/api/Examples_Guide.md` | C++/Python 官方示例 |

首页只做信息导航与范围说明，不定义新的技术规格。

## 4. 信息架构

```text
BodyOS SDK v2.0.0 开发者文档
├── 首页
├── SDK 开发者手册
├── C++ API
├── Python API
└── 官方示例
```

官方示例覆盖：

- `sensor_read_record`
- `body_assist_control`
- `body_expert_control`
- `direct_motor_control`

## 5. 用户与核心任务

主要用户为使用 C++ 或 Python 接入外骨骼控制能力的开发者。他们需要完成以下任务：

1. 理解 daemon 与客户端的通信架构。
2. 部署并建立 SDK 连接。
3. 选择正确的工作模式和 API。
4. 读取传感器或执行受控的驱动器操作。
5. 参考官方示例完成首个程序并排查常见问题。

## 6. 本期范围

- 中文单语言网站。
- MkDocs Material 展示、导航、搜索与代码复制。
- 五个正式页面。
- GitHub Actions 严格构建、结构检查与 GitHub Pages 部署。
- 当前架构的 Markdown、FreeMind `.mm` 与 OPML 导出文件。

## 7. 非本期范围

- 未经开发确认的英文技术翻译。
- 机械结构、硬件规格、研究资料、第三方集成和通用故障排查栏目。
- 根据旧版 Wiki 推断出的接口、参数或兼容性说明。
- 在线 API 沙箱、版本切换和自动生成接口文档。

## 8. 内容与安全原则

- 技术事实必须来自四份正式原稿或后续开发确认资料。
- 首页可以重新组织阅读路径，但不能扩大技术承诺。
- 电机控制和助力控制内容需要明确运行前提与风险。
- 旧内容只做历史保留，不得被网站搜索索引收录。

## 9. 验收标准

- 顶部导航只有：首页、SDK 开发者手册、C++ API、Python API、官方示例。
- 四份开发原稿均有独立页面且内容完整。
- 所有站内链接、页面锚点和资源地址有效。
- 搜索索引不包含旧版目录和旧 API 页面。
- HTML 页面语言为中文。
- `mkdocs build --strict` 和 `python scripts/check_docs.py` 均通过。
- 桌面端和移动端的核心导航、正文与代码块可正常阅读。
