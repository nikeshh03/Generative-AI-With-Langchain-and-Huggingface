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

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variable = ['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1 , model, parser, prompt2, model, parser)

result = chain.invoke({'topic','AI'})

print(result)