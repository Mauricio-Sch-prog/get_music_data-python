import tomllib
import tomlkit

import darkdetect
from pathlib import Path
from app.config.set_config import CONFIG_FILE

class ConfigManager():

    def _load_settings(self):
        with open(Path(CONFIG_FILE), "rb") as f:
            return tomllib.load(f)
        
    def _reload(self):
        self._config = self._load_settings()

        
    def edit_system_config(self, key, value):
        with open(Path(CONFIG_FILE), "r") as f:
            config = tomlkit.parse(f.read())

        config["system"][key] = value

        with open(Path(CONFIG_FILE), "w") as f:
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