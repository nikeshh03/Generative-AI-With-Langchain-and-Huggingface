
#This code is not recommended since its outdated because LLM is used here but in latest versions we use chat models over llms

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1"
)

result = llm.invoke("What is the capital of India")

print(result)