#导入需要的包
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

#1.加载本地deepseek模型
llm = OllamaLLM(model="deepseek-r1:1.5b")

#2.定义提示词模板，{question}是变量，后面可以替换
prompt_template = PromptTemplate(
    input_variables=["qestion"],
    template="""
    请回答用户问题，**只输出JSON，不要多余文字、不要解释**。
    JSON包含两个字段：
    "answer": 答案文本
    "confidence": 0~1之间的可信度数字
    用户问题：{question}
    """
)

#3.填充变量
my_prompt=prompt_template.format(question="什么是勾股定理？")

#4.发给大模型，拿到返回结果
result = llm.invoke(my_prompt)
#打印输出
print(result)