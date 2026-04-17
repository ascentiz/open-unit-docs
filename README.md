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
│       └── docs-check.yml
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
├── .vercelignore
├── mkdocs.yml
├── requirements.txt
└── vercel.json
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

This repository is configured for **Vercel** deployment from a private GitHub repository.

### Recommended Private Deployment Model

Use Vercel Git integration for builds and keep GitHub Actions as a validation-only check.

This repository includes:

- `vercel.json` for static MkDocs builds on Vercel
- `.vercelignore` to avoid uploading local build and virtual environment files
- `.github/workflows/docs-check.yml` for strict documentation build checks on push and pull request

### Deploy To Vercel

1. Import `ascentiz/open-unit-docs` into Vercel.
2. Keep the repository private on GitHub.
3. Let Vercel build from the repository root using the included `vercel.json`.
4. In Vercel project settings, enable deployment protection appropriate to your plan.

### Access Control Notes

For team-only access, the most practical setup is Vercel Deployment Protection:

- `Vercel Authentication` is available on all plans
- on the Hobby plan, protection covers preview deployments and deployment URLs, but **not** the production domain
- to protect the production domain as well, use a plan that supports protection for **All Deployments**

If you need the final docs URL itself to remain private, plan for a paid Vercel tier or another access-control layer in front of the site.

### GitHub Actions Role

GitHub no longer handles site publishing in this repository. The GitHub workflow only verifies that:

- dependencies install correctly
- `mkdocs build --strict` succeeds
- pull requests do not break the documentation site

## Repository Settings To Review

Before publishing externally, update the following values in `mkdocs.yml` if your repository location changes:

- `repo_url`
- `repo_name`
- `edit_uri`

If you move to a different deployment target later, also review:

- `vercel.json`
- the GitHub workflow under `.github/workflows/docs-check.yml`

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
