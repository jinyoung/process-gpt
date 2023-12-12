import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

from pathlib import Path
from llama_index import download_loader

reader = download_loader("PptxReader")
#reader = download_loader("PDFReader")


loader = reader()

# check if storage already exists
if not os.path.exists("./storage"):
    # load the documents and create the index
    #documents = SimpleDirectoryReader("data").load_data()
    documents = loader.load_data(file=Path('./data/ppt.pptx'))
    #documents = loader.load_data(file=Path('./data/pdf.pdf'))

    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist()
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)



query_engine = index.as_query_engine()
response = query_engine.query("What's the file name in the data directory?")
print(response)

response = query_engine.query("DXez 가 뭐야?")
print(response)