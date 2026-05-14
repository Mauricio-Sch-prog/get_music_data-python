import customtkinter as ctk
from config import app_config
from interface.widgets.icons import arrow_right_icon
class GetDataBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, image=arrow_right_icon)
        self.configure(
            command=command,
            text="Get data",
            fg_color=app_config['theme']['secondary_color'][0],
            bg_color=app_config['theme']['secondary_color'][0], 
            border_width=2,
            corner_radius=5, 
            border_color=app_config['theme']['success_color'][0], 
            hover_color=app_config['theme']['success_color'][0],
            anchor="center",
            # border_spacing=10,
            # compound="center",
            **kwargs
        )
        self.pack(anchor='center')

