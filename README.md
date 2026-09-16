# BodyOS Developer Documentation

This repository contains the bilingual MkDocs documentation site for Exo Belt, B-core Pi 1, and the BodyOS Python SDK. BodyOS is distributed as a `.whl` package, not a complete operating system.

日常写作只需编辑 Markdown、检查构建、提交并推送，或通过 PR 合并到 main。无需重新开发网站。参见 [文档维护指南](AUTHORING.md)。修改已有页面不需要改配置；新增页面需要登记导航；改样式或特殊交互才需要开发。

当前信息架构以 [确认版架构](architecture/BodyOS_Developer_Docs_Architecture_Approved.md) 为准，实施说明见 [PRD v0.3](PRD_v0.3.md)。尚未确认的硬件及 SDK 信息已标注待补充，API 仍为预览内容；当前示例依据展会操作说明整理，尚未进行设备验证。

The docs are structured for:

- robotics developers building applications on top of Open Unit
- researchers evaluating control, sensing, and telemetry workflows
- university labs collaborating on experimental protocols and integration work
- ecosystem partners integrating hardware, software, and data services

## Stack

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Static i18n](https://ultrabug.github.io/mkdocs-static-i18n/) for English and Simplified Chinese localization

## Languages / 中英双语

The site supports English and Simplified Chinese. English keeps the existing root URLs; Chinese pages are built under `/zh/`. Use the header language selector to switch to the corresponding page in the other language.

本站支持英文与简体中文。英文保留原有根路径，中文页面位于 `/zh/`。使用页头语言菜单，可切换到另一种语言的对应页面；导航、搜索提示及目录界面随语言切换。

### Maintaining translations / 维护翻译

- Keep English source files as `page.md`; add Chinese translations beside them as `page.zh.md`.
- 英文页面使用 `page.md`，中文翻译使用同目录下的 `page.zh.md`。
- Use unsuffixed relative Markdown links in both languages, for example `../api/control-api.md`; the i18n plugin selects the localized destination automatically.
- 两种语言均使用不带语言后缀的相对 Markdown 链接，例如 `../api/control-api.md`，插件会自动选择对应语言页面。
- Add new navigation items in `mkdocs.yml` and their Chinese labels under `nav_translations`.
- 新增页面时，更新 `mkdocs.yml` 导航，并在 `nav_translations` 中添加中文名称。
- Update both versions together. Preserve code, API identifiers, numeric units, safety constraints, and early-platform caveats.
- 修改内容时同步更新中英文版本，保持代码、API 标识符、数值单位、安全约束及早期平台说明一致。
- Translate visible text and HTML iframe titles, but keep shared asset paths and code samples unchanged.
- 翻译可见文字及 iframe 标题，但保持共享资源路径和代码示例不变。

After building, run the bilingual consistency check:

构建后运行双语一致性检查：

```bash
python scripts/check_i18n.py
```

## Project Layout

```text
.
├── .github/
│   └── workflows/
│       └── docs.yml
├── docs/
│   ├── api/
│   ├── architecture/
│   ├── assets/
│   │   └── stylesheets/
│   ├── community/
│   ├── examples/
│   ├── getting-started/
│   ├── mechanical/
│   ├── hardware/
│   ├── sdk/
│   ├── integrations/
│   ├── troubleshooting/
│   ├── research/
│   ├── tutorials/
│   └── index.md
├── .gitignore
├── AUTHORING.md
├── mkdocs.yml
└── requirements.txt
```

## Local Setup

1. Create and activate a virtual environment.

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the documentation dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Start the local documentation server.

   ```bash
   mkdocs serve
   ```

4. Open `http://127.0.0.1:8000/open-unit-docs/` in your browser.

   English: `http://127.0.0.1:8000/open-unit-docs/`; 简体中文：`http://127.0.0.1:8000/open-unit-docs/zh/`.

   The preview uses the `/open-unit-docs/` base path configured in `site_url`, matching GitHub Pages.

   本地预览使用 `site_url` 中配置的 `/open-unit-docs/` 子路径，与 GitHub Pages 保持一致。

## Build

Run a strict production build locally before opening a pull request:

```bash
mkdocs build --strict
python scripts/check_i18n.py
```

The generated site will be written to `site/`.

## Deployment

This repository includes a GitHub Actions workflow for GitHub Pages deployment at `.github/workflows/docs.yml`.

The workflow builds both languages, checks bilingual consistency, and deploys only after these checks pass. A local commit alone does not publish the site. Push to main (or merge a PR into main) to trigger publication, with GitHub Pages configured for GitHub Actions.

工作流在双语构建及一致性检查通过后发布。仅本地提交不会更新网站；推送到 main 或将 PR 合并到 main 才会触发发布，并且需要 GitHub Pages 已配置为 GitHub Actions。

To enable deployment:

1. Open `Settings -> Pages` in GitHub.
2. Under `Build and deployment`, set `Source` to `GitHub Actions`.
3. Ensure the default branch is `main`.
4. Push changes to `main` or rerun the `docs` workflow from the Actions tab.

## Repository Settings To Review

Before publishing externally, update the following values in `mkdocs.yml` if your repository location changes:

- `repo_url`
- `repo_name`
- `edit_uri`

## Content Guidelines

The starter content is intentionally early-stage and technical:

- it explains the safety boundary between the Exoskeleton Unit and Open Unit
- it leaves room for versioned APIs and SDK references later
- it provides realistic workflows for labs, developers, and partners without overclaiming product maturity

## Next Recommended Additions

- add real API reference material generated from source contracts
- add hardware setup photos and electrical interface tables
- add versioned release notes and compatibility matrices
- add downloadable example code packages or linked repositories
