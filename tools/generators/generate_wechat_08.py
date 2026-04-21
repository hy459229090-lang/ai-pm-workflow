#!/usr/bin/env python3
"""
生成第 08 篇微信公众号 HTML
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
md_file = ROOT / 'content/platforms/wechat/08-templates-full.md'

md_content = md_file.read_text(encoding='utf-8')
# Remove frontmatter
md_content = re.sub(r'^---\n[\s\S]*?---\n', '', md_content, count=1)

html = md_content

# 1. Extract code blocks first to protect them from other regex transforms
code_blocks = []
def extract_code(m):
    code = m.group(2).replace('<', '&lt;').replace('>', '&gt;')
    placeholder = f'__CODEBLOCK_{len(code_blocks)}__'
    code_blocks.append(f'<div style="background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 13px; overflow-x: auto; margin: 16px 0; color: #24292e; white-space: pre-wrap;">{code}</div>')
    return placeholder
html = re.sub(r'```(\w*)\n(.+?)\n```', extract_code, html, flags=re.DOTALL)

# 2. H1
html = re.sub(r'^# (.+)$', r'<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; margin-bottom: 12px; line-height: 1.4; text-align: center;">\1</h1>', html, flags=re.MULTILINE)
# 3. H2
html = re.sub(r'^## (.+)$', r'<h2 style="font-size: 17px; font-weight: 700; color: #1a1a1a; margin: 35px 0 16px 0; padding-left: 12px; border-left: 4px solid #07c160;">\1</h2>', html, flags=re.MULTILINE)
# 4. H3
html = re.sub(r'^### (.+)$', r'<h3 style="font-size: 15px; font-weight: 600; color: #333; margin: 24px 0 12px 0;">\1</h3>', html, flags=re.MULTILINE)

# 5. Bold & Italic
html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

# 6. Inline code
html = re.sub(r'`(.+?)`', r'<code style="background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-family: monospace; font-size: 14px;">\1</code>', html)

# 7. Blockquotes
html = re.sub(r'^> (.+)$', r'<div style="background: #f8f9fa; border-left: 4px solid #07c160; padding: 16px 20px; margin: 20px 0; border-radius: 0 4px 4px 0; color: #555; font-size: 15px;">\1</div>', html, flags=re.MULTILINE)

# 8. Unordered lists
html = re.sub(r'^- (.+)$', r'<p style="margin: 12px 0; padding-left: 20px; position: relative;"><span style="position: absolute; left: 0; color: #07c160;">●</span> \1</p>', html, flags=re.MULTILINE)

# 9. Numbered lists
html = re.sub(r'^(\d+)\. (.+)$', r'<p style="margin: 12px 0; padding-left: 24px;"><strong>\1.</strong> \2</p>', html, flags=re.MULTILINE)

# 10. Horizontal rules
html = re.sub(r'^---$', r'<hr style="border: none; height: 1px; background: #e9ecef; margin: 40px 0;">', html, flags=re.MULTILINE)

# 11. Tables
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

# 12. Paragraphs
lines = html.split('\n')
processed = []
for line in lines:
    s = line.strip()
    if s and not s.startswith('<') and not s.startswith('__CODEBLOCK_') and not any(s.endswith(t) for t in ['</h1>', '</h2>', '</h3>', '</strong>', '</em>', '</code>', '</table>', '</tr>', '</p>', '</div>', '</h1', '</h2', '</h3']):
        if len(s) > 2 and not s.startswith('<code'):
            line = f'<p style="margin: 16px 0; text-align: justify; font-size: 15px; line-height: 1.9;">{line}</p>'
    processed.append(line)
html = '\n'.join(processed)

# 13. Restore code blocks
for i, block in enumerate(code_blocks):
    html = html.replace(f'__CODEBLOCK_{i}__', block)

output = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>公众号文章 - 第08篇</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif; line-height: 1.9; color: #333; max-width: 677px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
.container {{ background: #fff; padding: 40px; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }}
.btn {{ position: fixed; bottom: 30px; right: 30px; background: #07c160; color: #fff; border: none; padding: 14px 28px; border-radius: 30px; font-size: 15px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 20px rgba(7, 193, 96, 0.4); }}
.btn:hover {{ background: #06ad56; }}
</style>
</head>
<body>
<div class="container" id="article">
{html}
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

output_file = ROOT / 'publish/wechat-html/wechat-08-full.html'
output_file.write_text(output, encoding='utf-8')
print(f"Done: {output_file}")
