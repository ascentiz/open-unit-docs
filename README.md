# Ascentiz Open Unit Documentation

This repository contains the MkDocs-based documentation site for **Ascentiz Open Unit**, the developer-facing compute and control layer in the Ascentiz modular exoskeleton platform.

The docs are structured for:

- robotics developers building applications on top of Open Unit
- researchers evaluating control, sensing, and telemetry workflows
- university labs collaborating on experimental protocols and integration work
- ecosystem partners integrating hardware, software, and data services

## Stack

- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

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
│   ├── research/
│   ├── tutorials/
│   └── index.md
├── .gitignore
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

4. Open `http://127.0.0.1:8000` in your browser.

## Build

Run a strict production build locally before opening a pull request:

```bash
mkdocs build --strict
```

The generated site will be written to `site/`.

## Deployment

This repository includes a GitHub Actions workflow for GitHub Pages deployment at `.github/workflows/docs.yml`.

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
