from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence, RunnableParallel
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI(
                model = 'openai/gpt-4o-mini',
                base_url = 'https://openrouter.ai/api/v1'
)

prompt1 = PromptTemplate(
    template = "Genrate a Linkedin post about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Genrate a tweet about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'linkedin':RunnableSequence(prompt1, model, parser),
    'tweet' : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'types of Machine Learning'})

print(result['linkedin'])
print(result['tweet'])