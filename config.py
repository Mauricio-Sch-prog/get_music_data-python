import tomllib
import tomlkit
import os
import darkdetect

CONFIG_PATH = "config.toml"


def start_settings():
    with open("config.toml", "r") as f:
        config = tomlkit.parse(f.read())
    
    if config['system']['system_theme'] == True:
        print("using system's theme")
        theme = darkdetect.theme().lower()
        
    else:
        theme = config["system"]["pre_set_theme"]
    config["system"]["theme"] = theme

    with open("config.toml", "w") as f:
        f.write(tomlkit.dumps(config))

    return


class ConfigManager():
    def __init__(self):
        self._config = self._load_settings()

    def _load_settings(self):
        if not os.path.exists(CONFIG_PATH):
            return {"theme": {"primary_color": "#1f538d"}, "system": {"language": "en"}}
        
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
    
app_config = ConfigManager()

