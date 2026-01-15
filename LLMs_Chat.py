from .xai_client import complete_xai
from .settings import load_settings
import json


class LLMs_Chat:
    """xAI Grok 聊天模型节点类"""

    @classmethod
    def INPUT_TYPES(s):
        all_settings = load_settings()
        default_user_prompt = all_settings['example_user_prompt']
        available_apis = [a for a in all_settings['openai_compatible']]
        default_model = all_settings['openai_compatible']['default']['model']

        # 获取所有可用的提示词模板
        available_templates = list(all_settings['prompt_templates'].keys())

        # 获取默认模板的 system 提示词
        default_template = all_settings['prompt_templates'].get('default', {})
        default_system_prompt = default_template.get('system',
            "You are Grok, a highly intelligent, helpful AI assistant.")

        return {
            "required": {
                "api": (available_apis, {
                    "default": "default"
                }),
                "model": (default_model,
                          {"default": "grok-4-0709"}),
                "template": (available_templates, {
                    "default": "default"
                }),
                "user_prompt": ("STRING", {
                    "multiline": True,
                    "default": default_user_prompt
                }),
                "temperature": ("FLOAT", {
                    "default": 0.7, "min": 0.0, "max": 2.0, "step": 0.01,
                }),
            },
            "optional": {
                "system_prompt": ("STRING",
                                  {
                                      "default": default_system_prompt,
                                      "multiline": True, "dynamicPrompts": False
                                  }),
                "parse_json": ("BOOLEAN", {
                    "default": False,
                    "label_on": "解析 JSON",
                    "label_off": "不解析 JSON"
                }),
                "top_p": ("FLOAT", {
                    "default": 1.0, "min": 0.001, "max": 1.0, "step": 0.01,
                }),
                "max_tokens": ("INT", {
                    "default": 4096, "min": 1, "max": 32768, "step": 1,
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("grok_response", "zh_prompt", "en_prompt", "zh_na_prompt", "en_na_prompt")
    FUNCTION = "generate"
    CATEGORY = "xAI"

    def generate(self, api: str, model: str, template: str, temperature: float | None = None,
                 top_p: float | None = None, max_tokens: int = 4096,
                 user_prompt="", system_prompt="", parse_json: bool = False):
        # 获取 API 配置
        from .settings import get_chat_settings
        settings = get_chat_settings(api)
        api_key = settings['api_key']

        # 如果选择了模板，使用模板的配置
        if template:
            all_settings = load_settings()
            template_config = all_settings['prompt_templates'].get(template, {})
            if template_config:
                # 使用模板的 system 提示词（如果 system_prompt 参数为空）
                if not system_prompt and 'system' in template_config:
                    system_prompt = template_config['system']
                # 应用 prefix 和 suffix
                prefix = template_config.get('prefix', '')
                suffix = template_config.get('suffix', '')
                user_prompt = f"{prefix}{user_prompt}{suffix}"

        # 调用 xAI API
        response = complete_xai(
            api_key=api_key,
            model=model,
            temperature=temperature,
            top_p=top_p,
            system_content=system_prompt,
            user_content=user_prompt,
            max_tokens=max_tokens
        )

        # 提取响应内容
        try:
            if 'output' in response and len(response['output']) > 0:
                output = response['output'][0]
                if 'content' in output and len(output['content']) > 0:
                    content_item = output['content'][0]
                    if 'text' in content_item:
                        content = content_item['text']

                        # 如果需要解析 JSON
                        if parse_json:
                            try:
                                content_json = json.loads(content)
                                zh_prompt = content_json.get('zh_prompt', '')
                                en_prompt = content_json.get('en_prompt', '')
                                zh_na_prompt = content_json.get('zh_na_prompt', '')
                                en_na_prompt = content_json.get('en_na_prompt', '')
                                return (content, zh_prompt, en_prompt, zh_na_prompt, en_na_prompt)
                            except json.JSONDecodeError as e:
                                return (content, f"JSON 解析失败: {str(e)}", "", "", "")
                        else:
                            return (content, "", "", "", "")
                    else:
                        return (f"响应中缺少 'text' 字段: {list(content_item.keys())}", "", "", "", "")
                else:
                    return (f"响应中缺少 'content' 字段或为空", "", "", "", "")
            else:
                return (f"响应中缺少 'output' 字段或为空", "", "", "", "")
        except Exception as e:
            return (f"解析响应时出错: {str(e)}\n响应结构: {str(response)[:500]}", "", "", "", "")
