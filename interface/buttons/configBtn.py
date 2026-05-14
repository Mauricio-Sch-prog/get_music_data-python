import customtkinter as ctk
from interface.configFrame import ConfigFrame
from interface.widgets.icons import config_icon
from config import app_config

class ConfigBtn(ctk.CTkButton):
    def __init__(self, master : ctk.CTk , load = None, **kwargs):
        super().__init__(master,
                         image=config_icon,
                         )
        self.state = False
        self.load = load
        self.configFrame = ConfigFrame(master)
        self.configure(
            command=self._toggle_config,
            text=None,
            fg_color=app_config['theme']['secondary_color'][0],
            bg_color=app_config['theme']['secondary_color'][0],
            corner_radius=5, 
            hover_color=app_config['theme']['accent_color'][0],
            width=40,
            height=40,
            anchor="center",
            compound="center",   
            border_spacing=0,
            **kwargs
        )

    def _toggle_config(self):
        self.state = not self.state
        if self.state:
            for widget in self.master.winfo_children():
                if widget == self:
                    continue
                widget.pack_forget()
            self.configFrame.pack(fill="both", expand=True, padx=10, pady=10)
        else:
            self.configFrame.pack_forget()
            self.load()





