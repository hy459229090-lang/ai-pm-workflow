#!/usr/bin/env python
"""
公众号头图生成脚本
调用 AI 图片生成 API 生成技术风格封面图
"""

import requests
import base64
import json
import os

# 输出路径
OUTPUT_PATH = "E:/PMbranding/assets/wechat/04-cover-yellow.png"

# 提示词（亮黄色极简大字报风格）
PROMPT = """
Horizontal banner 2.35:1 aspect ratio. Pure bright yellow background (#FFD700), no gradient.
Center: ultra-large black ultra-bold Chinese text in two lines:
Line 1: 「我让 AI 跑了 7 天数据」
Line 2: 「老板问我是不是换了人」
Text occupies 60% of the image. No other elements. Minimalist poster style.
"""

def generate_image():
    """
    使用 Fal.ai FLUX 模型生成图片
    FLUX 对文字渲染效果较好
    """
    # 使用 Fal.ai API (FLUX 模型)
    url = "https://queue.fal.run/fal-ai/flux-pro/v1.1/image"

    headers = {
        "Authorization": f"Key {os.environ.get('FAL_KEY', '')}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": PROMPT,
        "image_size": {"width": 2350, "height": 1000},  # 2.35:1
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "negative_prompt": "blurry, low quality, distorted text, unreadable"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']
            # 下载图片
            img_response = requests.get(image_url, timeout=30)
            with open(OUTPUT_PATH, 'wb') as f:
                f.write(img_response.content)
            print(f"图片已保存到：{OUTPUT_PATH}")
            return True
        else:
            print("API 返回结果中没有图片")
            print(json.dumps(result, indent=2))
            return False

    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误：{e}")
        print(f"响应内容：{e.response.text if hasattr(e, 'response') else 'N/A'}")
        return False
    except Exception as e:
        print(f"生成失败：{e}")
        return False

if __name__ == "__main__":
    # 确保输出目录存在
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # 检查 API Key
    if not os.environ.get('FAL_KEY'):
        print("错误：请设置 FAL_KEY 环境变量")
        print("可以在 https://fal.ai/dashboard/keys 获取 API Key")
        exit(1)

    print("开始生成公众号头图...")
    print(f"提示词：{PROMPT[:100]}...")
    success = generate_image()
    exit(0 if success else 1)
