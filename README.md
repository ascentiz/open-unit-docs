# BodyOS 开发者文档

本仓库使用 MkDocs Material 构建 BodyOS 中英双语开发者文档，并由 GitHub Pages 发布。网站同时覆盖产品组成、Exo Belt、B-core Pi 1，以及 BodyOS SDK。

## 内容基线

SDK 接口与示例以开发团队提供的四份中文 Markdown 文档为正式技术来源：

- `docs/api/README.zh.md`：SDK 开发者手册
- `docs/api/C++_API_Reference.zh.md`：C++ API
- `docs/api/Python_API_Reference.zh.md`：Python API
- `docs/api/Examples_Guide.zh.md`：官方示例

产品组成与开发边界依据当前确认的信息维护在：

- `docs/product/overview.zh.md`：四个组成部分及用户开发边界
- `docs/product/exo-belt.zh.md`：Exo Belt 机械文档框架
- `docs/product/b-core-pi-1.zh.md`：B-core Pi 1 硬件文档框架

Exo Belt 与 B-core Pi 1 页面只发布已确认的系统定位；未知尺寸、载荷、供电、引脚和接口参数统一标为待确认。Exoskeleton Unit 的内部硬件和驱动属于封装范围，用户在 B-core Pi 1 上通过 BodyOS SDK/API 获取数据和下发控制。

旧版的 Getting Started、Mechanical、Hardware、SDK、Integrations、Troubleshooting 等内容仍保留在仓库中，方便追溯，但已从网站导航、搜索和构建结果中排除。新的机械与硬件框架位于 `docs/product/`，不复用旧页面中的未确认参数。

## 当前信息架构

1. 首页
2. 产品与硬件
   - 系统组成与开发边界
   - 机械结构：Exo Belt
   - 硬件：B-core Pi 1
3. Installation
4. BodyOS SDK
   - SDK 开发者手册
   - API Reference
     - C++ API
     - Python API
   - Integration Libraries（规划中）
5. 官方示例

所有正式页面都同时使用 `.zh.md` 与 `.en.md` 后缀。构建系统采用语言后缀结构，中文为默认语言，英文发布在 `/en/`，页面间通过“中 / EN”切换。

## 本地预览

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

打开 `http://127.0.0.1:8000/open-unit-docs/`。

## 构建与检查

```bash
mkdocs build --strict
python scripts/check_docs.py
```

`check_docs.py` 会检查 20 个中英文正式页面、站内链接、锚点、搜索索引以及旧目录是否被排除。

## 发布

推送到 `main` 后，`.github/workflows/docs.yml` 会严格构建、运行检查并部署 GitHub Pages。

内容维护规则见 [AUTHORING.md](AUTHORING.md)，产品范围见 [PRD_v0.5.md](PRD_v0.5.md)。
