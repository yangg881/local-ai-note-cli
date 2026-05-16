import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    EMBEDDING_MODEL = "text-embedding-3-small"
    DB_PATH = os.path.expanduser("~/.local-ai-note")
    INDEX_PATH = os.path.join(Config.DB_PATH, "index.faiss")
    NOTES_PATH = os.path.join(Config.DB_PATH, "notes.json")
