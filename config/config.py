import tomllib
import tomlkit

import darkdetect
import sys
from pathlib import Path

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

JSON_DIR = BASE_DIR  / "get_music_data-python" / "data.json"

CONFIG_PATH = "config.toml"

class ConfigManager():

    def _load_settings(self):
        with open(CONFIG_PATH, "rb") as f:
            return tomllib.load(f)
        
    def _reload(self):
        self._config = self._load_settings()

        
    def edit_system_config(self, key, value):
        with open("config.toml", "r") as f:
            config = tomlkit.parse(f.read())

        config["system"][key] = value

        with open("config.toml", "w") as f:
            f.write(tomlkit.dumps(config))

        self._reload()
    
    def get(self, section, key=None):
        if key:
            return self._config.get(section, {}).get(key)
        return self._config.get(section)
    

    def adjust_system_theme(self):
        if self.get(section="system", key="system_theme"):
            theme = darkdetect.theme().lower()
        else:
            theme = self.get(section="system", key="theme")
        return theme

    
app_config = ConfigManager()