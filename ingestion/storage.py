import chromadb

chroma_client = chromadb.PersistentClient(path="./data/chroma_db")

collection = chroma_client.create_collection(name="discord-messages")

collection.add(
    documents=["test", "this is another test"]
    metadatas=[{"source": "my_source", "page":1}, {"source": "my_source"}],
    ids=["id1", "id2"]
)
    
results = collection.query(
    query_text["This is a query document"],
    n_results = 2,
    include = ['distance', 'metadata', 'documents']
)

results