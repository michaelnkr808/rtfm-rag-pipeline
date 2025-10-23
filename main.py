from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb

app = FastAPI()
chroma_client = chromadb.Client()

class Message(BaseModel):
    message: str
    author: str | None = None
    channel: str | None = None
    timestamp: str | None = None
    message_id: str

@app.post("/messages")
async def convert_message_to_vector():
    try:
    
    except:
