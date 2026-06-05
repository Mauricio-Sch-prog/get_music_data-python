import customtkinter as ctk

from app.config.config import app_config


class SwitchBtn(ctk.CTkFrame):
    def __init__(self, master, text = "", callback = None, set = False, **kwargs):
        super().__init__(
            master,
            fg_color=app_config.get(section='theme', key='accent_color'),
            bg_color=app_config.get(section='theme', key='accent_color'),
            **kwargs,
            )

        self.switch_var = ctk.BooleanVar(self, set)

        self.label = ctk.CTkLabel(
            self,
            text=text,
        )

        self.switch = ctk.CTkSwitch(
            self,
            text="",
            button_color=app_config.get(section='theme', key='text_color'),
            progress_color=app_config.get(section='theme', key='success_color'),
            button_hover_color="#a5a5a5",
            variable=self.switch_var,
            onvalue=True, 
            offvalue=False,
            command=callback,
        )

        if self.switch_var.get():
            self.switch.select()

        self.label.pack(side="left")
        self.switch.pack(side="right")

    def get(self):
        return self.switch_var.get()
