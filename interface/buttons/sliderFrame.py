import customtkinter as ctk
from config import app_config
class Slider(ctk.CTkFrame):
    def __init__(self, master, steps = 1, callback = None, range = [0, 100], set = 0):
        super().__init__(master)
        self.configure()

        self.callback = callback
        self.slider_var = ctk.Variable(value=set)
        self.label = ctk.CTkLabel(
            self,
            text=int(self.slider_var.get())
        )

        self.slider = ctk.CTkSlider(
            self,
            from_=range[0],
            to=range[1],
            number_of_steps = steps,
            variable=self.slider_var,
            command=self._update_text,
        )
        self.label.pack(side="left")
        self.slider.pack(side="right")
    
    def _update_text(self, val):
        self.label.configure(text=int(self.slider_var.get()))
        if(self.callback):
            self.callback()
    
    def get(self):
        return int(self.slider_var.get())
