import json
import sys
from pathlib import Path

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    USER_DATA_DIR = Path(sys.executable).parent
    BASE_DIR = Path(sys._MEIPASS)
else:
    USER_DATA_DIR = Path(__file__).resolve().parent.parent.parent
    BASE_DIR = USER_DATA_DIR

LANGUAGE_LOCALE = BASE_DIR / "locales"

CONFIG_FILE = USER_DATA_DIR / "config.toml"
DATA_FILE = USER_DATA_DIR / "data.json"

DEFAULT_CONFIG = """# Application Configuration File

[theme]
primary_color = ["#5b3cc4", "#7b5bf2"]
secondary_color = ["#f8f9fa", "#1b1d26"]
accent_color = ["#eef0f3", "#242732"]
text_color = ["#212529", "#ffffff"] 
success_color = ["#2ecc71", "#2ecc71"]
list_primary_color = ["#e2e5e9", "#252525"]
list_secondary_color = ["#d1d5db", "#333333"]


[system]
language = "en"
system_theme = true
theme = "dark"
api_batch_fetch = 10
api_key = ""
"""

default_data = {}

def init_config():
    from app.config.config import app_config
    from app.config.data import app_data
    from app.config.language_settings import language_settings
    config_file = Path(CONFIG_FILE)
    if not config_file.exists():
        with open(config_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG) 
        print("Config file written and saved to disk.")

    data_file = Path(DATA_FILE)
    if not data_file.exists():
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)
        print("Data file written and saved to disk.")

    app_config._reload()
    app_data._reload()

    language_settings.change_language()


