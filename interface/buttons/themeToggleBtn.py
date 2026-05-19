import customtkinter as ctk
from interface.widgets.icons import theme_toggle_icon
from config import app_config

class ThemeToggleBtn(ctk.CTkFrame):
    def __init__(self,  master, text="", callback = None, **kwargs):
        super().__init__(
            master,
            fg_color=app_config.get(section='theme', key='accent_color'),
            bg_color=app_config.get(section='theme', key='accent_color'),
            **kwargs,
            )
            
        self.icon = ctk.CTkLabel(
            self,
            text="",
            image=theme_toggle_icon,
        )

        self.callback = callback

        self.switch_var = ctk.StringVar(value=ctk.get_appearance_mode())

        self.label = ctk.CTkLabel(
            self,
            text=text,
        )

        self.switch = ctk.CTkSwitch(
            master=self,
            text="",
            button_color=app_config.get(section='theme', key='text_color'),
            progress_color=app_config.get(section='theme', key='success_color'),
            button_hover_color="#a5a5a5",
            variable=self.switch_var,
            onvalue="dark", 
            offvalue="light",
            command=self._on_toggle
        )

        if self.switch_var.get() == 'Dark':
            self.switch.select()
 
        self.switch.pack(side="left")
        self.icon.pack(side="right")


    def _on_toggle(self):
        if(self.callback):
            self.callback()

    def get(self):
        return self.switch_var.get()