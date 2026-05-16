import customtkinter as ctk
from config import app_config
from interface.widgets.icons import close_icon

class CloseFolderBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, image=close_icon)
        self.configure(
            command=command,
            text="Close folder",
            fg_color=app_config.get(section='theme', key='secondary_color'),
            text_color=app_config.get(section='theme', key='text_color'),
            border_width=2,
            corner_radius=5, 
            border_color="#fc030b", 
            hover_color="#fc030b",
            **kwargs,
        )