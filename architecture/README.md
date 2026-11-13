# 当前开发者文档架构

日期：2026-11-13。

本目录只保存当前、可发布的信息架构。当前结构结合两类已确认输入：

- 用户确认的四个系统组成部分与开发边界；
- 开发团队提供的四份中文 SDK Markdown 文档。

Exo Belt 与 B-core Pi 1 已恢复为正式页面，但只搭建框架；未知机械和硬件参数保持待确认。Exoskeleton Unit 作为封装单元在系统组成页说明，不展开内部硬件与驱动文档。

## 当前文件

- `BodyOS_SDK_v2_Developer_Docs_Architecture_Current_2026-11-13.md`：可直接编辑与评审的 Markdown 大纲
- `BodyOS_SDK_v2_Developer_Docs_Architecture_Current_2026-11-13.mm`：ProcessOn 推荐导入文件
- `BodyOS_SDK_v2_Developer_Docs_Architecture_Current_2026-11-13.opml`：ProcessOn 备用导入文件

旧版架构已移动到 `archive/legacy-site/architecture/`，不再代表当前网站。

## 导入 ProcessOn

在 ProcessOn 中选择“新建”→“导入”，优先选择 `.mm`。如果无法识别，再导入 `.opml`。

图中的“首页、产品与硬件、BodyOS SDK、官方示例”对应网站导航分组；下一级节点对应正式页面或页面内容主题。修改后可以从 ProcessOn 导出 `.mm` 或 `.opml`，再交回本仓库同步调整。
