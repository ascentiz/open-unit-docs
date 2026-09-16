# 开发者文档维护指南

框架已搭好。日常写文档不需要重新设计网站，也不需要修改 SDK 软件。

## 修改已有页面

1. 在 docs/ 找到对应文件：page.md 是英文，page.zh.md 是中文。
2. 同步编辑两种语言的正文、图片说明和安全提示。代码块保持一致，注明测试版本。
3. 本地预览，运行严格构建和双语检查。
4. 提交需要的源文件并推送到 main；团队协作时先提交 PR，再合并到 main。
5. 在 GitHub Actions 确认 docs 工作流成功，再检查线上页面。

仅保存或本地 commit 不会更新线上网站。推送／合并后，工作流成功才会发布；GitHub Pages 的 Source 需要设为 GitHub Actions。

## 预览与检查

在项目根目录执行；首次安装环境见 README。

```bash
source .venv/bin/activate
mkdocs serve --dev-addr 127.0.0.1:8000
```

英文：http://127.0.0.1:8000/open-unit-docs/

中文：http://127.0.0.1:8000/open-unit-docs/zh/

检查命令在另一个终端执行；先停止预览，避免两个构建进程同时写 site：

```bash
source .venv/bin/activate
mkdocs build --strict
python scripts/check_i18n.py
```

检查涵盖中英页面成对、代码块一致、语言标记、对应语言切换、编辑链接、内部资源及锚点、搜索索引；不自动判断翻译质量或硬件／SDK 真实性。

## 新增页面

- 创建同名中英文文件，例如 docs/sdk/new-topic.md 和 docs/sdk/new-topic.zh.md。
- 在 mkdocs.yml 的 nav 登记英文名称和不带语言后缀的源文件路径。
- 在中文语言配置的 nav_translations 登记中文名称。
- 两种语言都用普通相对链接，例如 ../api/control-api.md，不要手动加 /zh/。
- 图片放入 docs/assets/，通过相对路径引用，共享资源无需复制。
- 刻意不进入主导航的辅助页登记到 not_in_nav，并从相关页面提供入口。

新增一级栏目同样只需改配置；配色、布局、自定义交互或构建工具变更才涉及网站开发。

## 当前栏目与内容状态

Getting Started → Exo Belt Mechanical → Hardware: B-core Pi 1 → BodyOS SDK → API → Examples → Integrations → Troubleshooting。

BodyOS 是通过 .whl 分发的 Python SDK，不是完整操作系统。实际软件包名称、兼容版本、调用方式、硬件参数及 ROS 2 支持情况，以正式资料为准。“待补充”页面是编写骨架，不是功能承诺。现有 API 仍为预览；当前示例依据展会操作说明整理，需与实际 demo 和设备版本核对。

原 architecture、tutorials、research、community 和早期入门页保留原 URL，可从首页补充资料及相关页面访问。

## 提交与安全

只提交本次需要的源文件；无需提交自动生成的 site/、.venv/ 或浏览器检查产物。不要提交账号凭据、令牌和未经授权的实验数据。

涉及接线、供电、佩戴及动作控制时，仅使用经过批准和验证的步骤。替换预览 API／示例前，与真实 wheel 和硬件版本核对。
