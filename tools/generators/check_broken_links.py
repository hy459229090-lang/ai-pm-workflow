#!/usr/bin/env python3
"""
检查所有 .md 文件中的 Obsidian wikilink 是否有效。

扫描所有 markdown 文件，提取 [[path/to/file|label]] 格式的链接，
检查每个链接的目标文件是否存在。

用法: python tools/generators/check_broken_links.py
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent  # E:/PMbranding

# Wikilink pattern: [[path]] or [[path|label]]
WIKILINK_RE = re.compile(r'\[\[([^\]\|]+)\|?[^\]]*\]\]')

# Files/dirs to skip
SKIP_DIRS = {'node_modules', '.git', '.obsidian', 'archive'}
SKIP_FILES = set()

def find_md_files():
    """Find all markdown files in the project."""
    md_files = []
    for root, dirs, files in os.walk(ROOT):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith('.md'):
                md_files.append(Path(root) / f)
    return md_files

def resolve_link(link_path: str, source_file: Path) -> Path | None:
    """
    Resolve a wikilink to an actual file path.
    Supports:
    - Absolute paths from repo root: [[content/sources/00-philosophy]]
    - Relative paths: [[00-philosophy]] (same directory)
    - With or without .md extension
    """
    # Remove leading ./
    link_path = link_path.lstrip('./')
    # Remove trailing backslash (from escaped pipe \|)
    link_path = link_path.rstrip('\\').strip()

    # Try as absolute path from repo root
    candidates = []

    # Try with .md extension
    candidates.append(ROOT / link_path)
    candidates.append(ROOT / f"{link_path}.md")

    # Try relative to source file's directory
    source_dir = source_file.parent
    candidates.append(source_dir / link_path)
    candidates.append(source_dir / f"{link_path}.md")

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None

def extract_wikilinks(content: str) -> list[str]:
    """
    Extract wikilinks from markdown content, skipping code blocks and inline code.
    """
    # Remove fenced code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    # Remove inline code
    content = re.sub(r'`[^`]+`', '', content)
    return WIKILINK_RE.findall(content)

def check_broken_links():
    """Scan all files and report broken links."""
    broken_links = []
    total_links = 0
    total_files = 0

    md_files = find_md_files()
    print(f"Found {len(md_files)} markdown files.\n")

    for md_file in sorted(md_files):
        total_files += 1
        content = md_file.read_text(encoding='utf-8')
        links = extract_wikilinks(content)

        for link in links:
            total_links += 1
            target = resolve_link(link, md_file)
            if target is None:
                # Calculate relative path for display
                rel_path = md_file.relative_to(ROOT)
                broken_links.append((rel_path, link))

    # Report
    if broken_links:
        print(f"Found {len(broken_links)} broken links:\n")
        for file_path, link in broken_links:
            print(f"  {file_path}: [[{link}]]")
        print(f"\nTotal: {total_links} links checked, {len(broken_links)} broken.")
        return 1
    else:
        print(f"All {total_links} wikilinks are valid across {total_files} files.")
        return 0

if __name__ == '__main__':
    sys.exit(check_broken_links())
