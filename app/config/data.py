import json
from pathlib import Path
from app.config.set_config import DATA_FILE


class DataManager():

    def _load_data(self):
        with open(Path(DATA_FILE), "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
        
    def _reload(self):
        self._data = self._load_data()

    def add_data(self, key, value):
        with open(Path(DATA_FILE), "r", encoding="utf-8") as f:
            data = json.load(f)

        if not key in data: data[key] = []
        data[key].append(value)
        
        with open(Path(DATA_FILE), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        self._reload()
    
    def get(self, key = None):
        if key:
            if key in self._data: return self._data[key]
        return self._data
    

    
app_data = DataManager()