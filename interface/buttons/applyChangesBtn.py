import customtkinter as ctk
from config import app_config
from interface.widgets.icons import arrow_down_icon
class ApplyChangesBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, image=arrow_down_icon)
        self.configure(
            command=command,
            text="Apply changes",
            fg_color=app_config['theme']['secondary_color'][0],
            bg_color=app_config['theme']['secondary_color'][0], 
            border_width=2,
            corner_radius=5, 
            border_color="#0320fc", 
            hover_color="#0320fc",
            **kwargs,
        )
        self.pack(anchor='center')