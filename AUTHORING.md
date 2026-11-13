# BodyOS 文档维护说明

## 1. 事实来源

SDK 技术内容只来自以下四个开发原稿：

- `docs/api/README.zh.md`
- `docs/api/C++_API_Reference.zh.md`
- `docs/api/Python_API_Reference.zh.md`
- `docs/api/Examples_Guide.zh.md`

产品组成和用户开发边界维护在以下三个页面：

- `docs/product/overview.zh.md`
- `docs/product/exo-belt.zh.md`
- `docs/product/b-core-pi-1.zh.md`

已确认的边界是：系统由 Exo Belt、B-core Pi 1、BodyOS SDK 和封装的 Exoskeleton Unit 组成；用户在 B-core Pi 1 上通过 SDK/API 获取外骨骼单元数据并下发控制；Exoskeleton Unit 的内部硬件和驱动不向用户开放。

开发团队提供新版本时，优先直接更新对应文件。不要根据宣传材料、个人笔记或旧版 Wiki 自行补写参数、兼容性、硬件规格或安全承诺。

## 2. 页面职责

- `docs/index.zh.md`：文档地图、阅读顺序、内容范围与必要安全提示。
- `docs/product/overview.zh.md`：四个组成部分、数据与控制路径、封装边界。
- `docs/product/exo-belt.zh.md`：机械结构、装配与佩戴的可维护框架。
- `docs/product/b-core-pi-1.zh.md`：硬件架构、供电、连接、板卡接口与开发工作流框架。
- `docs/api/README.zh.md`：架构、核心特性、部署、快速开始、文档导航与 FAQ。
- `docs/api/C++_API_Reference.zh.md`：C++ 接口参考。
- `docs/api/Python_API_Reference.zh.md`：Python 接口参考。
- `docs/api/integration-libraries.zh.md`：第三方传感器与外部设备集成库的规划和交付状态。
- `docs/api/Examples_Guide.zh.md`：四个官方示例的运行方式、逻辑与安全机制。

产品框架页不得用猜测填充具体规格。每项未知信息应保留“待确认”状态，直到取得负责团队提供的资料。

## 3. 修改原则

1. 保留开发原稿中的接口名、枚举、参数名、默认值、频率和错误行为。
2. 修正文案或排版时，不改变技术含义。
3. 新增技术结论前，先取得开发团队确认并记录来源。
4. 新增页面后，同时更新 `mkdocs.yml`、本文件、`README.md` 和 `scripts/check_docs.py`。
5. 控制类内容必须保留或补充与原稿一致的安全限制，尤其是电机直控示例。
6. Exoskeleton Unit 的内部硬件、驱动、固件和内部通信实现不应写成用户可访问接口。
7. Python `.whl` 的文件名、版本、依赖和安装命令在交付前保持待确认，不自行编造。
8. Integration Libraries 页面只记录正式交付或明确处于规划中的能力，不将预期设备写成已支持设备。

## 4. 旧内容处理

旧页面已移入 `archive/legacy-site/docs/` 作为历史资料保留，不参与网站构建。新的机械与硬件内容只维护在 `docs/product/`；不要把旧 `mechanical/` 或 `hardware/` 目录重新加入导航。

旧版信息架构保存在 `archive/legacy-site/architecture/`，不代表当前产品结构。

## 5. 本地验收

```bash
source .venv/bin/activate
mkdocs build --strict
python scripts/check_docs.py
```

提交前至少确认：

- 18 个中英文正式页面都能打开；
- 导航顺序正确；
- 页面内链接与锚点有效；
- 搜索只返回当前正式内容；
- 中文页面语言为 `zh`，英文页面语言为 `en`；
- “中 / EN”语言切换能进入对应页面；
- 旧版栏目没有出现在构建结果中。

## 6. 英文版本

中文页面统一使用 `.zh.md`，英文页面使用相同基础文件名的 `.en.md`。例如：

- `docs/product/overview.zh.md`
- `docs/product/overview.en.md`

英文版本已启用构建，发布路径为 `/en/`。中文原稿是 SDK 技术事实来源；英文稿应忠实翻译，不得新增中文原稿中没有的接口、参数、频率、安全保证或兼容性承诺。
