#!/usr/bin/env python3
"""
微信公众号封面图生成器
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

def generate_cover(title, subtitle, tag, output_path, colors):
    """生成公众号封面图"""

    # 创建 16:9 图片 (2350x1000)
    width, height = 2350, 1000
    img = Image.new('RGB', (width, height), color=colors['bg'])
    draw = ImageDraw.Draw(img)

    # 绘制渐变背景
    for y in range(height):
        ratio = y / height
        r = int(colors['bg_start'][0] + (colors['bg_end'][0] - colors['bg_start'][0]) * ratio)
        g = int(colors['bg_start'][1] + (colors['bg_end'][1] - colors['bg_start'][1]) * ratio)
        b = int(colors['bg_start'][2] + (colors['bg_end'][2] - colors['bg_start'][2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 顶部装饰条
    draw.rectangle([0, 0, width, 8], fill=colors['accent'])

    # 加载字体
    try:
        title_font = ImageFont.truetype('simhei.ttf', 72)
        subtitle_font = ImageFont.truetype('simhei.ttf', 36)
        tag_font = ImageFont.truetype('simhei.ttf', 24)
    except:
        try:
            title_font = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 72)
            subtitle_font = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 36)
            tag_font = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 24)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            tag_font = ImageFont.load_default()

    # 绘制标题（居中）
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) / 2
    title_y = height / 2 - 60
    draw.text((title_x, title_y), title, fill=(255, 255, 255), font=title_font)

    # 绘制副标题
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) / 2
    subtitle_y = height / 2 + 30
    draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 255, 255), font=subtitle_font)

    # 绘制标签（右下角）
    tag_bbox = draw.textbbox((0, 0), tag, font=tag_font)
    tag_width = tag_bbox[2] - tag_bbox[0]
    tag_x = width - tag_width - 60
    tag_y = height - 50
    draw.text((tag_x, tag_y), tag, fill=(200, 200, 200), font=tag_font)

    # 保存
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f'封面已保存：{output_path}')
    return output_path


def main():
    import sys
    article_num = sys.argv[1] if len(sys.argv) > 1 else "05"

    configs = {
        "05": {
            'title': '一个人管 14 个 AI 是什么体验',
            'subtitle': '从混乱到秩序，我走了 3 个月',
            'tag': 'Agent Team 实战',
            'output': 'assets/wechat/05-cover.png',
            'colors': {
                'bg_start': (26, 26, 46),
                'bg_end': (255, 107, 53),
                'bg': (26, 26, 46),
                'accent': (255, 107, 53),
            }
        },
        "06": {
            'title': 'AI 给的东西 你敢直接用吗',
            'subtitle': '3 个信号，该打回重做',
            'tag': 'AI 产出评估指南',
            'output': 'assets/wechat/06-cover.png',
            'colors': {
                'bg_start': (255, 215, 0),    # 亮黄
                'bg_end': (255, 196, 0),       # 金黄
                'bg': (255, 215, 0),
                'accent': (0, 0, 0),
            }
        }
    }

    config = configs.get(article_num, configs["05"])

    generate_cover(
        config['title'],
        config['subtitle'],
        config['tag'],
        config['output'],
        config['colors']
    )


if __name__ == '__main__':
    main()
