import customtkinter as ctk

from app.config.config import app_config


class BtnModel(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        defaults = {
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "text_color":app_config.get(section='theme', key='text_color'),
            "border_width":2,
            "corner_radius":5,
        }
        defaults.update(kwargs)
        super().__init__(
            master, 
            **defaults
            )
    
    def on_click(self, text = None):
        self.configure(
            text=text,
            state="disabled",
            )
        
    def on_click_end(self, text = None):
        self.configure(
            text=text,
            state="normal",
            )
    
    def update_text(self, text):
        self.text = text
    

