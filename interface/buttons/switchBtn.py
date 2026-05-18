import customtkinter as ctk
from config import app_config

class SwitchBtn(ctk.CTkFrame):
    def __init__(self, master, text, callback = None, set = False, **kwargs):
        super().__init__(
            master,
            **kwargs
        )

        self.switch_var = ctk.BooleanVar(self, set)

        self.label = ctk.CTkLabel(
            self,
            text=text,
        )

        self.switch = ctk.CTkSwitch(
            self,
            text="",
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
