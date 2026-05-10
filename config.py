import tomllib
import os

CONFIG_PATH = "config.toml"

def load_settings():
    if not os.path.exists(CONFIG_PATH):

        return {"theme": {"primary_color": "#1f538d"}, "system": {"language": "en"}}
    
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)

app_config = load_settings()