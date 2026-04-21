#!/usr/bin/env python
"""
公众号头图生成脚本 - 第 08 篇 模板与规范
使用 Pillow 本地生成
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PATH = "E:/PMbranding/assets/covers/08-cover.png"
WIDTH, HEIGHT = 2350, 1000
BG_COLOR = (80, 60, 140)

def create_cover():
    img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Top accent bar
    draw.rectangle([0, 0, WIDTH, 8], fill=(255, 180, 60))

    font_paths = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
    ]

    title_font = None
    subtitle_font = None

    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                title_font = ImageFont.truetype(font_path, 100)
                subtitle_font = ImageFont.truetype(font_path, 40)
                print(f"使用字体：{font_path}")
                break
            except:
                continue

    if not title_font:
        print("警告：未找到中文字体，使用默认字体")
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Title: 14 个 AI 产出风格完全不同
    # Subtitle: 模板与规范，让产出从一开始就像你写的
    line1 = "14 个 AI 产出风格完全不同"
    line2 = "模板与规范，让产出从一开始就像你写的"

    text_color = (255, 255, 255)

    bbox1 = title_font.getbbox(line1)
    bbox2 = title_font.getbbox(line2)
    text_width1 = bbox1[2] - bbox1[0]
    text_width2 = bbox2[2] - bbox2[0]
    text_height = bbox1[3] - bbox1[1]

    line_spacing = 30
    total_height = text_height * 2 + line_spacing
    start_y = (HEIGHT - total_height) // 2 - 20

    x1 = (WIDTH - text_width1) // 2
    x2 = (WIDTH - text_width2) // 2

    draw.text((x1, start_y), line1, font=title_font, fill=text_color)
    draw.text((x2, start_y + text_height + line_spacing), line2, font=subtitle_font, fill=text_color)

    # Bottom right tag
    tag_text = "模板与规范"
    tag_bbox = subtitle_font.getbbox(tag_text)
    tag_width = tag_bbox[2] - tag_bbox[0]
    draw.text((WIDTH - tag_width - 60, HEIGHT - 50), tag_text, font=subtitle_font, fill=(200, 200, 200))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    img.save(OUTPUT_PATH, "PNG")
    print(f"封面已保存：{OUTPUT_PATH}")
    print(f"尺寸：{WIDTH}x{HEIGHT}")

if __name__ == "__main__":
    print("开始生成公众号封面...")
    create_cover()
