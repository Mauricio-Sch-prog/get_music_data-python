import customtkinter as ctk

from app.config.config import app_config
from app.config.language_settings import language_settings

from app.interface.components.buttons.apply_changes_btn import ApplyChangesBtn
from app.interface.components.inputs.theme_toggle_btn import ThemeToggleBtn
from app.interface.components.inputs.switch_btn import SwitchBtn
from app.interface.components.inputs.text_input import TextInput
from app.interface.components.inputs.slider_input import SliderInput
from app.interface.components.inputs.options_input import OptionsInput
 
class ConfigView(ctk.CTkFrame):
    def __init__(self, master, on_close_request):
        super().__init__(master, 
                        fg_color=app_config.get(section='theme', key='accent_color'),
                        bg_color=app_config.get(section='theme', key='accent_color'),
                        corner_radius=5,
                        )
        
        self.on_close = on_close_request

        self.label = ctk.CTkLabel(
            self,
            text=_("Config"),
            fg_color= app_config.get(section='theme', key='accent_color')
        )

        self.slider_label = ctk.CTkLabel(self, text=_("Batch fetch per api request"))
        self.theme_label = ctk.CTkLabel(self, text=_("Theme"))
        self.system_theme_label = ctk.CTkLabel(self, text=_("Use system's theme"))
        self.select_language_label = ctk.CTkLabel(self, text=_("Language"))
        self.api_key_label = ctk.CTkLabel(self, text=_("API KEY"))


        self.slider = SliderInput(
            master=self,
            steps=None,
            range=[1,100],
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

        self.language_select = OptionsInput(
            self,
            options={
                "en" : "English", 
                "es" : "Spanish",
                },
            callback=self._on_language_change,
            preset=app_config.get(section="system", key="language")
        )

        self.api_key_input = TextInput(
            master=self,
            placeholder=_("Place here your gemini api key"),
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

        self.select_language_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.language_select.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        self.api_key_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.api_key_input.grid(row=5, column=1, sticky="w", padx=10, pady=5)


        self.apply_changes_btn.grid(row=6, column=0, columnspan=2, pady=15)

        self.bind("<Unmap>", self.adjust_buttons)


    def _toggle_theme(self):
        app_config.edit_system_config(key="theme", value=self.toggle_theme_btn.get())
        ctk.set_appearance_mode(app_config.adjust_system_theme())

    def _switch_system_theme(self):
        app_config.edit_system_config(key="system_theme", value=self.system_theme_switch.get())
        ctk.set_appearance_mode(app_config.adjust_system_theme())
        
    def _on_language_change(self, value):
        language_settings.change_language(value)
        self.update_gui()
        return

    def _apply_changes(self):
        app_config.edit_system_config("api_batch_fetch", self.slider.get())
        app_config.edit_system_config("api_key", self.api_key_input.get())
        app_config.edit_system_config("language", self.language_select.get())
        ctk.set_appearance_mode(app_config.adjust_system_theme())
        self.on_close()

    
    def adjust_buttons(self, event = None):
        self.slider.slider.set(app_config.get(section="system", key="api_batch_fetch"))
        self.slider._update_text(self.slider.slider_var)
        self.api_key_input.input_var.set(app_config.get(section="system", key="api_key"))
        self.language_select.set(app_config.get(section="system", key="language"))
        self._on_language_change(app_config.get(section="system", key="language"))

        return
    
    def update_gui(self):
        self.label.configure(text=_("Config"))
        self.slider_label.configure(text=_("Batch fetch per api request"))
        self.theme_label.configure(text=_("Theme"))
        self.system_theme_label.configure(text=_("Use system's theme"))
        self.api_key_label.configure(text=_("API KEY"))
        self.api_key_input.input.configure(placeholder_text=_("Place here your gemini api key"))
        self.apply_changes_btn.configure(text=_("Apply changes"))
