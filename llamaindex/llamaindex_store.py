from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

# Load the text file
with open("../resource/data_sample.txt", "r") as file:
    text = file.read()

# Create a document
document = Document(text)

# Create an index from the document
index = GPTVectorStoreIndex.from_documents([document])

# Query the index
query_engine = index.as_query_engine()
response = query_engine.query("我叫什么?来自哪里?")
print(response)
