# BodyOS / Open Unit 文档站 PRD

版本：v0.1 · 现状梳理  
调研日期：2026-09-16  
仓库：[ascentiz/open-unit-docs](https://github.com/ascentiz/open-unit-docs)  
在线站点：[Ascentiz Open Unit](https://ascentiz.github.io/open-unit-docs/)  
调研基线：`main` 分支，提交 `82728114182b41ad579cf72bfd7d548169e4efef`

本文件保存第一版现状 PRD，作为后续逐步修改的基线。改版建议尚未实施，本文不代表控制软件或 SDK 的正式功能承诺。

## 1. 产品定位与目标

面向 Ascentiz 模块化外骨骼平台的开发者知识库，帮助用户理解平台架构、完成初次接入、了解控制与遥测接口，并开展应用开发及科研合作。

当前仓库是 MkDocs 技术文档站，首页已使用 BodyOS 名称，但不包含 BodyOS 控制软件或 SDK 实现。

主要目标：

- 降低开发者和合作实验室的入门成本。
- 明确应用开发与底层设备安全之间的职责边界。
- 集中管理教程、接口说明、示例和贡献规范。

当前属于早期文档框架，部分接口与代码明确标注为概念性占位内容。[来源：仓库说明](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/README.md)

## 2. 目标用户

| 用户 | 主要需求 |
|---|---|
| 嵌入式与控制工程师 | 理解硬件边界、设备接入及命令流程 |
| 机器人应用开发者 | 查找接口、遥测数据和应用示例 |
| 高校及科研实验室 | 建立实验流程、评估数据采集和合作条件 |
| 生态合作伙伴 | 理解软件、传感器与数据服务的集成方式 |

## 3. 当前内容功能

现有导航包含 8 个一级入口、22 个 Markdown 页面。

| 模块 | 现有内容 | 当前提供的价值 |
|---|---|---|
| 首页 | 平台定位、双层架构、设计原则、文档地图 | 帮助用户理解平台并选择阅读入口 |
| Getting Started | 入门概览、开发套件、首次会话 | 介绍环境准备、状态检查、遥测和命令会话 |
| Architecture | 架构概览、平台边界、安全模型 | 说明控制权、安全职责及会话状态 |
| API | 接口概览、Control API、Telemetry API | 描述会话、命令、拒绝原因、数据主题和消息格式 |
| Tutorials | 启动检查、安全门控命令、YouTube 嵌入规范 | 提供分步骤流程和视频辅助说明 |
| Examples | 遥测订阅、步态辅助循环 | 展示 Python 代码及高层控制伪代码 |
| Research | 科研概览、高校实验室合作 | 说明研究方向、合作前提和沟通流程 |
| Community | 社区概览、贡献指南、反馈规范 | 指导用户通过 Issue 和 PR 参与改进 |

上述功能主要是内容展示与指导，不是网页内直接连接或控制设备。[来源：导航配置](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/mkdocs.yml)

## 4. 当前网站交互功能

- 顶部分类导航、左侧章节导航及页内目录。
- 全站搜索、搜索建议和结果关键词高亮。
- 代码语法高亮及一键复制。
- 标题锚点、返回顶部及上一篇／下一篇导航。
- 跳转 GitHub 编辑对应文档源码。
- 提示块、折叠内容、表格和标签页内容格式支持。
- YouTube 视频嵌入，使用响应式播放器、懒加载，并保留文字操作说明。

当前配置为英文、单一浅色主题；未发现站内登录、后台 CMS、多语言切换或文档版本切换功能。[来源：网站配置](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/mkdocs.yml)、[视频规范](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/tutorials/embedding-youtube-videos.md)

## 5. 文档描述的平台架构

这部分是文档所描述的设计，不代表本仓库已实现对应软件。

| 层级 | 职责 |
|---|---|
| Exoskeleton Unit | 实时电机控制、执行器驱动、硬限制、安全联锁、看门狗及故障处理 |
| Open Unit / BodyOS | 高层控制策略、意图估计、传感器融合、实验应用、遥测处理及外部集成 |

核心原则：应用层可以请求动作，但最终由 Exoskeleton Unit 根据设备状态和安全限制决定接受、限制或拒绝请求。

文档提出的会话状态包括 `idle`、`unarmed`、`armed`、`fault`、`estop`，具体名称及接口仍可能演进。[来源：平台边界](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/architecture/platform-boundary.md)、[安全模型](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/architecture/safety-model.md)

## 6. 技术框架与维护方式

| 层面 | 当前实现 |
|---|---|
| 内容源 | Markdown，位于 `docs/` |
| 静态网站生成 | MkDocs |
| 页面主题 | Material for MkDocs |
| 内容扩展 | PyMdown Extensions |
| 样式定制 | `docs/assets/stylesheets/extra.css` |
| 导航与站点配置 | `mkdocs.yml` |
| 依赖管理 | `requirements.txt` |
| 自动构建与发布 | GitHub Actions → GitHub Pages |

依赖范围为 MkDocs `>=1.6,<2.0`、Material `>=9.5,<10.0`、PyMdown Extensions `>=10.7,<11.0`；部署环境使用 Python 3.11。

维护流程为：修改 Markdown／配置 → 本地预览 → 严格构建检查 → 提交 PR → 合并到 `main` 后自动部署。目前工作流支持 `main` 推送和手动触发，尚未配置 PR 自动构建检查。[来源：依赖文件](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/requirements.txt)、[部署工作流](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/.github/workflows/docs.yml)

本地预览命令为 `mkdocs serve`，严格构建命令为 `mkdocs build --strict`，生成网站位于 `site/`。

## 7. 当前不足与后续修改建议

以下为调研建议，尚未实施。

| 优先级 | 问题 | 建议 |
|---|---|---|
| P0 | 首页使用 BodyOS，站点标题及正文大量使用 Open Unit | 明确两者关系，统一品牌名称和术语 |
| P0 | 入门页引用 `Connect B-core pi 1.md`，但当前仓库没有该文件 | 补齐连接教程或移除无效链接 |
| P0 | API 和示例存在占位内容，容易被误认为可直接运行 | 统一标注“概念示例／已验证”，注明适用版本 |
| P1 | 硬件接入细节不足 | 补充接线图、接口表、安装步骤和故障排查 |
| P1 | 缺少完整、可验证的开发闭环 | 提供真实 SDK 安装及最小可运行示例 |
| P1 | PR 缺少自动构建验证 | 增加 PR 严格构建和链接检查 |
| P2 | 缺少版本与兼容性管理 | 增加发布说明、硬件／固件／SDK 兼容矩阵 |
| P2 | 视频仍为测试嵌入，版本信息为 TBD | 替换正式教程视频，补充适用版本及备用链接 |

问题依据：[首页](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/index.md)、[入门页](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/getting-started/index.md)、[API 成熟度说明](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/api/index.md)、[启动教程](https://github.com/ascentiz/open-unit-docs/blob/82728114182b41ad579cf72bfd7d548169e4efef/docs/tutorials/bring-up-workflow.md)。

## 8. 后续改版的基础验收标准

- 平台名称和术语一致。
- 导航、内部链接及页面资源有效。
- `mkdocs build --strict` 通过。
- 示例注明真实性、前置条件和适用版本。
- 关键操作包含预期结果、失败处理与停止条件。
- 视频不可播放时，文字教程仍可独立使用。

建议第一轮先完成命名统一、无效链接修复、入门流程补全和示例成熟度标注，形成可靠的开发者入口，再扩展 API 和科研内容。

## 9. 版本记录

| 版本 | 日期 | 内容 |
|---|---|---|
| v0.1 | 2026-09-16 | 保存首次仓库调研的现状 PRD；尚未实施改版 |
