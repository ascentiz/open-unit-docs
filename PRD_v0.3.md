# BodyOS 开发者文档 PRD v0.3

日期：2026-09-16。本文记录本地实施阶段及后续调整；实际发布状态以 GitHub Actions 的 docs 工作流为准。

## 目标

按用户修改并确认的架构建立精简的中英双语开发者文档。BodyOS 定位为通过 .whl 分发的 Python SDK，不作为完整操作系统。后续作者以 Markdown 写作为主，无需反复开发网站。

架构依据：architecture/BodyOS_Developer_Docs_Architecture_Approved.md。历史 PRD v0.1／v0.2 保留，不覆盖。

## 信息架构

1. Getting Started：Platform Overview、Setup and First Run。
2. Exo Belt Mechanical：Structure Overview、Assembly and Fit。
3. Hardware: B-core Pi 1：Hardware Architecture、Power and Connection、Board and Interfaces。
4. BodyOS SDK：Installation and Configuration、Basic Usage、Architecture and Safety Boundary。
5. API：保留现有 Control API、Telemetry API 预览页面，不扩展未经确认的接口分类。
6. Examples：保留现有 Streaming Telemetry、Assistive Gait Loop 预览页面。
7. Integrations：ROS 2、External Devices and Tools。
8. Troubleshooting：Common Issues、Logs and Feedback。

共 8 个一级栏目；用户明确的 14 个二级主题按原稿落地。各栏目的概览页作为入口，不增加三级目录。首页属于 Getting Started 概览，不增加第 9 个一级栏目。

## 范围与内容策略

- MkDocs + Material + static-i18n，沿用现有样式与 GitHub Pages 工作流。
- 英文沿用根路径，中文 /zh/，同页语言切换及双语搜索继续支持。
- 新增 19 对页面，原有 22 对页面保留，共 41 对／82 个语言页面。
- 机械、硬件、SDK 和集成资料不足的页面明确标注待补充，仅提供作者提纲；不猜测引脚、电气参数、软件包名称、Python 兼容版本及 ROS 2 支持。
- SDK 安装页仅给通用 pip 模板，需替换实际 wheel 路径；不声称已测试实际产品安装。
- 原 architecture、tutorials、research、community 和早期入门页保留原 URL；不占一级导航，由首页补充资料及相关链接访问。
- API／示例明确属于概念预览，尚未与实际 wheel 验证。
- README 说明维护方法，AUTHORING.md 提供中文操作指南。
- 发布工作流增加双语一致性检查，检查失败不发布。

## 日常维护

已有页：编辑同名 .md 和 .zh.md → 本地预览／检查 → 提交并推送或合并至 main → GitHub Actions 自动发布。

新增页：创建双语文件并更新 mkdocs.yml 的 nav／nav_translations。特殊布局、交互和样式才需要网站开发。提交本身不会发布，需推送／合并及工作流成功，GitHub Pages 需配置为 GitHub Actions。

## 验收

- 严格构建通过。
- 双语检查通过：41 英文 + 41 中文，代码块、语言标记、对应语言／编辑链接、内部资源、锚点及搜索索引。
- Playwright 浏览器检查通过：1440×1000 桌面导航包含完整 8 栏目；SDK 安装页中文切换至对应英文页；390×844 手机正文与菜单正常显示。截图位于 output/playwright/，不提交发布。
- 已知非阻塞问题：Material 在语言／深层页面请求不存在的局部 sitemap；仓库 latest release 查询返回 404。正文、导航及已验证的同页语言切换不受影响。实际 wheel 安装与硬件调用尚未验证。
- 无 GitHub 推送或线上发布；真实硬件、SDK 及 ROS 2 集成验证不在本次范围。

## 后续资料

实际 .whl、发布版本和兼容矩阵；经过批准的机械图纸／佩戴步骤；B-core Pi 1 规格与接口表；真实 SDK API 与最小运行示例；已验证的外部集成方案和故障日志说明。

## 后续调整 读取外骨骼本体

2026-09-16：用户提供 AZ算力盒展会版本操作说明1.docx，要求替换当前示例。

- 当前示例仅保留“读取外骨骼本体”，中英文路径为 examples/read-exoskeleton/ 和 zh/examples/read-exoskeleton/。
- 原遥测数据流、步态辅助循环的中英文源文件移到 architecture/archive/examples/，不进入网站导航、搜索和发布，可恢复。
- 新例说明展会连接方式、SSH 登录、算力盒上的 az_sdk／demo.py、状态和传感器读取、CSV 记录能力及 Windows 数据查看。
- 文件名 az_sdk-1.4.0-cp314-cp314-linux_aarch64.whl 对应 CPython 3.14／Linux AArch64，限该展会版本，不作为整个 SDK 的通用兼容承诺。
- 未上传实际 demo.py／wheel，不编造函数、返回字段、端口或 CSV 路径，不声称实际运行验证。
- 公开页面去除所有密码；不收录非穿戴情况下人工限制电机转动的操作；保留开机运动与穿戴检测警告。
- 上文 41 对页面为架构调整时的历史统计；本次替换后为 40 英文 + 40 中文页面。
- 验证通过：严格构建、40 对页面双语检查；导航仅一个当前示例；旧示例不出现在搜索索引或发布目录；公开源文及生成站点无原文密码；本地新页面返回 HTTP 200。实际设备及 demo 未执行。

## 发布调整 语言切换入口

用户要求将页头语言切换图标改为“中/EN”，并上传当前版本至 GitHub、通过 GitHub Actions 部署 GitHub Pages。

- 使用 overrides/partials/alternate.html 保留 Material 下拉菜单及插件生成的对应页面链接，仅替换入口文字。
- 英文、简体中文选项及无障碍语言标签保持可用。
- 双语检查增加入口文字、无障碍标签及菜单目标验证，覆盖全部 80 个语言页面。
- 推送目标：ascentiz/open-unit-docs 的 main；站点：https://ascentiz.github.io/open-unit-docs/。
