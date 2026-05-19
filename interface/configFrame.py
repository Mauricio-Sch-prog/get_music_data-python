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
                        corner_radius=5,
                        )

        self.label = ctk.CTkLabel(
            self,
            text="Config",
            fg_color= app_config.get(section='theme', key='accent_color')
        )

        self.slider_label = ctk.CTkLabel(self, text="Batch fetch per api request")
        self.theme_label = ctk.CTkLabel(self, text="Theme")
        self.system_theme_label = ctk.CTkLabel(self, text="Use system's theme")
        self.api_key_label = ctk.CTkLabel(self, text="API KEY")


        self.slider = Slider(
            master=self,
            steps=None,
            set=app_config.get(section='system', key='api_batch_fetch')
        )
 

        self.toggle_theme_btn = ThemeToggleBtn(
            self,
            callback=self._toggle_theme,
        )

        self.system_theme_switch = SwitchBtn(
            master=self,
            callback=self._switch_system_theme,
            set=app_config.get(section="system", key="system_theme"),
        )

        self.api_key_input = TextInput(
            master=self,
            placeholder="Place here your gemini api key",
            set=app_config.get(section="system", key="api_key")
        )


        self.apply_changes_btn = ApplyChangesBtn(
            master=self,
            command=self._apply_changes,
            fg_color = app_config.get(section="theme", key="accent_color"),
            bg_color = app_config.get(section="theme", key="accent_color"),
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.label.grid(row=0, column=0, columnspan=2, pady=15)

        self.slider_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.slider.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.theme_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.toggle_theme_btn.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.system_theme_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.system_theme_switch.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        self.api_key_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.api_key_input.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        self.apply_changes_btn.grid(row=5, column=0, columnspan=2, pady=15)


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
        ctk.set_appearance_mode(app_config.adjust_system_theme())

    def get(self):
        return self.toggle_theme_btn.get()


        




    