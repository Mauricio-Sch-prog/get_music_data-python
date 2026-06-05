import customtkinter as ctk

from app.config.config import app_config


class SliderInput(ctk.CTkFrame):
    def __init__(self, master, text="", steps = 1, callback = None, range = [0, 100], set = 0, **kwargs):
        super().__init__(
            master,
            fg_color=app_config.get(section='theme', key='accent_color'),
            bg_color=app_config.get(section='theme', key='accent_color'),
            **kwargs,
            )

        self.callback = callback
        self.slider_var = ctk.Variable(value=set)

        self.label = ctk.CTkLabel(
            self,
            text=text,
        )

        self.number_label = ctk.CTkLabel(
            self,
            text=int(self.slider_var.get())
        )

        self.slider = ctk.CTkSlider(
            self,
            from_=range[0],
            to=range[1],
            number_of_steps = steps,
            button_color=app_config.get(section='theme', key='text_color'),
            progress_color=app_config.get(section='theme', key='success_color'),
            button_hover_color="#a5a5a5",
            variable=self.slider_var,
            command=self._update_text,
        )
        self.label.pack(side="left")
        self.number_label.pack(side="left")
        self.slider.pack(side="right")
    
    def _update_text(self, val):
        self.number_label.configure(text=int(self.slider_var.get()))
        if(self.callback):
            self.callback()
    
    def get(self):
        return int(self.slider_var.get())
    
