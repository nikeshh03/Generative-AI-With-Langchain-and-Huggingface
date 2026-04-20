from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

url = 'https://www.amazon.in/realme-7000mAh-Biggest-Battery-Charging/dp/B0G4BWMQDZ/?_encoding=UTF8&ref_=pd_hp_d_btf_ci_mcx_mr_hp_atf_m'

loader = WebBaseLoader(url)

docs = loader.load()

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

prompt = PromptTemplate(
    template = "answer the following question \n {question} \n based on the following text \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question':'what is the name of product', 'text':docs[0].page_content})

print(result)