import customtkinter as ctk
from config import app_config
from interface.buttons.sliderFrame import Slider
from interface.buttons.applyChangesBtn import ApplyChangesBtn
from interface.buttons.themeToggleBtn import ThemeToggleBtn
from interface.buttons.switchBtn import SwitchBtn
from interface.buttons.textInput import TextInput

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

        self.slider = Slider(
            master=self,
            steps=None,
            set=app_config.get(section='system', key='api_batch_fetch')
        )

        self.toggle_theme_btn = ThemeToggleBtn(
            self,
            self._toggle_theme
        )

        self.system_theme_switch = SwitchBtn(
            master=self,
            text="Use system's theme",
            callback=self._switch_system_theme,
            set=app_config.get(section="system", key="system_theme"),
        )

        self.api_key_input = TextInput(
            master=self,
            text="API KEY",
            placeholder="Place here your gemini api key",
            set=app_config.get(section="system", key="api_key")
        )


        self.apply_changes_btn = ApplyChangesBtn(
            master=self,
            command=self._apply_changes,
            fg_color = app_config.get(section="theme", key="accent_color"),
            bg_color = app_config.get(section="theme", key="accent_color"),
        )


        self.label.pack(side="top", pady=15)
        self.slider.pack(anchor="center")
        self.toggle_theme_btn.pack(anchor="center")
        self.system_theme_switch.pack(anchor="center")
        self.system_theme_switch.pack(anchor="center")
        self.api_key_input.pack(anchor="center")
        self.apply_changes_btn.pack(anchor="center")


    def _toggle_theme(self):
        app_config.edit_system_config(key="theme", value=self.toggle_theme_btn.get())
        ctk.set_appearance_mode(app_config.adjust_system_theme())
        # ctk.set_appearance_mode(self.toggle_theme_btn.get())

    def _switch_system_theme(self):
        app_config.edit_system_config(key="system_theme", value=self.system_theme_switch.get())
        ctk.set_appearance_mode(app_config.adjust_system_theme())
        

    def _apply_changes(self):
        app_config.edit_system_config("api_batch_fetch", self.slider.get())
        app_config.edit_system_config("api_key", self.api_key_input.get())
        ctk.set_appearance_mode(app_config.get(section='system', key='theme'))

    def get(self):
        return self.toggle_theme_btn.get()

    def adjust(self):
        self.slider.slider_var.set(app_config.get(section='system', key='api_batch_fetch'))
        self.slider._update_text(0)
        




    