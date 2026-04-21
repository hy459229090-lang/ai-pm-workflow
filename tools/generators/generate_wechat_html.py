#!/usr/bin/env python3
"""
公众号文章 HTML 生成器（统一版）
支持生成任意篇号的微信公众号 HTML

用法: python tools/generators/generate_wechat_html.py <篇号>
示例: python tools/generators/generate_wechat_html.py 05
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

# Article config: (source_md_path, output_html_path, title)
ARTICLE_CONFIG = {
    '04': ('content/platforms/wechat/04-data-agent-full.md', 'publish/wechat-html/wechat-04-full.html', '让 AI 当你的数据分析师'),
    '05': ('content/platforms/wechat/05-agent-team-full.md', 'publish/wechat-html/wechat-05-full.html', 'Agent Team — 当一个人搞不定的时候'),
    '06': ('content/platforms/wechat/06-evaluate-full.md', 'publish/wechat-html/wechat-06-full.html', 'AI 产出评估 — 什么时候该打回重做'),
    '07': ('content/platforms/wechat/07-review-full.md', 'publish/wechat-html/wechat-07-full.html', 'AI 产出不失控 — Review 机制'),
    '08': ('content/platforms/wechat/08-templates-full.md', 'publish/wechat-html/wechat-08-full.html', '模板与规范 — 让产出一致'),
}


def md_to_wechat_html(md_content: str) -> str:
    """Convert Markdown to WeChat-compatible HTML.

    Key: extract code blocks first to prevent regex transforms from corrupting them.
    """
    html = md_content

    # 1. Extract code blocks to protect from other transforms
    code_blocks = []
    def extract_code(m):
        code = m.group(2).replace('<', '&lt;').replace('>', '&gt;')
        placeholder = f'__CODEBLOCK_{len(code_blocks)}__'
        code_blocks.append(
            f'<div style="background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; '
            f'padding: 16px; font-family: monospace; font-size: 13px; overflow-x: auto; '
            f'margin: 16px 0; color: #24292e; white-space: pre-wrap;">{code}</div>'
        )
        return placeholder
    html = re.sub(r'```(\w*)\n(.+?)\n```', extract_code, html, flags=re.DOTALL)

    # 2. Headings
    html = re.sub(r'^# (.+)$', r'<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; margin-bottom: 12px; line-height: 1.4; text-align: center;">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2 style="font-size: 17px; font-weight: 700; color: #1a1a1a; margin: 35px 0 16px 0; padding-left: 12px; border-left: 4px solid #07c160;">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3 style="font-size: 15px; font-weight: 600; color: #333; margin: 24px 0 12px 0;">\1</h3>', html, flags=re.MULTILINE)

    # 3. Bold & Italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # 4. Inline code
    html = re.sub(r'`(.+?)`', r'<code style="background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-family: monospace; font-size: 14px;">\1</code>', html)

    # 5. Blockquotes
    html = re.sub(r'^> (.+)$', r'<div style="background: #f8f9fa; border-left: 4px solid #07c160; padding: 16px 20px; margin: 20px 0; border-radius: 0 4px 4px 0; color: #555; font-size: 15px;">\1</div>', html, flags=re.MULTILINE)

    # 6. Unordered lists
    html = re.sub(r'^- (.+)$', r'<p style="margin: 12px 0; padding-left: 20px; position: relative;"><span style="position: absolute; left: 0; color: #07c160;">●</span> \1</p>', html, flags=re.MULTILINE)

    # 7. Numbered lists
    html = re.sub(r'^(\d+)\. (.+)$', r'<p style="margin: 12px 0; padding-left: 24px;"><strong>\1.</strong> \2</p>', html, flags=re.MULTILINE)

    # 8. Horizontal rules
    html = re.sub(r'^---$', r'<hr style="border: none; height: 1px; background: #e9ecef; margin: 40px 0;">', html, flags=re.MULTILINE)

    # 9. Tables
    def table_repl(m):
        rows = [r.strip() for r in m.group(0).split('\n') if r.strip()]
        result = '<table style="width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px;">'
        for i, row in enumerate(rows):
            if re.match(r'^[\|\-\s:]+$', row):
                continue
            cells = [c.strip() for c in row.split('|') if c.strip()]
            if not cells:
                continue
            tag = 'th' if i == 0 else 'td'
            bg = 'background: #f6f8fa; font-weight: 600;' if i == 0 else ''
            result += '<tr>'
            for cell in cells:
                result += f'<{tag} style="{bg} padding: 10px 12px; border: 1px solid #e1e4e8; text-align: left;">{cell}</{tag}>'
            result += '</tr>'
        result += '</table>'
        return result
    html = re.sub(r'(\|.*\|(?:\n\|.*\|)+)', table_repl, html)

    # 10. Paragraphs (skip code block placeholders)
    lines = html.split('\n')
    processed = []
    for line in lines:
        s = line.strip()
        if (s and not s.startswith('<') and not s.startswith('__CODEBLOCK_')
                and not any(s.endswith(t) for t in ['</h1>', '</h2>', '</h3>', '</strong>', '</em>', '</code>', '</table>', '</tr>', '</p>', '</div>'])
                and len(s) > 2):
            line = f'<p style="margin: 16px 0; text-align: justify; font-size: 15px; line-height: 1.9;">{line}</p>'
        processed.append(line)
    html = '\n'.join(processed)

    # 11. Restore code blocks
    for i, block in enumerate(code_blocks):
        html = html.replace(f'__CODEBLOCK_{i}__', block)

    return html


def generate_full_html(article_content: str, title: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; line-height: 1.9; color: #333; max-width: 677px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
.container {{ background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }}
.btn {{ position: fixed; bottom: 30px; right: 30px; background: #07c160; color: #fff; border: none; padding: 14px 28px; border-radius: 30px; font-size: 15px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 20px rgba(7, 193, 96, 0.4); }}
.btn:hover {{ background: #06ad56; }}
</style>
</head>
<body>
<div class="container" id="article">
{article_content}
</div>

<button class="btn" onclick="copyHTML()">复制 HTML 代码</button>

<script>
function copyHTML() {{
    const content = document.getElementById('article').innerHTML;
    navigator.clipboard.writeText(content).then(() => {{
        alert('HTML 已复制到剪贴板！\\n\\n在公众号后台：\\n1. 切换到"源代码模式"\\n2. 粘贴 HTML 代码\\n3. 切换回编辑模式即可预览');
    }}).catch(err => {{
        const textarea = document.createElement('textarea');
        textarea.value = content;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        alert('HTML 已复制到剪贴板！');
    }});
}}
</script>
</body>
</html>'''


def main():
    if len(sys.argv) > 1:
        article_num = sys.argv[1]
    else:
        # Default: generate all
        for num in ARTICLE_CONFIG:
            generate_article(num)
        return

    generate_article(article_num)


def generate_article(article_num: str):
    config = ARTICLE_CONFIG.get(article_num)
    if not config:
        print(f"未找到篇号 {article_num} 的配置，可选: {', '.join(ARTICLE_CONFIG.keys())}")
        return

    md_path, output_path, title = config
    md_file = ROOT / md_path
    if not md_file.exists():
        print(f"文件不存在：{md_file}")
        return

    md_content = md_file.read_text(encoding='utf-8')
    # Remove frontmatter
    md_content = re.sub(r'^---\n[\s\S]*?---\n', '', md_content, count=1)

    html_content = md_to_wechat_html(md_content)
    full_html = generate_full_html(html_content, title)

    output_file = ROOT / output_path
    output_file.write_text(full_html, encoding='utf-8')
    print(f"篇号 {article_num}: {output_file}")


if __name__ == '__main__':
    main()
