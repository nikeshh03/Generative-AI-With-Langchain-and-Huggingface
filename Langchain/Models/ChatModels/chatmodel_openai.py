from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                temperature= 1.8, 
                max_completion_tokens=10,
                base_url = 'https://openrouter.ai/api/v1'
)

result = chat_model.invoke("write a 5 line poem on cricket")
print(result.content)