#!/usr/bin/env python3
"""Validate the source-based BodyOS SDK documentation build."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

NAV_SOURCES = (
    "index.md",
    "product/overview.md",
    "product/exo-belt.md",
    "product/b-core-pi-1.md",
    "installation/index.md",
    "api/README.md",
    "api/C++_API_Reference.md",
    "api/Python_API_Reference.md",
    "api/integration-libraries.md",
    "api/Examples_Guide.md",
)

LOCALES = ("zh", "en")


def localized_source(source: str, locale: str) -> str:
    return str(Path(source).with_suffix(f".{locale}.md"))


def localized_output(source: str, locale: str) -> str:
    path = Path(source)
    if path.name.lower() == "readme.md":
        output = path.parent / "index.html"
    elif path.name == "index.md":
        output = path.parent / "index.html"
    else:
        output = path.with_suffix("") / "index.html"
    return str(Path("en") / output) if locale == "en" else str(output)


PUBLISHED_SOURCES = tuple(
    localized_source(source, locale)
    for locale in LOCALES
    for source in NAV_SOURCES
)

PUBLISHED_OUTPUTS = {
    localized_source(source, locale): localized_output(source, locale)
    for locale in LOCALES
    for source in NAV_SOURCES
}

PUBLISHED_SEARCH_LOCATIONS = {
    source: quote(output.removesuffix("index.html"), safe="/")
    for source, output in PUBLISHED_OUTPUTS.items()
}

LEGACY_PREFIXES = (
    "architecture/",
    "community/",
    "examples/",
    "getting-started/",
    "hardware/",
    "integrations/",
    "mechanical/",
    "research/",
    "sdk/",
    "troubleshooting/",
    "tutorials/",
)

LEGACY_API_LOCATIONS = {
    "api/index/",
    "api/control-api/",
    "api/telemetry-api/",
}

LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
ID_RE = re.compile(r"\bid=[\"']([^\"']+)[\"']", re.IGNORECASE)
H1_RE = re.compile(r"<h1(?:\s[^>]*)?>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def flatten_nav(node: object) -> list[str]:
    paths: list[str] = []
    if isinstance(node, str):
        paths.append(node)
    elif isinstance(node, list):
        for item in node:
            paths.extend(flatten_nav(item))
    elif isinstance(node, dict):
        for value in node.values():
            paths.extend(flatten_nav(value))
    return paths


def source_h1(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def normalize_h1(value: str | None) -> str | None:
    if value is None:
        return None
    return value.replace("`", "").removesuffix("¶").strip()


def output_for_url(page: Path, url_path: str) -> Path:
    if url_path.startswith("/"):
        normalized = url_path.lstrip("/")
        prefix = "open-unit-docs/"
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix) :]
        target = SITE / normalized
    else:
        target = (page.parent / unquote(url_path)).resolve()

    if target.suffix:
        return target
    return target / "index.html"


def main() -> int:
    failures: list[str] = []

    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    nav_paths = flatten_nav(config.get("nav", []))
    if nav_paths != list(NAV_SOURCES):
        fail(
            "mkdocs.yml 的导航必须严格等于：" + ", ".join(NAV_SOURCES),
            failures,
        )

    if config.get("theme", {}).get("language") != "zh":
        fail("MkDocs 主题语言必须为 zh。", failures)

    i18n_config = next(
        (
            plugin["i18n"]
            for plugin in config.get("plugins", [])
            if isinstance(plugin, dict) and "i18n" in plugin
        ),
        None,
    )
    if i18n_config is None or i18n_config.get("docs_structure") != "suffix":
        fail("必须启用 suffix 结构的 i18n 插件。", failures)
    else:
        languages = {
            language.get("locale"): language
            for language in i18n_config.get("languages", [])
        }
        zh = languages.get("zh", {})
        en = languages.get("en", {})
        if not (zh.get("default") is True and zh.get("build") is True):
            fail("中文 zh 必须是当前默认构建语言。", failures)
        if zh.get("name") != "中":
            fail("中文语言切换名称必须为 中。", failures)
        if not (en.get("build") is True and en.get("name") == "EN"):
            fail("英文 en 必须启用构建，且语言切换名称为 EN。", failures)

    for relative in PUBLISHED_SOURCES:
        source = DOCS / relative
        if not source.is_file():
            fail(f"缺少正式源文件：docs/{relative}", failures)
            continue

        output = SITE / PUBLISHED_OUTPUTS[relative]
        if not output.is_file():
            fail(f"缺少构建页面：site/{PUBLISHED_OUTPUTS[relative]}", failures)
            continue

        content = output.read_text(encoding="utf-8")
        locale = "en" if relative.endswith(".en.md") else "zh"
        language_pattern = rf"<html[^>]+lang=[\"']{locale}[\"']"
        if not re.search(language_pattern, content, re.IGNORECASE):
            fail(f"页面语言不是 {locale}：{output.relative_to(ROOT)}", failures)

        expected_h1 = source_h1(source)
        match = H1_RE.search(content)
        actual_h1 = html.unescape(TAG_RE.sub("", match.group(1))).strip() if match else None
        if normalize_h1(expected_h1) != normalize_h1(actual_h1):
            fail(
                f"H1 不匹配：{relative}（源文件={expected_h1!r}，页面={actual_h1!r}）",
                failures,
            )

    for output_rel in PUBLISHED_OUTPUTS.values():
        page = SITE / output_rel
        if not page.is_file():
            continue
        content = page.read_text(encoding="utf-8")
        anchors = {html.unescape(value) for value in ID_RE.findall(content)}

        for raw_link in LINK_RE.findall(content):
            link = html.unescape(raw_link)
            parsed = urlsplit(link)
            if parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}:
                continue
            if link.startswith("//"):
                continue

            if not parsed.path:
                target = page
            else:
                target = output_for_url(page, parsed.path)

            if not target.exists():
                fail(
                    f"无效站内链接：{page.relative_to(ROOT)} -> {link}",
                    failures,
                )
                continue

            if parsed.fragment and target.suffix == ".html":
                target_content = target.read_text(encoding="utf-8")
                target_anchors = {
                    html.unescape(value) for value in ID_RE.findall(target_content)
                }
                fragment = unquote(parsed.fragment)
                if fragment not in target_anchors:
                    fail(
                        f"无效页面锚点：{page.relative_to(ROOT)} -> {link}",
                        failures,
                    )

    search_file = SITE / "search" / "search_index.json"
    if not search_file.is_file():
        fail("缺少搜索索引：site/search/search_index.json", failures)
    else:
        search_data = json.loads(search_file.read_text(encoding="utf-8"))
        locations = {
            str(item.get("location", "")).lstrip("/")
            for item in search_data.get("docs", [])
        }
        for source, expected in PUBLISHED_SEARCH_LOCATIONS.items():
            if expected not in locations:
                fail(f"搜索索引缺少正式页面：{expected or '/'}", failures)

        for location in sorted(locations):
            if location in LEGACY_API_LOCATIONS or location.startswith(LEGACY_PREFIXES):
                fail(f"搜索索引包含旧页面：{location}", failures)

    required_markers = {
        "product/overview.zh.md": "Exoskeleton Unit（封装）",
        "product/exo-belt.zh.md": "本页为框架页",
        "product/b-core-pi-1.zh.md": "BodyOS SDK / 公开 API",
        "api/README.zh.md": "BodyOS SDK 开发者手册",
        "api/C++_API_Reference.zh.md": "BodyClient",
        "api/Python_API_Reference.zh.md": "BodyClient",
        "api/integration-libraries.zh.md": "未列入正式支持清单",
        "api/Examples_Guide.zh.md": "sensor_read_record",
        "product/overview.en.md": "encapsulated",
        "product/exo-belt.en.md": "framework page",
        "product/b-core-pi-1.en.md": "BodyOS SDK / Public API",
        "installation/index.zh.md": "SHA-256",
        "installation/index.en.md": "SHA-256",
        "api/README.en.md": "BodyOS SDK Developer Guide",
        "api/C++_API_Reference.en.md": "BodyClient",
        "api/Python_API_Reference.en.md": "BodyClient",
        "api/integration-libraries.en.md": "formal support list",
        "api/Examples_Guide.en.md": "sensor_read_record",
    }
    for source, marker in required_markers.items():
        if marker not in (DOCS / source).read_text(encoding="utf-8"):
            fail(f"正式原稿缺少预期标识：{source} -> {marker}", failures)

    if failures:
        print("Documentation checks failed:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Documentation checks passed: 20 bilingual pages, links, anchors, and search scope are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
