from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'models/gemini-2.5-flash'

)

result = model.invoke("write a poem on cricket")

print(result.content)