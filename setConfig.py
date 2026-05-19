from pathlib import Path
from config import app_config

CONFIG_FILE = Path("config.toml")

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
pre_set_theme = 'dark'
api_batch_fetch = 12
api_key = "AIzaSyAUSlpO98ubEqlSma-W2emRjMHathAS2ac"
"""

def init_config():
    config_file = Path("config.toml")
    if not config_file.exists():
        with open(config_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG) 
        print("Config file written and saved to disk.")
    app_config._reload()
