# AI Pipeline for Discord Bot

RAG-based system that embeds Discord messages and retrieves similar past conversations to answer repeated questions.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `keys.env` file:
```
GOOGLE_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

3. Run the API:
```bash
python main.py
```

## Project Structure

- `ingestion/` - Message embedding and storage
- `retrieval/` - Similarity search logic
- `agent/` - LangGraph agent
- `api/` - REST endpoints for Discord bot
- `data/chroma_db/` - Vector database (not in git)

## API Endpoints

**POST /ingest** - Add message to vector store
**POST /query** - Find similar messages and get response

## How It Works

1. Discord messages get embedded and stored in Chroma
2. New message → find most similar past messages
3. Return the answer that was given before
4. LangGraph agent decides when to use similarity vs. generate new response