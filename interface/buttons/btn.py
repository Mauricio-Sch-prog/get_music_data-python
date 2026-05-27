import customtkinter as ctk
from config.config import app_config

class Btn(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master, 
            fg_color=kwargs.get('fg_color', app_config.get(section='theme', key='secondary_color')),
            bg_color=kwargs.get('bg_color', app_config.get(section='theme', key='secondary_color')),
            text_color=app_config.get(section='theme', key='text_color'),
            border_width=2,
            corner_radius=5,
            border_color="#0320fc",
            hover_color="#0320fc",
            )
        self.configure(
            **kwargs
        )

    def update_gui(self, text):
        self.configure(text=text)