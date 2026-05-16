import json
import os
from datetime import datetime
from config import Config

class NoteManager:
    def __init__(self):
        self._init_db()
        self.notes = self._load_notes()

    def _init_db(self):
        if not os.path.exists(Config.DB_PATH):
            os.makedirs(Config.DB_PATH)
        if not os.path.exists(Config.NOTES_PATH):
            with open(Config.NOTES_PATH, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load_notes(self):
        with open(Config.NOTES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_notes(self):
        with open(Config.NOTES_PATH, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, content, tags=None):
        note = {
            "id": len(self.notes) + 1,
            "content": content,
            "tags": tags or [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        self._save_notes()
        return note["id"]

    def delete_note(self, note_id):
        original_len = len(self.notes)
        self.notes = [n for n in self.notes if n["id"] != note_id]
        if len(self.notes) < original_len:
            self._save_notes()
            return True
        return False

    def get_note(self, note_id):
        return next((n for n in self.notes if n["id"] == note_id), None)

    def list_notes(self):
        return sorted(self.notes, key=lambda x: x["created_at"], reverse=True)
