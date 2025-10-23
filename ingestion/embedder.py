import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import List

class GeminiEmbeddingFunction:
    
    def __init__(self, model_name: str="gemini-embedding-001"):
        load_dotenv()
        self.model_name = model_name
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environement variable does not exist.")
    
        genai.configure(api_key=api_key)
    
    def __call__(self, texts: List[str]) -> List[List[float]]:

        if not texts:
            return[]
        
        result = genai.embed_content(
            model=self.model_name,
            content=texts,
            task_type="retrieval_document"
        )
    
        return result['embedding']