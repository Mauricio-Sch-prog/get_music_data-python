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

        data.setdefault(key, [])

        data[key].append(value)
        
        with open(Path(DATA_FILE), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        self._reload()

    def update_by_id(self, key, id, value):
        with open(Path(DATA_FILE), "r", encoding="utf-8") as f:
            data = json.load(f)

        if key not in data: 
            data[key] = {}

        if str(id) in data[key]:
            data[key][str(id)].update(value)
        else:
            data[key][str(id)] = value
        

        with open(Path(DATA_FILE), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        self._reload()
    
    def remove_by_id(self, key, id):
        with open(Path(DATA_FILE), "r", encoding="utf-8") as f:
            data = json.load(f)

        if key in data and str(id) in data[key]:
            data[key].pop(str(id))

        with open(Path(DATA_FILE), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        self._reload()

    def get(self, key = None):
        if key and key in self._data:
            return self._data[key]
        return self._data
    

    
app_data = DataManager()