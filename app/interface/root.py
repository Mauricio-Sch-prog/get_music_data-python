import customtkinter as ctk

from app.config.config import app_config


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode(app_config.adjust_system_theme())
        self.title("Get Your Music Data(AI Powered).")
        self.geometry("800x600")
        self.configure(fg_color=app_config.get(section='theme', key='secondary_color'))

        