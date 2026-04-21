#!/usr/bin/env python3
"""
公众号文章 HTML 生成器 - 第 06 篇
"""

import re
from pathlib import Path

def md_to_wechat_html(md_content: str) -> str:
    """将 Markdown 内容转换为公众号 HTML"""

    html = md_content

    # 标题
    html = re.sub(r'^# (.+)$', r'<h1 style="font-size: 22px; font-weight: 700; color: #1a1a1a; margin-bottom: 12px; line-height: 1.4; text-align: center;">\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2 style="font-size: 17px; font-weight: 700; color: #1a1a1a; margin: 35px 0 16px 0; padding-left: 12px; border-left: 4px solid #07c160;">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3 style="font-size: 15px; font-weight: 600; color: #333; margin: 24px 0 12px 0;">\1</h3>', html, flags=re.MULTILINE)

    # 强调
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # 代码块
    html = re.sub(r'```(\w*)\n(.+?)\n```', r'<div style="background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; padding: 16px; font-family: monospace; font-size: 13px; overflow-x: auto; margin: 16px 0; color: #24292e; white-space: pre-wrap;">\2</div>', html, flags=re.DOTALL)

    # 行内代码
    html = re.sub(r'`(.+?)`', r'<code style="background: #f6f8fa; padding: 2px 6px; border-radius: 3px; font-family: monospace; font-size: 14px;">\1</code>', html)

    # 引用块
    html = re.sub(r'^> (.+)$', r'<div style="background: #f8f9fa; border-left: 4px solid #07c160; padding: 16px 20px; margin: 20px 0; border-radius: 0 4px 4px 0; color: #555; font-size: 15px;">\1</div>', html, flags=re.MULTILINE)

    # 列表
    html = re.sub(r'^- (.+)$', r'<p style="margin: 12px 0; padding-left: 20px; position: relative;"><span style="position: absolute; left: 0; color: #07c160;">●</span> \1</p>', html, flags=re.MULTILINE)

    # 分割线
    html = re.sub(r'^---$', r'<hr style="border: none; height: 1px; background: #e9ecef; margin: 40px 0;">', html, flags=re.MULTILINE)

    return html


def generate_full_html(article_content: str, title: str = "") -> str:
    """生成完整的 HTML 文档"""

    base_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>公众号文章生成器</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            line-height: 1.9;
            color: #333;
            max-width: 677px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }}
        .btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #07c160;
            color: #fff;
            border: none;
            padding: 14px 28px;
            border-radius: 30px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(7, 193, 96, 0.4);
        }}
        .btn:hover {{
            background: #06ad56;
        }}
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

    return base_html


def main():
    md_file = Path('publish/wechat/06-evaluate-full.md')
    if not md_file.exists():
        print(f"文件不存在：{md_file}")
        return

    md_content = md_file.read_text(encoding='utf-8')
    html_content = md_to_wechat_html(md_content)
    full_html = generate_full_html(html_content)

    output_file = Path('tools/wechat-06-full.html')
    output_file.write_text(full_html, encoding='utf-8')

    print(f"生成完成：{output_file}")
    print("在浏览器中打开该文件，点击'复制 HTML 代码'按钮即可")


if __name__ == '__main__':
    main()
