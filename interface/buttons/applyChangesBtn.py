import customtkinter as ctk
from config import app_config
from interface.widgets.icons import arrow_down_icon
class ApplyChangesBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, image=arrow_down_icon)
        self.configure(
            command=command,
            text="Apply changes",
            fg_color=app_config.get(section='theme', key='secondary_color'),
            bg_color=app_config.get(section='theme', key='secondary_color'),
            text_color=app_config.get(section='theme', key='text_color'),
            border_width=2,
            corner_radius=5, 
            border_color="#0320fc", 
            hover_color="#0320fc",
            **kwargs,
        )