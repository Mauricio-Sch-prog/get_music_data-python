import customtkinter as ctk
from config import app_config
from interface.buttons.sliderFrame import Slider
from interface.buttons.applyChangesBtn import ApplyChangesBtn
from interface.buttons.themeToggleBtn import ThemeToggleBtn

class ConfigFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, 
                        fg_color=app_config.get(section='theme', key='accent_color'),
                        bg_color=app_config.get(section='theme', key='accent_color'),
                        corner_radius=5
                        )

        self.label = ctk.CTkLabel(
            self,
            text="Config",
            anchor="n",
            fg_color= app_config.get(section='theme', key='accent_color')
        )
        self.label.pack(side="top", pady=15)

        self.slider = Slider(
            master=self,
            steps=None,
            set=app_config.get(section='system', key='api_batch_fetch')
        )
        self.slider.pack(anchor="center")

        self.toggle_theme_btn = ThemeToggleBtn(
            self,
            self._toggle_theme
        )
        self.toggle_theme_btn.pack(anchor="center")



        self.apply_changes_btn = ApplyChangesBtn(
            master=self,
            command=self._apply_changes,
        )
        self.apply_changes_btn.pack(anchor="center")


    def _toggle_theme(self):
        ctk.set_appearance_mode(self.toggle_theme_btn.get())

    def _apply_changes(self):
        app_config.edit_system_config("api_batch_fetch", self.slider.get())
        ctk.set_appearance_mode(app_config.get(section='system', key='theme'))

    def get(self):
        return self.toggle_theme_btn.get()

    def adjust(self):
        self.slider.slider_var.set(app_config.get(section='system', key='api_batch_fetch'))
        self.slider._update_text(0)
        




    