import customtkinter as ctk
from interface.widgets.icons import theme_toggle_icon

class ThemeToggleBtn(ctk.CTkFrame):
    def __init__(self, master, callback : None):
        super().__init__(master)
        self.icon = ctk.CTkLabel(
            self,
            text="",
            image=theme_toggle_icon,
        )
        self.icon.pack(side="left")

        self.callback = callback

        self.switch_var = ctk.StringVar(value=ctk.get_appearance_mode())

        self.switch = ctk.CTkSwitch(
            master=self,
            text="",
            variable=self.switch_var,
            onvalue="dark", 
            offvalue="light",
            command=self._on_toggle
        )

        if(self.switch_var.get() == 'Dark'):
            self.switch.select()

        self.switch.pack(side="right")


    def _on_toggle(self):
        if(self.callback):
            self.callback()

    def get(self):
        return self.switch_var.get()