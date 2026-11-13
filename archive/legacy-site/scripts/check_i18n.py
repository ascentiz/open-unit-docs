#!/usr/bin/env python3
"""Check translation coverage and a freshly built bilingual MkDocs site."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
FENCES = re.compile(r"^```[^\n]*\n.*?^```", re.MULTILINE | re.DOTALL)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.lang = None
        self.references = []
        self.alternates = {}
        self.edit_links = []
        self.ids = set()
        self.h1 = ""
        self.in_h1 = False
        self.language_button = ""
        self.in_language_button = False
        self.language_button_label = None
        self.language_menu = {}
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.in_h1 = True
        if tag == "button" and "md-language-toggle" in attrs.get("class", "").split():
            self.in_language_button = True
            self.language_button_label = attrs.get("aria-label")
        if tag == "a" and "md-select__link" in attrs.get("class", "").split():
            self.language_menu[attrs.get("hreflang")] = attrs.get("href", "")
        if tag == "link" and attrs.get("rel") == "alternate":
            self.alternates[attrs.get("hreflang")] = attrs.get("href")
        if tag == "a" and "content.action.edit" in attrs.get("title", ""):
            self.edit_links.append(attrs.get("href", ""))
        if tag == "a" and "/edit/main/docs/" in attrs.get("href", ""):
            self.edit_links.append(attrs["href"])
        for attribute in ("href", "src"):
            if attribute in attrs:
                self.references.append(attrs[attribute])

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False
        if tag == "button":
            self.in_language_button = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1 += data
        if self.in_language_button:
            self.language_button += data


def page_path(source):
    relative = source.relative_to(DOCS)
    if relative.name == "index.md":
        return relative.with_suffix(".html")
    return relative.with_suffix("") / "index.html"


def page_url(base_url, relative):
    return urljoin(base_url, relative.as_posix().removesuffix("index.html"))


def main():
    errors = []
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    base_url = config["site_url"]
    base = urlsplit(base_url)
    english = sorted(path for path in DOCS.rglob("*.md") if not path.name.endswith(".zh.md"))
    expected_chinese = {path.with_suffix(".zh.md") for path in english}
    actual_chinese = set(DOCS.rglob("*.zh.md"))
    for missing in sorted(expected_chinese - actual_chinese):
        errors.append(f"Missing translation: {missing.relative_to(ROOT)}")
    for orphan in sorted(actual_chinese - expected_chinese):
        errors.append(f"Translation has no English source: {orphan.relative_to(ROOT)}")

    if not (SITE / "index.html").exists():
        errors.append("No built site. Run mkdocs build --strict first.")

    pages = {}
    for source in english:
        translated = source.with_suffix(".zh.md")
        if not translated.exists():
            continue
        en_text = source.read_text(encoding="utf-8")
        zh_text = translated.read_text(encoding="utf-8")
        if FENCES.findall(en_text) != FENCES.findall(zh_text):
            errors.append(f"Code samples differ: {source.relative_to(DOCS)}")
        if not re.search(r"[\u4e00-\u9fff]", zh_text):
            errors.append(f"Translation has no Chinese text: {translated.relative_to(DOCS)}")
        relative = page_path(source)
        expected_urls = {"en": page_url(base_url, relative), "zh": page_url(base_url, Path("zh") / relative)}
        for lang, text, actual_source in (("en", en_text, source), ("zh", zh_text, translated)):
            output = relative if lang == "en" else Path("zh") / relative
            artifact = SITE / output
            if not artifact.exists():
                errors.append(f"Missing built page: {output}")
                continue
            page = Page(artifact.read_text(encoding="utf-8"))
            pages[artifact] = page
            if page.lang != lang:
                errors.append(f"Wrong HTML language in {output}: {page.lang}")
            if page.language_button.strip() != "中/EN" or not page.language_button_label:
                errors.append(f"Wrong or inaccessible language switch in {output}")
            heading = re.search(r"^# (.+)$", text, re.MULTILINE).group(1).strip()
            if not page.h1.strip().startswith(heading):
                errors.append(f"Wrong heading (possible fallback) in {output}: {page.h1}")
            for alternate_lang, expected_url in expected_urls.items():
                alternate = page.alternates.get(alternate_lang, "")
                if not alternate or urljoin(expected_urls[lang], alternate) != expected_url:
                    errors.append(f"Wrong {alternate_lang} alternate in {output}: {page.alternates.get(alternate_lang)}")
                menu_link = page.language_menu.get(alternate_lang, "")
                if not menu_link or urljoin(expected_urls[lang], menu_link) != expected_url:
                    errors.append(f"Wrong {alternate_lang} language-menu link in {output}: {menu_link}")
            expected_edit = config["repo_url"] + "/edit/main/docs/" + actual_source.relative_to(DOCS).as_posix()
            if expected_edit not in page.edit_links:
                errors.append(f"Wrong edit link in {output}: {page.edit_links}")

    # Check internal resources and links against actual build output, including anchors.
    for artifact, page in list(pages.items()):
        current_url = page_url(base_url, artifact.relative_to(SITE))
        for reference in page.references:
            resolved = urlsplit(urljoin(current_url, reference))
            if resolved.scheme not in ("http", "https") or resolved.netloc != base.netloc:
                continue
            if not resolved.path.startswith(base.path):
                errors.append(f"Link escapes GitHub Pages base path in {artifact.relative_to(SITE)}: {reference}")
                continue
            relative = unquote(resolved.path[len(base.path):])
            target = SITE / relative
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"Broken link/resource in {artifact.relative_to(SITE)}: {reference}")
            elif resolved.fragment and target.suffix == ".html":
                if target not in pages:
                    pages[target] = Page(target.read_text(encoding="utf-8"))
                if unquote(resolved.fragment) not in pages[target].ids:
                    errors.append(f"Broken anchor in {artifact.relative_to(SITE)}: {reference}")

    index_file = SITE / "search" / "search_index.json"
    if not index_file.exists():
        errors.append("Missing search index.")
    else:
        search = json.loads(index_file.read_text(encoding="utf-8"))
        indexed_locations = {item["location"].split("#")[0] for item in search["docs"]}
        for source in english:
            relative = page_path(source)
            for prefix in (Path(), Path("zh")):
                location = (prefix / relative).as_posix().removesuffix("index.html")
                if location not in indexed_locations:
                    errors.append(f"Page missing from search index: {location or '/'}")
        if not any("遥测" in item.get("text", "") for item in search["docs"]):
            errors.append("Chinese keyword 遥测 missing from search content.")

    if errors:
        for error in sorted(set(errors)):
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(english)} English + {len(actual_chinese)} Chinese pages; code samples, languages, alternate/edit links, resources, anchors and search index.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
