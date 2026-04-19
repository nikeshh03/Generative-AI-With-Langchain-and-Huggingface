from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "summarize the following text \n {text}",
    input_variables=['text']
)

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>=500 , RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()   
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic':'Machine Learning vs Deep Learning'})

print(result)