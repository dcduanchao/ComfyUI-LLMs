#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本地测试脚本 - xAI Grok API
直接测试聊天和视觉功能，无需启动 ComfyUI
"""
import json
import os
import sys

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import requests
import base64
from PIL import Image
import io

# 导入本地模块
import settings
from xai_client import complete_xai


def test_chat():
    """测试聊天功能"""
    print("\n" + "="*60)
    print("🤖 测试 xAI Grok 聊天功能")
    print("="*60)

    try:
        # 加载配置
        all_settings = settings.load_settings()
        chat_config = settings.get_chat_settings('default')
        api_key = chat_config['api_key']

        print(f"\n📝 配置信息:")
        print(f"   - API Key: {api_key[:10]}...")
        print(f"   - 模型: grok-4-0709")

        # 测试问题
        test_questions = [
            "海滩，美女"
        ]

        for i, question in enumerate(test_questions, 1):
            print(f"\n{'='*60}")
            print(f"📋 测试 {i}/{len(test_questions)}")
            print(f"{'='*60}")
            print(f"\n❓ 问题: {question}")
            print(f"⏳ 正在调用 API...")

            try:
                # 获取 Stable Diffusion Prompt 生成模板
                template_name = 'sd_prompt_generator'
                template_config = all_settings['prompt_templates'].get(template_name, {})

                if template_config:
                    system_prompt = template_config.get('system', '')
                    prefix = template_config.get('prefix', '')
                    suffix = template_config.get('suffix', '')
                    user_prompt = f"{prefix}{question}{suffix}"

                    print(f"\n📋 使用模板: {template_name}")
                else:
                    system_prompt = "You are a helpful assistant."
                    user_prompt = question
                    print(f"\n⚠️  模板 '{template_name}' 不存在，使用默认设置")

                # 调用 API
                response = complete_xai(
                    api_key=api_key,
                    model="grok-4-0709",
                    temperature=0.7,
                    top_p=1.0,
                    system_content=system_prompt,
                    user_content=user_prompt,
                    max_tokens=512
                )

                # 解析响应
                if 'output' in response and len(response['output']) > 0:
                    output = response['output'][0]
                    if 'content' in output and len(output['content']) > 0:
                        content_item = output['content'][0]
                        if 'text' in content_item:
                            content = content_item['text']
                            print(f"\n✅ 原始回答:")
                            print(f"   {content}")

                            # 尝试解析 JSON
                            try:
                                content_json = json.loads(content)
                                print(f"\n📊 解析结果:")
                                print(f"   🇨🇳 中文提示词 (zh_prompt):")
                                print(f"      {content_json.get('zh_prompt', '')}")
                                print(f"   🇺🇸 英文提示词 (en_prompt):")
                                print(f"      {content_json.get('en_prompt', '')}")
                                print(f"   🇨🇳 中文负向提示词 (zh_na_prompt):")
                                print(f"      {content_json.get('zh_na_prompt', '')}")
                                print(f"   🇺🇸 英文负向提示词 (en_na_prompt):")
                                print(f"      {content_json.get('en_na_prompt', '')}")
                                print(f"\n📊 Tokens: {response.get('usage', {}).get('total_tokens', 'N/A')}")
                            except json.JSONDecodeError as e:
                                print(f"\n❌ JSON 解析失败: {str(e)}")
                                print(f"   原始内容: {content}")
                        else:
                            print(f"\n❌ 响应中缺少 'text' 字段: {list(content_item.keys())}")
                    else:
                        print(f"\n❌ 响应中缺少 'content' 字段或为空")
                else:
                    print(f"\n❌ 响应中缺少 'output' 字段或为空")

            except Exception as e:
                print(f"\n❌ 测试失败: {str(e)}")

        print(f"\n{'='*60}")
        print("✅ 聊天功能测试完成")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()


def test_vision():
    """测试视觉功能"""
    print("\n" + "="*60)
    print("🎯 测试 xAI Grok 视觉功能")
    print("="*60)

    try:
        # 加载配置
        vision_config = settings.get_vision_settings('xai')
        api_key = vision_config['api_key']

        print(f"\n📝 配置信息:")
        print(f"   - API Key: {api_key[:10]}...")
        print(f"   - 模型: grok-4")

        # 检查是否有测试图片
        test_image_path = "examples/screenshot01.png"
        if not os.path.exists(test_image_path):
            print(f"\n⚠️  未找到测试图片: {test_image_path}")
            print("   跳过视觉测试")
            return

        print(f"\n📸 测试图片: {test_image_path}")

        # 编码图片
        import base64
        from PIL import Image
        import io

        with open(test_image_path, 'rb') as f:
            image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode()

        print(f"⏳ 正在调用视觉 API...")

        # 导入视觉处理函数
        import LLMs_Vision_XAI

        # 调用视觉 API
        result = LLMs_Vision_XAI.process_xai(
            encoded_image=encoded_image,
            prompt="请详细描述这张图片的内容",
            config=vision_config
        )

        print(f"\n✅ 图片描述:")
        print(f"   {result[:300]}..." if len(result) > 300 else f"   {result}")

        print(f"\n{'='*60}")
        print("✅ 视觉功能测试完成")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()


def test_parameters():
    """测试不同参数"""
    print("\n" + "="*60)
    print("🔧 测试不同参数配置")
    print("="*60)

    try:
        all_settings = settings.load_settings()
        chat_config = settings.get_chat_settings('default')
        api_key = chat_config['api_key']

        test_question = "What is 2+2?"

        # 测试不同的 temperature
        temperatures = [0.2, 0.7, 1.2]

        for temp in temperatures:
            print(f"\n📊 测试 temperature={temp}")
            print(f"   问题: {test_question}")

            try:
                response = complete_xai(
                    api_key=api_key,
                    model="grok-4-0709",
                    temperature=temp,
                    top_p=None,
                    system_content="You are a helpful assistant.",
                    user_content=test_question,
                    max_tokens=2000
                )

                if 'output' in response and 'choices' in response['output']:
                    content = response['output']['choices'][0]['message']['content']
                    print(f"   回答: {content}")
                else:
                    print(f"   ❌ 响应格式错误")

            except Exception as e:
                print(f"   ❌ 失败: {str(e)}")

        print(f"\n{'='*60}")
        print("✅ 参数测试完成")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    print("\n" + "="*60)
    print("🚀 ComfyUI-LLMs xAI 本地测试工具")
    print("="*60)

    # 检查配置
    config_path = os.path.join(os.path.dirname(__file__), "settings.yaml")
    if not os.path.exists(config_path):
        print("\n❌ 错误: settings.yaml 文件不存在")
        print("💡 请先运行: cp settings.yaml.sample settings.yaml")
        return

    print("\n✅ 配置文件存在")

    # 菜单
    print("\n请选择测试项目:")
    print("1. 测试聊天功能")
    print("2. 测试视觉功能")
    print("3. 测试不同参数")
    print("4. 运行所有测试")
    print("0. 退出")

    choice = input("\n请输入选项 (0-4): ").strip()

    if choice == "1":
        test_chat()
    elif choice == "2":
        test_vision()
    elif choice == "3":
        test_parameters()
    elif choice == "4":
        test_chat()
        test_vision()
        test_parameters()
    elif choice == "0":
        print("\n👋 退出测试")
    else:
        print("\n❌ 无效的选项")

    print("\n" + "="*60)
    print("🎉 测试完成！")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
