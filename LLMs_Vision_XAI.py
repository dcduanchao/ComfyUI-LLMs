import requests
import base64
from io import BytesIO
from PIL import Image


def process_xai(encoded_image, prompt, config):
    """处理图像并返回 xAI Grok 视觉模型的响应

    Args:
        encoded_image: base64编码的图像
        prompt: 提示词
        config: 模型配置信息

    Returns:
        str: 模型的响应文本
    """
    try:
        # 构建 API 请求
        url = "https://api.x.ai/v1/responses"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config['api_key']}"
        }

        # 构建消息数组 - 包含图像和文本
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]

        # 构建请求体
        payload = {
            "input": messages,
            "model": config['model_list'][0],
            "max_tokens": 4096
        }

        # 发送请求
        response = requests.post(url, headers=headers, json=payload, timeout=3600)

        # 检查响应
        if response.status_code != 200:
            return f"xAI Grok 视觉处理出错: {response.status_code} - {response.text}"

        # 解析响应
        result = response.json()

        # 提取响应内容
        if 'output' in result and 'choices' in result['output'] and len(result['output']['choices']) > 0:
            content = result['output']['choices'][0]['message']['content']
            return content
        else:
            return f"xAI Grok 视觉处理出错: 无法解析响应 - {str(result)}"

    except Exception as e:
        return f"xAI Grok 视觉处理出错: {str(e)}"
