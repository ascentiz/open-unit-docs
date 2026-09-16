# 开发者文档架构草案

日期：2026-09-16。此目录用于讨论与修改信息架构，不属于已发布网站内容。

## 当前采用的架构

`BodyOS_Developer_Docs_Architecture_Approved.md` 保存用户修改并确认的 Markdown 原稿，是当前网站导航的依据。一级栏目为 8 个；BodyOS 与 SDK 合并为 BodyOS SDK，定位为通过 .whl 分发的 Python SDK，不是完整操作系统。

本地网站已按此结构调整；API 和 Examples 保留原有预览页面。概览页用于落地导航，不额外扩展主题。旧资料保留 URL，详见根目录 PRD_v0.3.md。

下方 .mm／.opml 及说明属于早期讨论记录，未同步到确认版，不应作为当前产品定位或导航依据。

## 文件

- `BodyOS_Developer_Docs_Architecture_Draft.mm`：推荐导入的 FreeMind 思维导图，包含中英双语节点、栏目顺序与简单颜色设置。
- `BodyOS_Developer_Docs_Architecture_Draft.opml`：相同层级内容的备用大纲格式。

## 草案假设

用户给出的箭头被理解为 9 个同级一级栏目的阅读顺序，而不是逐层嵌套或软件执行流程：

Getting Started → Mechanical → Hardware: B-core Pi 1 → BodyOS → SDK → API → Examples → Integrations → Troubleshooting。

一级栏目沿用用户指定架构。按用户反馈，每个一级栏目只保留 2–3 个关键二级目录，共 19 个二级目录，不增加三级节点。二级节点全部是建议目录，供用户修改，不是已完成页面或正式产品功能承诺；例如 ROS 2 集成是否支持仍需确认。未提供任何猜测的硬件规格、引脚或协议参数。

建议职责边界：

- Getting Started：导航和首次成功接入闭环，通过链接引用其他栏目，避免重复完整教程。
- Mechanical：物理结构、装配、佩戴、安装与维护。
- Hardware：B-core Pi 1 板卡、供电、接口及物理连接。
- BodyOS：系统、服务、应用生命周期、安全边界和部署。
- SDK：开发工具包的安装与使用方法。
- API：接口契约、参数、数据结构、单位、错误码与版本参考。
- Examples：可运行或明确标注成熟度的示例项目。
- Integrations：外部工具与系统的集成流程。
- Troubleshooting：按症状组织的检查、诊断与反馈流程。

本轮不改动网站导航或正文，也不推送 GitHub。

## 导入 ProcessOn

在 ProcessOn“我的文件”页面选择“新建”→“导入”，选择 `.mm` 文件。如果该入口未识别 FreeMind，请改用 `.opml` 备用文件。

ProcessOn 官方手册列出对 `.mm` 与 `.opml` 的导入支持：[文件导入](https://www.processon.com/support/file-import)。本地已检查 XML 和层级一致性；未在用户 ProcessOn 账号中实际执行导入。

导入后可以改用组织结构图布局，拖动、重命名、增删节点，数字前缀可以保留或删除。

## 修改后交回

优先从 ProcessOn 导出 FreeMind（`.mm`）文件并上传到当前任务。也可以导出 ProcessOn 原生 `.pos` 文件。机器可读文件有助于保留所有层级与名称；截图仅作为布局参考。

ProcessOn 官方导出说明：[文件下载](https://www.processon.com/support/file-download)。

收到修改版后，再按最终架构进行现有页面迁移、新页面规划、中英文导航调整及 PRD 更新。
