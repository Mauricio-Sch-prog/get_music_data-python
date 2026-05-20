import customtkinter as ctk
from interface.configFrame import ConfigFrame
from interface.widgets.icons import config_icon
from config import app_config

class ConfigBtn(ctk.CTkButton):
    def __init__(self, master : ctk.CTk , load = None, **kwargs):
        super().__init__(master,
                         image=config_icon,
                         )
        self.load = load
        self.config_frame = ConfigFrame(master)
        self.config_frame.state = False
        self.configure(
            command=self._toggle_config,
            text=None,
            fg_color=app_config.get(section='theme', key='secondary_color'),
            bg_color=app_config.get(section='theme', key='secondary_color'),
            text_color=app_config.get(section='theme', key='text_color'),
            corner_radius=5, 
            hover_color=app_config.get(section='theme', key='accent_color'),
            width=40,
            height=40,
            anchor="center",
            compound="center",   
            border_spacing=0,
            **kwargs
        )

    def _toggle_config(self):
        self.config_frame.state = not self.config_frame.state
        if self.config_frame.state:
            self.config_frame.adjust_buttons()
            self.config_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)
            self.config_frame.lift()

        else:
            self.config_frame.place_forget()





