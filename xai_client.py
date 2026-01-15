import requests
import json
import os

# 导入 settings 模块
from . import settings


def complete_xai(api_key: str, model: str, temperature: float, top_p: float,
                system_content: str, user_content: str, max_tokens: int = 4096):
    """
    调用 xAI Grok API 完成对话

    Args:
        api_key: xAI API 密钥
        model: 模型名称
        temperature: 温度参数
        top_p: 核采样参数
        system_content: 系统提示词
        user_content: 用户提示词
        max_tokens: 最大 token 数

    Returns:
        API 响应对象
    """
    # 参数验证（只在参数值超出范围时验证）
    if top_p is not None and (top_p < 0 or top_p > 1):
        raise ValueError('top_p must be a number between 0 and 1')
    if temperature is not None and (temperature < 0 or temperature > 2):
        raise ValueError('Temperature should be a value between 0.0 and 2.0')

    # 构建 API 请求
    url = "https://api.x.ai/v1/responses"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # 构建消息数组
    messages = []
    if system_content:
        messages.append({
            "role": "system",
            "content": system_content
        })
    if user_content:
        messages.append({
            "role": "user",
            "content": user_content
        })

    # 构建请求体
    payload = {
        "input": messages,
        "model": model,
        "max_tokens": max_tokens
    }

    # 添加可选参数
    if temperature is not None:
        payload["temperature"] = temperature
    if top_p is not None:
        payload["top_p"] = top_p
    print(url)
    print(json.dumps(payload, ensure_ascii=False))

    # 发送请求
    response = requests.post(url, headers=headers, json=payload, timeout=3600)
    print(response.text)
    # 检查响应
    if response.status_code != 200:
        raise RuntimeError(f"xAI API 请求失败: {response.status_code} - {response.text}")

    return response.json()
