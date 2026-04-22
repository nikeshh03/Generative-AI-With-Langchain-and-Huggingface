from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('SQL Notes by Apna College.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[6])