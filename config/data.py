import json
from pathlib import Path
import sys


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

JSON_DIR = BASE_DIR  / "get_music_data-python" / "data.json"

class DataManager():

    def _load_data(self):
        with open(Path(JSON_DIR), "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
        
    def _reload(self):
        self._data = self._load_data()

    def add_data(self, key, value):
        with open(Path(JSON_DIR), "r", encoding="utf-8") as f:
            data = json.load(f)

        if not key in data: data[key] = []
        data[key].append(value)
        
        with open(Path(JSON_DIR), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        self._reload()
    
    def get(self, key = None):
        if key:
            if key in self._data: return self._data[key]
        return self._data
    

    
app_data = DataManager()