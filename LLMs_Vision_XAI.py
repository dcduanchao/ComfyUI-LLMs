import json

import requests


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
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{encoded_image}",
                        "detail": "high"
                    },
                    {
                        "type": "input_text",
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
        # print(json.dumps(payload, ensure_ascii=False))
        # 发送请求
        response = requests.post(url, headers=headers, json=payload, timeout=3600)
        print(response.text)

        # 检查响应
        if response.status_code != 200:
            return f"xAI Grok 视觉处理出错: {response.status_code} - {response.text}"

        # 解析响应
        result = response.json()

        # 提取响应内容
        # xAI 视觉 API 响应格式: output[0].content[0].text
        if 'output' in result and len(result['output']) > 0:
            output_item = result['output'][0]
            if 'content' in output_item and len(output_item['content']) > 0:
                content_item = output_item['content'][0]
                if 'text' in content_item:
                    return content_item['text']

        return f"xAI Grok 视觉处理出错: 无法解析响应 - {str(result)}"

    except Exception as e:
        return f"xAI Grok 视觉处理出错: {str(e)}"
