# ComfyUI xAI (Grok) Extension

A ComfyUI extension that supports xAI's Grok models, providing a unified interface for chat and vision capabilities.

![Node Preview](examples/screenshot06.png)

[English](#english) | [中文](#chinese)

<a name="english"></a>
## ✨ Features

- 🤖 Support for xAI Grok chat models
- 🎯 xAI Grok Vision for image understanding
- 🔄 Dynamic model switching between Grok variants
- 🌐 Bilingual interface (English/Chinese)
- ⚙️ Simple configuration with YAML
- 📋 Multiple prompt templates for different use cases

## 📦 Installation

1. Navigate to ComfyUI's custom_nodes directory
```bash
cd ComfyUI/custom_nodes
```

2. Clone the repository and checkout the xai branch
```bash
git clone https://github.com/leoleexh/ComfyUI-LLMs
cd ComfyUI-LLMs
git checkout xai
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Basic Setup

1. Copy the configuration template
```bash
cp settings.yaml.sample settings.yaml
```

2. Edit `settings.yaml` to configure your xAI API key

### Get xAI API Key

1. Visit https://console.x.ai/
2. Sign up or log in to your xAI account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key to your `settings.yaml`

### Configuration Validation

After setting up your configuration, you can use the validation tool:

```bash
python validate_config.py
```

This tool will:
- ✅ Check if `settings.yaml` exists
- ✅ Validate configuration file structure
- ✅ Display current API endpoints and model configurations
- ⚠️ Warn about default API keys that need to be updated

### Detailed Configuration

```yaml
chatllmleoleexh:
  # xAI API Configuration
  openai_compatible:
    default:
      api_base: "https://api.x.ai/v1/chat/completions"
      organisation: "NONE"
      api_key: "your-xai-api-key-here"
      model:
        - "grok-4-0709"
        - "grok-4"
        - "grok-3"
        - "grok-3-mini"
        - "grok-3-fast"
        # ... more models

  # xAI Vision Model Configuration
  vision_models:
    xai:
      api_key: "your-xai-api-key-here"
      api_base: "https://api.x.ai/v1/responses"
      model_list:
        - "grok-4-0709"
        - "grok-4"
        # ... more models

  # Prompt Templates
  prompt_templates:
    default:
      system: "You are Grok, an AI assistant..."
      prefix: ""
      suffix: ""
```

### Supported Models

#### Chat Models
- grok-4-0709
- grok-4
- grok-3
- grok-3-mini
- grok-3-fast
- grok-4-1-fast-non-reasoning
- grok-4-1-fast-reasoning
- grok-4-fast-non-reasoning
- grok-4-fast-reasoning

#### Vision Models
- grok-2-vision-1212
- grok-4 (with vision capabilities)
- grok-3 (with vision capabilities)

### Prompt Templates

The extension includes several pre-configured prompt templates:

1. **default**: General-purpose AI assistant
2. **image_generator**: For generating detailed image prompts
3. **creative_writer**: For creative writing tasks
4. **code_assistant**: For programming and code-related tasks
5. **chinese_assistant**: For Chinese language interactions

You can customize these templates in `settings.yaml` or use them directly in the node's system_prompt field.

## 🎯 Usage

### Chat Function

1. Find `🤖 Grok Chat | 智能对话` in the node list (under 🚀 xAI category)
2. Configure model parameters:
   - Select API configuration (default)
   - Choose the Grok model
   - Set system prompt (or use default)
   - Enter user prompt
   - Adjust temperature (0.0-2.0) and top_p (0.001-1.0)
   - Set max_tokens (optional, default 4096)
3. Run the node to get response

### Image Understanding

1. Find `🎯 Grok Vision | 图像理解` in the node list (under 🚀 xAI category)
2. Configure parameters:
   - Connect image input from ComfyUI
   - Select model type (xai)
   - Choose the specific Grok vision model
   - Enter description prompt
3. Run the node to get image description

## 📝 Notes

- Ensure xAI API key is configured correctly
- Some models may have different capabilities and pricing
- Stable network connection recommended
- Be aware of API rate limits
- Temperature affects creativity: higher values (0.8-1.2) for more creative outputs, lower values (0.2-0.5) for more focused responses

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md)

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License

---

<a name="chinese"></a>
# ComfyUI xAI (Grok) 扩展

ComfyUI的xAI扩展，支持Grok系列模型的对话和视觉理解功能，提供统一的接口和简单的配置方式。

![节点预览](examples/screenshot06.png)

## ✨ 功能特点

- 🤖 支持 xAI Grok 聊天模型
- 🎯 xAI Grok Vision 图像理解功能
- 🔄 动态切换不同的 Grok 模型
- 🌐 支持中英文双语界面
- ⚙️ 通过 YAML 文件简单配置
- 📋 多种提示词模板，适用于不同场景

## 📦 安装方法

1. 进入ComfyUI的custom_nodes目录
```bash
cd ComfyUI/custom_nodes
```

2. 克隆仓库并切换到xai分支
```bash
git clone https://github.com/leoleexh/ComfyUI-LLMs
cd ComfyUI-LLMs
git checkout xai
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## ⚙️ 配置说明

### 基本配置

1. 复制配置文件模板
```bash
cp settings.yaml.sample settings.yaml
```

2. 编辑 `settings.yaml` 文件，配置您的 xAI API 密钥

### 获取 xAI API 密钥

1. 访问 https://console.x.ai/
2. 注册或登录您的 xAI 账户
3. 导航到 API Keys 部分
4. 创建新的 API 密钥
5. 将 API 密钥复制到您的 `settings.yaml`

### 配置验证

配置完成后，可以使用验证工具检查配置：

```bash
python validate_config.py
```

该工具将：
- ✅ 检查 `settings.yaml` 是否存在
- ✅ 验证配置文件结构
- ✅ 显示当前的 API 端点和模型配置
- ⚠️ 警告需要更新的默认 API 密钥

### 详细配置说明

```yaml
chatllmleoleexh:
  # xAI API 配置
  openai_compatible:
    default:
      api_base: "https://api.x.ai/v1/chat/completions"
      organisation: "NONE"
      api_key: "your-xai-api-key-here"
      model:
        - "grok-4-0709"
        - "grok-4"
        - "grok-3"
        # ... 更多模型

  # xAI 视觉模型配置
  vision_models:
    xai:
      api_key: "your-xai-api-key-here"
      api_base: "https://api.x.ai/v1/responses"
      model_list:
        - "grok-4-0709"
        - "grok-4"
        # ... 更多模型

  # 提示词模板配置
  prompt_templates:
    default:
      system: "You are Grok, an AI assistant..."
      prefix: ""
      suffix: ""
```

### 支持的模型

#### 聊天模型
- grok-4-0709
- grok-4
- grok-3
- grok-3-mini
- grok-3-fast
- grok-4-1-fast-non-reasoning
- grok-4-1-fast-reasoning
- grok-4-fast-non-reasoning
- grok-4-fast-reasoning

#### 视觉模型
- grok-2-vision-1212
- grok-4 (支持视觉功能)
- grok-3 (支持视觉功能)

### 提示词模板

扩展包含多个预配置的提示词模板：

1. **default**: 通用 AI 助手
2. **image_generator**: 用于生成详细的图像提示词
3. **creative_writer**: 用于创意写作任务
4. **code_assistant**: 用于编程和代码相关任务
5. **chinese_assistant**: 用于中文语言交互

您可以在 `settings.yaml` 中自定义这些模板，或直接在节点的 system_prompt 字段中使用。

## 🎯 使用方法

### 聊天功能

1. 在节点列表中找到 `🤖 Grok Chat | 智能对话`（位于 🚀 xAI 分类下）
2. 配置模型参数：
   - 选择 API 配置（default）
   - 选择 Grok 模型
   - 设置系统提示词（或使用默认值）
   - 输入用户提示词
   - 调整 temperature (0.0-2.0) 和 top_p (0.001-1.0)
   - 设置 max_tokens（可选，默认 4096）
3. 运行节点获取响应

### 图像理解功能

1. 在节点列表中找到 `🎯 Grok Vision | 图像理解`（位于 🚀 xAI 分类下）
2. 配置参数：
   - 从 ComfyUI 连接图像输入
   - 选择模型类型（xai）
   - 选择具体的 Grok 视觉模型
   - 输入描述提示词
3. 运行节点获取图像描述

## 📝 注意事项

- 请确保 xAI API 密钥配置正确
- 不同模型可能有不同的功能和定价
- 建议使用稳定的网络环境
- 注意 API 调用频率限制
- Temperature 参数影响输出创造性：较高值（0.8-1.2）用于更创意的输出，较低值（0.2-0.5）用于更聚焦的响应

## 🔄 更新日志

详见 [CHANGELOG.md](CHANGELOG.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
