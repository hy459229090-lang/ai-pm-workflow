#!/usr/bin/env python
"""
公众号头图生成脚本 - 使用 Pillow 本地生成
极简大字报风格封面图
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 配置
OUTPUT_PATH = "E:/PMbranding/assets/wechat/04-cover-yellow.png"
WIDTH, HEIGHT = 2350, 1000  # 2.35:1 比例
BG_COLOR = "#FFD700"  # 纯亮黄色背景

def create_cover():
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 尝试加载字体（使用系统字体）
    # 中文需要支持中文的字体
    font_paths = [
        "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",    # 黑体
        "C:/Windows/Fonts/simsun.ttc",    # 宋体
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/chinese/simsun.ttf",
    ]

    title_font = None

    # 使用超大字号让文字占画面 60%
    title_font_size = 180

    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                title_font = ImageFont.truetype(font_path, title_font_size)
                print(f"使用字体：{font_path}")
                break
            except:
                continue

    if not title_font:
        print("警告：未找到中文字体，使用默认字体")
        title_font = ImageFont.load_default()

    # 绘制标题文字（中央）- 黑色超粗体，分两行
    line1 = "我让 AI 跑了 7 天数据"
    line2 = "老板问我是不是换了人"

    text_color = "#000000"  # 纯黑色

    # 计算文字居中位置
    bbox1 = title_font.getbbox(line1)
    bbox2 = title_font.getbbox(line2)
    text_width1 = bbox1[2] - bbox1[0]
    text_width2 = bbox2[2] - bbox2[0]
    text_height = bbox1[3] - bbox1[1]

    line_spacing = 40  # 行间距

    total_height = text_height * 2 + line_spacing
    start_y = (HEIGHT - total_height) // 2

    x1 = (WIDTH - text_width1) // 2
    x2 = (WIDTH - text_width2) // 2

    # 绘制第一行
    draw.text((x1, start_y), line1, font=title_font, fill=text_color)
    # 绘制第二行
    draw.text((x2, start_y + text_height + line_spacing), line2, font=title_font, fill=text_color)

    # 极简风格，无其他装饰元素

    # 保存图片
    img.save(OUTPUT_PATH, "PNG")
    print(f"图片已保存到：{OUTPUT_PATH}")
    print(f"尺寸：{WIDTH}x{HEIGHT}")
    return True

if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    print("开始生成公众号头图...")
    create_cover()
