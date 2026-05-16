import customtkinter as ctk
from PIL import Image
from pathlib import Path

# 1. Get the directory where THIS file (icons.py) is located
# .parent.parent moves up to the project root or the level where 'icons' folder lives
BASE_DIR = Path(__file__).resolve().parent.parent.parent 
ICON_DIR = BASE_DIR / "icons"

# 2. Use the / operator (pathlib magic) to join paths
config_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "settings-light.png"),
    dark_image=Image.open(ICON_DIR / "settings-dark.png"),
    size=(24, 24),
)

folder_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "folder-search-light.png"),
    dark_image=Image.open(ICON_DIR / "folder-search-dark.png"),
    size=(24, 24),
)

close_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "circle-x-light.png"),
    dark_image=Image.open(ICON_DIR / "circle-x-dark.png"),
    size=(24, 24),
)

arrow_right_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "circle-arrow-right-light.png"),
    dark_image=Image.open(ICON_DIR / "circle-arrow-right-dark.png"),
    size=(24, 24),
)

arrow_down_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "arrow-big-down-dash-light.png"),
    dark_image=Image.open(ICON_DIR / "arrow-big-down-dash-dark.png"),
    size=(24, 24),
)

x_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "x-light.png"),
    dark_image=Image.open(ICON_DIR / "x-dark.png"),
    size=(16, 16),
)

check_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "check-light.png"),
    dark_image=Image.open(ICON_DIR / "check-dark.png"),
    size=(16, 16),
)

theme_toggle_icon = ctk.CTkImage(
    light_image=Image.open(ICON_DIR / "theme_toggle_off.png"),
    dark_image=Image.open(ICON_DIR / "theme_toggle_on.png"),
    size=(24, 24),
)
