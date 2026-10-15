#!/usr/bin/env python3
"""Dependency-free packaging/link checks; not a medical-safety validator."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills" if (ROOT / "skills").is_dir() else ROOT
NAMES = {"cc-assess", "cc-treat", "cc-navigate", "cc-monitor", "cc-strategist"}
errors = []
links_checked = 0


def check_local(source, target, base=None, anchors=None):
    global links_checked
    url = urlsplit(target)
    if url.scheme or url.netloc:
        return
    links_checked += 1
    base = base or source.parent
    path = (base / unquote(url.path).lstrip("/")).resolve() if url.path else source
    if not path.is_relative_to(ROOT) or not path.exists():
        errors.append("%s: missing/escaping target %s" % (source.relative_to(ROOT), target))
    if anchors is not None and not url.path and url.fragment and url.fragment not in anchors:
        errors.append("%s: missing anchor %s" % (source.relative_to(ROOT), target))


for name in sorted(NAMES):
    skill = SKILLS / name / "SKILL.md"
    if not skill.is_file():
        errors.append("Missing %s" % skill)
        continue
    content = skill.read_text()
    front = content.split("---", 2)
    if len(front) != 3 or front[0].strip():
        errors.append("%s: invalid frontmatter" % name)
    else:
        fields = dict(re.findall(r"^([a-z_]+): (.+)$", front[1], re.M))
        if fields.get("name") != name or not fields.get("description"):
            errors.append("%s: missing/mismatched skill metadata" % name)
    if not (skill.parent / "references").is_dir():
        errors.append("%s: missing reference directory" % name)

markdown = [ROOT / "README.md"] + sorted(SKILLS.glob("cc-*/**/*.md"))
for source in markdown:
    if not source.is_file():
        errors.append("Missing %s" % source)
        continue
    content = source.read_text()
    if len(re.findall(r"^```", content, re.M)) % 2:
        errors.append("%s: unclosed Markdown fence" % source.relative_to(ROOT))
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content):
        check_local(source, target)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.assets = []
        self.json_ld = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag in {"a", "link"} and attrs.get("href"):
            self.links.append(attrs["href"])
        if attrs.get("src"):
            self.assets.append(attrs["src"])
        if tag == "script":
            self.json_ld = attrs.get("type") == "application/ld+json"

    def handle_data(self, data):
        if self.json_ld:
            try:
                json.loads(data)
            except ValueError as exc:
                errors.append("Invalid JSON-LD: %s" % exc)

    def handle_endtag(self, tag):
        if tag == "script":
            self.json_ld = False


site = ROOT / "site"
if site.is_dir():
    source = site / "index.html"
    page = Page()
    page.feed(source.read_text())
    if len(set(page.ids)) != len(page.ids):
        errors.append("Duplicate landing-page IDs")
    for target in page.links + page.assets:
        check_local(source, target, site, set(page.ids))
    for source in site.glob("*.webmanifest"):
        json.loads(source.read_text())

if errors:
    raise SystemExit("\n".join(errors))
print("PASS: 5 packaged skills, %d Markdown files, %d local links/assets%s" % (
    len(markdown), links_checked, ", landing metadata/anchors" if site.is_dir() else ""))
