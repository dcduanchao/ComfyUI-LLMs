#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 LLMs_Chat 节点的新功能
"""

import os
import sys

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from LLMs_Chat import LLMs_Chat


def test_template_and_json():
    """测试模板选择和 JSON 解析"""
    print("\n" + "="*80)
    print("🧪 测试 LLMs_Chat 节点 - 模板选择和 JSON 解析")
    print("="*80)

    # 创建节点实例
    chat_node = LLMs_Chat()

    # 测试参数
    api = "default"
    model = "grok-4-0709"
    template = "sd_prompt_generator"
    user_prompt = "海滩，美女"
    temperature = 0.7
    top_p = 1.0
    max_tokens = 512
    system_prompt = ""
    parse_json = True

    print(f"\n📋 测试参数:")
    print(f"   - API: {api}")
    print(f"   - 模型: {model}")
    print(f"   - 模板: {template}")
    print(f"   - 用户提示词: {user_prompt}")
    print(f"   - 解析 JSON: {parse_json}")

    print(f"\n⏳ 正在调用 LLMs_Chat.generate()...")

    try:
        # 调用 generate 方法
        result = chat_node.generate(
            api=api,
            model=model,
            template=template,
            user_prompt=user_prompt,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            parse_json=parse_json
        )

        # 解包结果
        grok_response, zh_prompt, en_prompt, zh_na_prompt, en_na_prompt = result

        print(f"\n✅ 调用成功！")
        print(f"\n📄 原始响应 (grok_response):")
        print(f"   {grok_response[:400]}..." if len(grok_response) > 400 else f"   {grok_response}")

        print(f"\n📊 解析结果:")
        print(f"   🇨🇳 中文提示词 (zh_prompt):")
        print(f"      {zh_prompt}")
        print(f"   🇺🇸 英文提示词 (en_prompt):")
        print(f"      {en_prompt}")
        print(f"   🇨🇳 中文负向提示词 (zh_na_prompt):")
        print(f"      {zh_na_prompt}")
        print(f"   🇺🇸 英文负向提示词 (en_na_prompt):")
        print(f"      {en_na_prompt}")

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()

    print(f"\n{'='*80}")
    print("🎉 测试完成！")
    print(f"{'='*80}\n")


def test_without_json_parsing():
    """测试不解析 JSON 的情况"""
    print("\n" + "="*80)
    print("🧪 测试 LLMs_Chat 节点 - 不解析 JSON")
    print("="*80)

    chat_node = LLMs_Chat()

    api = "default"
    model = "grok-4-0709"
    template = "default"
    user_prompt = "你好，请用中文简单介绍一下你自己"
    temperature = 0.7
    top_p = 1.0
    max_tokens = 256
    system_prompt = ""
    parse_json = False

    print(f"\n📋 测试参数:")
    print(f"   - API: {api}")
    print(f"   - 模型: {model}")
    print(f"   - 模板: {template}")
    print(f"   - 用户提示词: {user_prompt}")
    print(f"   - 解析 JSON: {parse_json}")

    print(f"\n⏳ 正在调用 LLMs_Chat.generate()...")

    try:
        result = chat_node.generate(
            api=api,
            model=model,
            template=template,
            user_prompt=user_prompt,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            system_prompt=system_prompt,
            parse_json=parse_json
        )

        grok_response, zh_prompt, en_prompt, zh_na_prompt, en_na_prompt = result

        print(f"\n✅ 调用成功！")
        print(f"\n📄 原始响应 (grok_response):")
        print(f"   {grok_response[:400]}..." if len(grok_response) > 400 else f"   {grok_response}")

        print(f"\n📊 其他字段（应该为空）:")
        print(f"   zh_prompt: '{zh_prompt}'")
        print(f"   en_prompt: '{en_prompt}'")
        print(f"   zh_na_prompt: '{zh_na_prompt}'")
        print(f"   en_na_prompt: '{en_na_prompt}'")

    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()

    print(f"\n{'='*80}")
    print("🎉 测试完成！")
    print(f"{'='*80}\n")


def main():
    """主函数"""
    print("\n" + "="*80)
    print("🚀 LLMs_Chat 节点功能测试")
    print("="*80)

    # 测试 1: 使用模板并解析 JSON
    test_template_and_json()

    # 测试 2: 不解析 JSON
    test_without_json_parsing()

    print("\n" + "="*80)
    print("🎉 所有测试完成！")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
