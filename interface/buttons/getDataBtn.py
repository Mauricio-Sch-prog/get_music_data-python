import customtkinter as ctk
from config.config import app_config
from interface.icons import arrow_right_icon
class GetDataBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, image=arrow_right_icon)
        self.configure(
            command=command,
            text=_("Get data"),
            fg_color=app_config.get(section='theme', key='secondary_color'),
            bg_color=app_config.get(section='theme', key='secondary_color'),
            text_color=app_config.get(section='theme', key='text_color'),
            border_width=2,
            corner_radius=5, 
            border_color=app_config.get(section='theme', key='success_color'), 
            hover_color=app_config.get(section='theme', key='success_color'),
            anchor="center",
            **kwargs
        )

    def update_gui(self):
        self.configure(text=_("Get data"))

