import customtkinter as ctk
from config import app_config

class TextInput(ctk.CTkFrame):
    def __init__(self, master, text = "", placeholder = None, set = None, **kwargs):
        super().__init__(
            master,
            fg_color=app_config.get(section='theme', key='accent_color'),
            bg_color=app_config.get(section='theme', key='accent_color'),
            **kwargs,
            )
        
        self.input_var = ctk.StringVar(self, value=set)

        self.label = ctk.CTkLabel(
            self,
            text=text,
            text_color= app_config.get(section="theme", key="text_color"),
            bg_color= app_config.get(section="theme", key="secondary_color"),
            fg_color= app_config.get(section="theme", key="secondary_color"),
        )

        self.input = ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            textvariable=self.input_var
        )
  
        

        self.label.pack(side="left")
        self.input.pack(side="right")

    def get(self):
        return self.input.get()