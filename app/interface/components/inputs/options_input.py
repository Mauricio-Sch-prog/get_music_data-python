import customtkinter as ctk

from app.config.config import app_config


class OptionsInput(ctk.CTkFrame):
    def __init__(self, master, options, callback, preset = None):
        super().__init__(
            master
            )
        

        self.callback = callback
        self.options = options
        self.options_display = list(options.values()) 
        self.set_value = preset

        self.select = ctk.CTkOptionMenu(
            self,
            text_color=app_config.get(section='theme', key='text_color'),
            fg_color=app_config.get(section='theme', key='secondary_color'),
            button_color=app_config.get(section='theme', key='success_color'),
            button_hover_color=app_config.get(section='theme', key='primary_color'),
            values=self.options_display,
            command=self._on_select_change,
        )
        if self.set_value:
            self.select.set(self.options[self.set_value])

        self.select.pack(anchor="center")

    def _on_select_change(self, value):
        lang = next((k for k, v in self.options.items() if v == value), None)
        self.set_value = lang
        
        if self.callback:
            self.callback(self.set_value)

    def set(self, value = None):
        if value:
            self.set_value = value
        self.select.set(self.options[self.set_value])
    
    def get(self):
        return self.set_value

    
