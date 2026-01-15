# Changelog

## [2.0.0] - xAI Branch - 2024-01-15

### 🚀 主要更新
- 专门针对 xAI Grok 模型优化
- 完全移除 OpenAI 客户端依赖，直接使用 xAI API
- 移除了其他第三方模型支持（GLM4、阿里、Gemini）
- 大幅简化代码结构和依赖

### ✨ 新功能
- 新增 `xai_client.py` 直接调用 xAI API
- 新增 `LLMs_Vision_XAI.py` 专门处理 xAI 视觉模型
- 优化了 `LLMs_Chat.py` 针对 Grok 模型的默认配置
- 新增多种提示词模板（default、image_generator、creative_writer、code_assistant、chinese_assistant）
- 添加 `max_tokens` 参数支持

### 🔧 优化
- 完全移除 OpenAI SDK 依赖
- 使用原生 requests 库直接调用 xAI API
- 简化配置文件结构，只保留 xAI 相关配置
- 移除 `api_base` 配置项（xAI 使用固定端点）
- 更新节点分类为 "🚀 xAI"
- 更新节点显示名称为 "🤖 Grok Chat | 智能对话" 和 "🎯 Grok Vision | 图像理解"
- 优化默认 temperature 参数为 0.7（更适合 Grok）

### 📝 配置变更
- 移除 `api_base` 和 `organisation` 配置项
- 只需配置 `api_key` 即可
- 支持的模型列表更新为 Grok 系列模型
- 新增 5 个预配置的提示词模板

### 🗑️ 移除
- 移除 `openai_client.py`（OpenAI 客户端）
- 移除 `LLMs_Vision_OpenAI.py`
- 移除 `LLMs_Vison_GLM4.py`
- 移除 `LLMs_Vison_Ali.py`
- 移除 `LLMs_Vison_Gemini.py`
- 移除 `comfyui_llms_wrapper.py`
- 移除 openai、zhipuai、dashscope、google-generativeai 依赖
- 只保留 requests、Pillow、PyYAML 依赖

### 🐛 修复
- 修复配置验证工具的提示信息
- 优化错误处理机制
- 修复 API 响应解析逻辑

## [1.0.0] - 2024-01-11

### 🎯 主要更新
- 重构了整个项目结构，提供更统一和简洁的使用体验
- 新增统一的视觉模型节点，支持多种LLM模型
- 优化了节点UI和提示语设计

### ✨ 新功能
- 新增 `LLMs Vision Unified` 节点，支持：
  - OpenAI GPT-4V
  - 智谱 GLM-4V
  - 阿里 通义千问
  - Google Gemini
- 支持动态模型选择和切换
- 改进的图像分析提示语，提供更详细的图像描述

### 🔧 优化
- 简化了配置文件结构
- 优化了节点分类和显示名称
- 改进了错误处理和提示信息
- 统一了API调用接口

### 🎨 界面改进
- 添加了更直观的emoji图标
- 优化了节点分组和分类
- 添加了中英文双语显示

### 📝 配置变更
- 更新了配置文件格式，支持多模型配置
- 简化了API密钥配置方式
- 统一了视觉模型的配置结构

### 🗑️ 移除
- 移除了单独的模型节点，统一使用 `LLMs Vision Unified`
- 移除了冗余的配置选项

### 🐛 修复
- 修复了模型切换时的显示问题
- 修复了配置文件加载的问题
- 改进了错误处理机制

## [0.0.1] - 2023-12-20
- 初始版本发布
