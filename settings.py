import os
import yaml
import pathlib

DEFAULT_SETTINGS = {
    "chatllmleoleexh": {
        "openai_compatible": {
            "default": {
                "api_key": "your-xai-api-key",
                "model": [
                    "grok-4-0709",
                    "grok-4",
                    "grok-3",
                    "grok-3-mini",
                    "grok-3-fast",
                    "grok-2-vision-1212",
                    "grok-4-1-fast-non-reasoning",
                    "grok-4-1-fast-reasoning",
                    "grok-4-fast-non-reasoning",
                    "grok-4-fast-reasoning"
                ]
            }
        },
        "vision_models": {
            "xai": {
                "api_key": "your-xai-api-key",
                "model_list": [
                    "grok-4-0709",
                    "grok-4",
                    "grok-3",
                    "grok-3-mini",
                    "grok-3-fast",
                    "grok-2-vision-1212",
                    "grok-4-1-fast-non-reasoning",
                    "grok-4-1-fast-reasoning",
                    "grok-4-fast-non-reasoning",
                    "grok-4-fast-reasoning"
                ]
            }
        },
        "example_user_prompt": "your user prompt here",
        "prompt_templates": {
            "default": {
                "system": "You are Grok, a highly intelligent, helpful AI assistant.",
                "prefix": "",
                "suffix": ""
            },
            "image_generator": {
                "system": "You are an expert image prompt generator. Convert text descriptions into detailed, high-quality image prompts suitable for AI image generation models.",
                "prefix": "Create a detailed image prompt for: ",
                "suffix": " - Include specific details about style, lighting, colors, composition, and mood."
            },
            "creative_writer": {
                "system": "You are a creative writing assistant. Help generate engaging stories, vivid descriptions, and compelling narratives.",
                "prefix": "Write about: ",
                "suffix": ""
            },
            "code_assistant": {
                "system": "You are an expert programmer. Help write, debug, and explain code in various programming languages. Provide clear, well-commented code examples when appropriate.",
                "prefix": "",
                "suffix": ""
            },
            "chinese_assistant": {
                "system": "你是一个有用的中文助手。请用中文回答用户的问题，提供准确、详细的信息。",
                "prefix": "",
                "suffix": ""
            }
        }
    }
}


def load_settings():
    """加载配置文件，如果文件不存在则返回默认配置"""
    path = os.path.join(os.path.dirname(__file__), "settings.yaml")
    file_path = pathlib.Path(path)
    if not file_path.exists():
        return DEFAULT_SETTINGS['chatllmleoleexh']

    with open(path, 'r', encoding='utf-8') as settings:
        the_yaml = yaml.safe_load(settings)
    return the_yaml['chatllmleoleexh']


def get_chat_settings(section: str = "default"):
    """获取聊天配置"""
    settings = load_settings()
    return settings['openai_compatible'][section]


def get_vision_settings(model_type: str):
    """获取视觉模型配置"""
    settings = load_settings()
    return settings['vision_models'].get(model_type)
