from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()  This loads all the files at once in the memory

docs = loader.lazy_load() # loads the files in the memory as per the call one by one

for document in docs:
    print(document.metadata)