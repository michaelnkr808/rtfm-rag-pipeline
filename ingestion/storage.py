import chromadb
import datetime 
from embedder import GeminiEmbeddingFunction

chroma_client = chromadb.PersistentClient(path="./data/chroma_db")

gemini_embed_fn = GeminiEmbeddingFunction()

def get_server_collection(server_id: str) -> chromadb.Collection:

    collection_name = f"discord-server-{server_id}"

    collection = chroma_client.get_or_create_collection(name=f"{collection_name}",
        metadata = {
            "description": f"Discord message collection for Server ID: {server_id}",
            "created" : str(datetime.datetime.now()),
        },
        embedding_function=gemini_embed_fn
    )

    print(f"Accessed collection: {collection.name}")
    return collection