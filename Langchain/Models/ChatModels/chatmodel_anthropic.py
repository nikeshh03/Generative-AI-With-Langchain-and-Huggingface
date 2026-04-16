from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(
    model = 'anthropic/claude-opus-4.6-fast',
    #base_url = 'https://openrouter.ai/api/v1' #only for openrouter not for official API provider
)

result = chat_model.invoke("Write me a poem on charger")

print(result.content)