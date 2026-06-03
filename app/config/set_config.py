from pathlib import Path
import json
import sys


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent


CONFIG_FILE = BASE_DIR / "config.toml"
DATA_FILE = BASE_DIR / "data.json"
LANGUAGE_LOCALE = BASE_DIR / "locales"

DEFAULT_CONFIG = """# Application Configuration File

[theme]
primary_color = ["#6347d1","#7b5bf2"]
secondary_color = ["#ffffff","#1b1d26"]
accent_color = ["#f4f4f9","#242732"]
text_color = ["#1a1a1b","#ffffff"]
success_color = ["#5236b8","#2ecc71"]
list_primary_color = "#252525"
list_secondary_color = "#333333"


[system]
language = "en"
system_theme = true
theme = "dark"
api_batch_fetch = 10
api_key = ""
"""

default_data = {"unchanged_processes": []}

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


