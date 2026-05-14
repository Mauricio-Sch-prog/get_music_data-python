import customtkinter as ctk
from config import app_config
from interface.buttons.sliderFrame import Slider

class ConfigFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, 
                        fg_color=app_config['theme']['accent_color'][0],
                        bg_color=app_config['theme']['accent_color'][0],
                        corner_radius=5
                        )

        self.label = ctk.CTkLabel(
            self,
            text="Config",
            anchor="n",
            fg_color= app_config['theme']['accent_color'][0]
        )
        self.label.pack(side="top", pady=15)

        self.slider = Slider(
            master=self,
            steps=None
        )
        self.slider.pack(anchor="center")


        




    