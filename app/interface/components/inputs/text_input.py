import customtkinter as ctk

from app.config.config import app_config


class TextInput(ctk.CTkFrame):
    def __init__(self, master, placeholder = None, set = None, **kwargs):
        super().__init__(
            master,
            bg_color="transparent",
            fg_color="transparent",
            **kwargs,
            )
        
        self.input_var = ctk.StringVar(self, value=set)

        self.input = ctk.CTkEntry(
            self,
            fg_color=app_config.get(section='theme', key='secondary_color'),
            border_width=0,
            placeholder_text=placeholder,
            textvariable=self.input_var
        )
  
        self.input.pack(side="right")

    def get(self):
        return self.input.get()