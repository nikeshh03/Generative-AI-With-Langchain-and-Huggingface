from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = TextLoader('text_file.txt', encoding='utf-8')

docs = loader.load()

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

prompt = PromptTemplate(
    template = "write a summary of the following story - \n {story}",
    input_variables=['story']
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'story':docs[0].page_content}))