from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

loader = PyPDFLoader('SQL Notes by Apna College.pdf')

docs = loader.load()

# print(docs)
print(docs[0].metadata)