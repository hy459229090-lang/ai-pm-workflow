#!/usr/bin/env python
"""
小红书轮播图生成脚本 - 第 04 篇：数据取数自动化
大字报极简风格 - 纯色背景 + 超大文字
"""

from PIL import Image, ImageDraw, ImageFont
import os

# 输出目录
OUTPUT_DIR = "E:/PMbranding/assets/xiaohongshu/04-data-agent"

# 画布尺寸 - 小红书竖版 3:4 (推荐 1080x1440)
WIDTH, HEIGHT = 1080, 1440

# 配色方案
COLORS = {
    "yellow": "#FFD700",      # 亮黄
    "green": "#00FF88",       # 荧光绿
    "purple": "#4A00FF",      # 电光紫
    "blue": "#0047FF",        # 克莱因蓝
    "red": "#FF3333",         # 红色强调
    "white": "#FFFFFF",
    "black": "#000000",
    "gray": "#888888",
}

def get_font(size):
    """获取中文字体"""
    font_paths = [
        "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
        "C:/Windows/Fonts/simhei.ttf",    # 黑体
        "C:/Windows/Fonts/simbold.ttf",   # 粗黑体
    ]

    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                continue
    return ImageFont.load_default()

def create_text_image(background_color, text_elements, output_path):
    """
    创建纯色背景大字报图片

    background_color: 背景色 hex
    text_elements: 文字元素列表 [(text, size, color, position, align)]
    output_path: 输出路径
    """
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), color=background_color)
    draw = ImageDraw.Draw(img)

    for text, font_size, color, position, align in text_elements:
        font = get_font(font_size)

        # 计算文字位置
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x, y = position
        if align == "center":
            x = (WIDTH - text_width) // 2
        elif align == "right":
            x = WIDTH - text_width - 40
        elif align == "left":
            x = 40

        draw.text((x, y), text, font=font, fill=color)

    img.save(output_path, "PNG", quality=95)
    print(f"已生成：{output_path}")
    return True

def draw_rect(draw, coords, color, width=0):
    """绘制矩形"""
    draw.rectangle(coords, outline=color, width=width, fill=color if width == 0 else None)

def generate_p1():
    """P1 - 封面"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["yellow"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(80)
    font_subtitle = get_font(32)

    # 主标题 - 两行
    title1 = "我让 AI 跑了 7 天数据"
    title2 = "老板问我是不是换了人"

    # 居中绘制标题
    bbox1 = draw.textbbox((0, 0), title1, font=font_title)
    bbox2 = draw.textbbox((0, 0), title2, font=font_title)
    total_width = max(bbox1[2] - bbox1[0], bbox2[2] - bbox2[0])
    total_height = (bbox1[3] - bbox1[1]) + (bbox2[3] - bbox2[1]) + 20

    start_y = (HEIGHT - total_height) // 2 - 100
    draw.text(((WIDTH - (bbox1[2] - bbox1[0])) // 2, start_y), title1, font=font_title, fill=COLORS["black"])
    draw.text(((WIDTH - (bbox2[2] - bbox2[0])) // 2, start_y + (bbox1[3] - bbox1[1]) + 20), title2, font=font_title, fill=COLORS["black"])

    # 右下角小字
    subtitle = "不会 SQL 的产品怎么活下来的？"
    draw.text((WIDTH - 300, HEIGHT - 100), subtitle, font=font_subtitle, fill=COLORS["gray"])

    output_path = f"{OUTPUT_DIR}/p1.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P1: {output_path}")

def generate_p2():
    """P2 - 痛点"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["white"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_bubble = get_font(28)
    font_big = get_font(64)

    # 顶部大标题
    title = "每次查数据，都要说一遍"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 60), title, font=font_title, fill=COLORS["black"])

    # 聊天气泡 (3 条，透明度递增)
    bubbles = [
        ("帮我查 DAU，用 t_user 表...", 1.0),
        ("帮我查留存，用 t_user 表...", 0.6),
        ("帮我查营收，用 t_order 表...", 0.3),
    ]

    start_y = 200
    for i, (text, alpha) in enumerate(bubbles):
        y = start_y + i * 180
        # 气泡背景
        bbox = draw.textbbox((0, 0), text, font=font_bubble)
        bubble_w = bbox[2] - bbox[0] + 40
        bubble_h = bbox[3] - bbox[1] + 20
        bubble_x = (WIDTH - bubble_w) // 2

        # 根据透明度计算颜色
        gray = int(220 * alpha)
        draw.rounded_rectangle([bubble_x, y, bubble_x + bubble_w, y + bubble_h], radius=10, fill=(gray, gray, gray, int(255 * alpha)))

        # 气泡文字
        text_x = bubble_x + 20
        text_y = y + 10
        text_color = (int(50 * alpha), int(50 * alpha), int(50 * alpha))
        draw.text((text_x, text_y), text, font=font_bubble, fill=text_color)

    # 底部红色大字
    bottom_text = "你不累吗？"
    bbox = draw.textbbox((0, 0), bottom_text, font=font_big)
    draw.text(((WIDTH - (bbox[2] - bbox[0])) // 2, HEIGHT - 150), bottom_text, font=font_big, fill=COLORS["red"])

    output_path = f"{OUTPUT_DIR}/p2.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P2: {output_path}")

def generate_p3():
    """P3 - 核心洞察"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["purple"])
    draw = ImageDraw.Draw(img)

    font_wrong = get_font(48)
    font_right = get_font(64)
    font_small = get_font(32)

    # 上方错误认知（带删除线）
    wrong_text = "Skill = Prompt 模板"
    wrong_bbox = draw.textbbox((0, 0), wrong_text, font=font_wrong)
    wrong_x = (WIDTH - (wrong_bbox[2] - wrong_bbox[0])) // 2
    wrong_y = HEIGHT // 3

    draw.text((wrong_x, wrong_y), wrong_text, font=font_wrong, fill=COLORS["gray"])
    # 删除线
    draw.line([(wrong_x - 10, wrong_y + 24), (wrong_x + wrong_bbox[2] - wrong_bbox[0] + 10, wrong_y + 24)], fill=COLORS["red"], width=4)
    # 红色叉号
    draw.text((wrong_x - 50, wrong_y), "❌", font=font_wrong, fill=COLORS["red"])

    # 下方正确认知
    right_text = "Skill = 给 AI 加能力"
    right_bbox = draw.textbbox((0, 0), right_text, font=font_right)
    right_x = (WIDTH - (right_bbox[2] - right_bbox[0])) // 2
    right_y = HEIGHT // 2 + 50

    draw.text((right_x, right_y), right_text, font=font_right, fill=COLORS["white"])
    # 绿色对勾
    draw.text((right_x - 50, right_y), "✅", font=font_right, fill="#00FF00")

    # 底部小字
    small_text = "不是让它背模板，是让它学会"
    small_bbox = draw.textbbox((0, 0), small_text, font=font_small)
    draw.text(((WIDTH - (small_bbox[2] - small_bbox[0])) // 2, HEIGHT - 150), small_text, font=font_small, fill=COLORS["white"])

    output_path = f"{OUTPUT_DIR}/p3.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P3: {output_path}")

def generate_p4():
    """P4 - 效果对比"""
    # 左右分屏
    half_width = WIDTH // 2
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["white"])
    draw = ImageDraw.Draw(img)

    # 左半部分红色
    draw.rectangle([0, 0, half_width, HEIGHT], fill=COLORS["red"])
    # 右半部分绿色
    draw.rectangle([half_width, 0, WIDTH, HEIGHT], fill="#00AA66")

    font_time = get_font(40)
    font_text = get_font(20)
    font_arrow = get_font(80)

    # 左侧 - 红色
    left_time = "每次 30 秒"
    left_text = """帮我查昨天 DAU
用 t_event_log 表
按 event_time 过滤
排除测试账号..."""

    draw.text((40, 80), left_time, font=font_time, fill=COLORS["white"])

    # 左侧气泡
    bubble_left_x, bubble_left_y = 20, 160
    draw.rounded_rectangle([bubble_left_x, bubble_left_y, half_width - 20, bubble_left_y + 200], radius=10, fill=COLORS["white"])
    draw.multiline_text((bubble_left_x + 15, bubble_left_y + 15), left_text, font=font_text, fill=COLORS["black"])

    # 右侧 - 绿色
    right_time = "现在 3 秒"
    right_text = "/data 过去 7 天 DAU"

    draw.text((half_width + 40, 80), right_time, font=font_time, fill=COLORS["white"])

    # 右侧气泡
    bubble_right_x, bubble_right_y = half_width + 20, 160
    draw.rounded_rectangle([bubble_right_x, bubble_right_y, WIDTH - 20, bubble_right_y + 60], radius=10, fill=COLORS["white"])
    draw.text((bubble_right_x + 15, bubble_right_y + 15), right_text, font=font_text, fill=COLORS["black"])

    # 中间大箭头
    arrow_text = "→"
    draw.text((WIDTH // 2 - 30, HEIGHT // 2), arrow_text, font=font_arrow, fill=COLORS["white"])

    output_path = f"{OUTPUT_DIR}/p4.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P4: {output_path}")

def generate_p5():
    """P5 - 它能做什么"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["green"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_item = get_font(36)
    font_bottom = get_font(36)

    # 顶部标题
    title = "它现在会什么？"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 50), title, font=font_title, fill=COLORS["black"])

    # 四个黑色方块
    items = [
        "说人话查数据",
        "自动写 SQL",
        "生成图表",
        "解释逻辑",
    ]

    box_size = 80
    start_y = 200
    gap = 130

    for i, item in enumerate(items):
        y = start_y + i * gap
        box_x = (WIDTH - box_size) // 2

        # 黑色方块
        draw.rectangle([box_x, y, box_x + box_size, y + box_size], fill=COLORS["black"])

        # 方块右侧文字
        draw.text((box_x + box_size + 20, y + 22), item, font=font_item, fill=COLORS["white"])

    # 底部文字
    bottom = "你只需要会提问"
    draw.text(((WIDTH - draw.textbbox((0, 0), bottom, font=font_bottom)[2]) // 2, HEIGHT - 120), bottom, font=font_bottom, fill=COLORS["black"])

    output_path = f"{OUTPUT_DIR}/p5.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P5: {output_path}")

def generate_p6():
    """P6 - 最大坑"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["white"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_item = get_font(36)
    font_box = get_font(32)

    # 顶部标题
    title = "我踩过最大的坑"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 50), title, font=font_title, fill=COLORS["black"])

    # 中央警告三角
    warning = "⚠️"
    draw.text(((WIDTH - 120) // 2, 150), warning, font=get_font(120))

    # 下方文字
    items = [
        "我以为口径一样",
        "AI 理解的和我想的不一样",
        "算出来差一倍",
    ]

    start_y = 350
    for i, item in enumerate(items):
        y = start_y + i * 70
        draw.text((40, y), f"• {item}", font=font_item, fill=COLORS["black"])

    # 底部黑框白底
    box_text = "先对齐定义，再执行"
    box_bbox = draw.textbbox((0, 0), box_text, font=font_box)
    box_w = box_bbox[2] - box_bbox[0] + 80
    box_h = box_bbox[3] - box_bbox[1] + 40
    box_x = (WIDTH - box_w) // 2
    box_y = HEIGHT - 180

    # 黑框
    draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], outline=COLORS["black"], width=4, fill=COLORS["white"])
    draw.text((box_x + 40, box_y + 20), box_text, font=font_box, fill=COLORS["black"])

    output_path = f"{OUTPUT_DIR}/p6.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P6: {output_path}")

def generate_p7():
    """P7 - 搞不定的场景"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["blue"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_item = get_font(32)
    font_bottom = get_font(28)

    # 顶部标题
    title = "什么时候搞不定？"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 50), title, font=font_title, fill=COLORS["white"])

    # 三个条目
    items = [
        ("中间表没权限", "手动导出"),
        ("表是别人建的", "先采样再确认"),
        ("复杂连表", "AI 写基础版人优化"),
    ]

    start_y = 250
    for i, (left, right) in enumerate(items):
        y = start_y + i * 150

        # 圆点
        draw.ellipse([(40, y + 10), (60, y + 30)], fill=COLORS["white"])

        # 左侧文字
        draw.text((80, y), left, font=font_item, fill=COLORS["white"])

        # 右侧箭头和说明
        draw.text((80, y + 50), f"→ {right}", font=get_font(28), fill=COLORS["gray"])

    # 底部小字
    bottom = "它不是万能的，但 80% 够了"
    draw.text(((WIDTH - draw.textbbox((0, 0), bottom, font=font_bottom)[2]) // 2, HEIGHT - 100), bottom, font=font_bottom, fill=COLORS["white"])

    output_path = f"{OUTPUT_DIR}/p7.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P7: {output_path}")

def generate_p8():
    """P8 - 核心观点"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["yellow"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_big = get_font(180)
    font_mid = get_font(40)
    font_small = get_font(28)

    # 顶部标题
    title = "人人都是数据科学家？"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 50), title, font=font_title, fill=COLORS["black"])

    # 中央超大数字
    percent = "80%"
    draw.text(((WIDTH - draw.textbbox((0, 0), percent, font=font_big)[2]) // 2, HEIGHT // 2 - 120), percent, font=font_big, fill=COLORS["black"])

    # 下方解释
    explain = "日常分析 AI 搞定"
    draw.text(((WIDTH - draw.textbbox((0, 0), explain, font=font_mid)[2]) // 2, HEIGHT // 2 + 80), explain, font=font_mid, fill=COLORS["black"])

    # 底部小字
    bottom = "剩下 20% 靠专家（复杂建模/数据治理/口径统一）"
    draw.text(((WIDTH - draw.textbbox((0, 0), bottom, font=font_small)[2]) // 2, HEIGHT - 100), bottom, font=font_small, fill=COLORS["black"])

    output_path = f"{OUTPUT_DIR}/p8.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P8: {output_path}")

def generate_p9():
    """P9 - 互动页"""
    img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS["white"])
    draw = ImageDraw.Draw(img)

    font_title = get_font(56)
    font_option = get_font(36)
    font_bottom = get_font(32)
    font_credit = get_font(20)

    # 顶部标题
    title = "你在用什么方式"
    title2 = "做数据分析？"
    draw.text(((WIDTH - draw.textbbox((0, 0), title, font=font_title)[2]) // 2, 50), title, font=font_title, fill=COLORS["black"])
    draw.text(((WIDTH - draw.textbbox((0, 0), title2, font=font_title)[2]) // 2, 110), title2, font=font_title, fill=COLORS["black"])

    # 三个选项
    options = [
        "手动写 SQL",
        "试过 AI 生成",
        "还在用 Excel",
    ]

    start_y = 300
    for i, option in enumerate(options):
        y = start_y + i * 100

        # 选择框
        draw.rectangle([(WIDTH // 2 - 200, y), (WIDTH // 2 - 160, y + 40)], outline=COLORS["black"], width=3, fill=None)

        # 选项文字
        draw.text((WIDTH // 2 - 140, y + 5), option, font=font_option, fill=COLORS["black"])

    # 底部文字
    bottom = "评论区聊聊，我很好奇"
    draw.text(((WIDTH - draw.textbbox((0, 0), bottom, font=font_bottom)[2]) // 2, HEIGHT - 180), bottom, font=font_bottom, fill=COLORS["black"])

    # 右下角署名
    credit = "RicHe · AI-PM-Workflow"
    draw.text((WIDTH - 280, HEIGHT - 60), credit, font=font_credit, fill=COLORS["gray"])

    output_path = f"{OUTPUT_DIR}/p9.png"
    img.save(output_path, "PNG", quality=95)
    print(f"已生成 P9: {output_path}")

def main():
    """主函数 - 生成全部 9 张图片"""
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"开始生成小红书轮播图，输出目录：{OUTPUT_DIR}")
    print(f"画布尺寸：{WIDTH}x{HEIGHT}")
    print("-" * 50)

    # 逐张生成
    generate_p1()
    generate_p2()
    generate_p3()
    generate_p4()
    generate_p5()
    generate_p6()
    generate_p7()
    generate_p8()
    generate_p9()

    print("-" * 50)
    print(f"全部生成完成！")
    print(f"保存路径：{OUTPUT_DIR}/p1.png ~ p9.png")

if __name__ == "__main__":
    main()
