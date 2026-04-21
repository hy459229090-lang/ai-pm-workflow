#!/usr/bin/env python3
"""
扫描所有 .md 文件，找出孤立节点和链接异常的节点。

孤立节点：没有任何入链或出链的文件。
低链接节点：入链或出链数异常少的文件（< 2）。

用法: python tools/generators/check_orphan_nodes.py
"""

import os
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent  # E:/PMbranding

# Wikilink pattern: [[path|label]] or [[path]]
WIKILINK_RE = re.compile(r'\[\[([^\]\|]+)\|?[^\]]*\]\]')

# Files/dirs to skip
SKIP_DIRS = {'node_modules', '.git', '.obsidian', 'archive'}

# Files to ignore (not content nodes)
SKIP_FILES = {
    'LICENSE.md',
}

def find_md_files():
    """Find all markdown files in the project."""
    md_files = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith('.md') and f not in SKIP_FILES:
                md_files.append(Path(root) / f)
    return md_files

def extract_wikilinks(content: str) -> list[str]:
    """Extract wikilinks from markdown content, skipping code blocks and inline code."""
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    return WIKILINK_RE.findall(content)

def resolve_link(link_path: str) -> Path | None:
    """Resolve a wikilink to an actual file path."""
    link_path = link_path.lstrip('./').rstrip('\\').strip()

    candidates = [
        ROOT / link_path,
        ROOT / f"{link_path}.md",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None

def normalize_path(p: Path) -> str:
    """Get a human-readable relative path from repo root."""
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)

def check_orphan_nodes():
    """Scan all files and report orphan nodes and low-link nodes."""
    md_files = find_md_files()
    file_map = {}  # normalized_path -> Path
    out_links = defaultdict(set)  # file -> set of targets
    in_links = defaultdict(set)   # file -> set of sources

    # Build file map
    for f in md_files:
        file_map[normalize_path(f)] = f

    # Scan links
    for f in md_files:
        content = f.read_text(encoding='utf-8')
        links = extract_wikilinks(content)
        norm = normalize_path(f)

        for link in links:
            target = resolve_link(link)
            if target:
                target_norm = normalize_path(target)
                out_links[norm].add(target_norm)
                in_links[target_norm].add(norm)

    # Find orphan nodes (no in-links and no out-links)
    orphans = []
    low_link = []

    all_files = set(file_map.keys())

    for f in sorted(all_files):
        has_out = len(out_links.get(f, set())) > 0
        has_in = len(in_links.get(f, set())) > 0

        if not has_in and not has_out:
            orphans.append(f)
        elif (has_in and len(in_links[f]) < 2) or (has_out and len(out_links[f]) < 2):
            low_link.append(f)

    # Report
    print(f"Found {len(md_files)} markdown files.\n")

    if orphans:
        print(f"=== {len(orphans)} Orphan Nodes (no links at all) ===\n")
        for f in orphans:
            print(f"  {f}")
    else:
        print("No orphan nodes found.")

    print()

    if low_link:
        print(f"=== {len(low_link)} Low-Link Nodes (< 2 in/out links) ===\n")
        for f in sorted(low_link):
            in_count = len(in_links.get(f, set()))
            out_count = len(out_links.get(f, set()))
            print(f"  {f}  (in: {in_count}, out: {out_count})")
    else:
        print("No low-link nodes found.")

    # Summary
    print(f"\n=== Summary ===")
    print(f"Total files: {len(md_files)}")
    print(f"Orphan nodes: {len(orphans)}")
    print(f"Low-link nodes: {len(low_link)}")
    print(f"Well-connected: {len(all_files) - len(orphans) - len(low_link)}")

    return 0 if not orphans else 1

if __name__ == '__main__':
    check_orphan_nodes()
