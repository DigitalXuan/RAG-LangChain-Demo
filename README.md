# LangChain RAG 学习项目
## 项目介绍
本项目使用LangChain搭建RAG检索增强生成应用，包含：
LLM基础调用（智谱GLM-4 ChatZhipuAI）
Prompt模板、LLMChain链式调用
对话记忆系统
文档加载、文本切分、向量库Chroma
Pydantic结构化输出

## 环境
Python >=3.10

### 依赖包
langchain-core==0.2.33
langchain-community
python-dotenv
chromadb
dashscope

## 运行步骤
1. 克隆仓库
2. 在项目根目录新建  .env  文件，填入API密钥

ZHIPUAI_API_KEY="你的智谱key"
DASHSCOPE_API_KEY="你的通义key"

3. 启动Jupyter Notebook运行代码

> 注意事项
> 1. 部分WiFi会出现 APITimeoutError 接口超时，切换手机热点即可解决
> 2. langchain-core固定版本0.2.33，用于兼容旧版ChatZhipuAI
> 3. .gitignore已配置，不会上传密钥和本地BGE大模型权重