import faiss
import numpy as np
from openai import OpenAI
from config import Config
from note_manager import NoteManager

client = OpenAI(api_key=Config.OPENAI_API_KEY)

class SearchEngine:
    def __init__(self):
        self.note_manager = NoteManager()
        self.index = self._load_index()

    def _load_index(self):
        if os.path.exists(Config.INDEX_PATH):
            return faiss.read_index(Config.INDEX_PATH)
        return faiss.IndexFlatL2(1536)

    def _save_index(self):
        faiss.write_index(self.index, Config.INDEX_PATH)

    def _get_embedding(self, text):
        response = client.embeddings.create(input=text, model=Config.EMBEDDING_MODEL)
        return np.array(response.data[0].embedding, dtype=np.float32)

    def add_note_to_index(self, note_id, content):
        embedding = self._get_embedding(content)
        self.index.add(np.array([embedding]))
        self._save_index()

    def search_notes(self, query, top_k=5):
        if self.index.ntotal == 0:
            return []
        query_embedding = self._get_embedding(query)
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.note_manager.notes):
                note = self.note_manager.notes[idx]
                results.append({
                    "note": note,
                    "distance": float(distances[0][i])
                })
        return results
