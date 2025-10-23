import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

result = genai.embed_content(
    model = "gemini-embedding-001",
    content="What is the meaning of life?",
)

print("Embeddings work!")
print(f"Embedding length: {len(result['embedding'])}")