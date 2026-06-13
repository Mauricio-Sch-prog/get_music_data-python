import customtkinter as ctk

from app.config.config import app_config


class OptionsInput(ctk.CTkFrame):
    def __init__(self, master, options, callback, preset=None):
        super().__init__(master, fg_color="transparent")

        self.callback = callback
        self.options = options
        self.options_display = list(options.values())
        self.set_value = preset

        self.text_color = app_config.get(section='theme', key='text_color')
        self.bg_color = app_config.get(section='theme', key='secondary_color')
        self.btn_color = app_config.get(section='theme', key='success_color')
        self.hover_color = app_config.get(section='theme', key='primary_color')

        self.dropdown_open = False
        self.dropdown_window = None


        self.menu_button = ctk.CTkButton(
            self,
            text=self.options.get(self.set_value, "Select an option"),
            text_color=self.text_color,
            fg_color=self.bg_color,
            hover_color=self.hover_color,
            command=self._toggle_dropdown
        )
        self.menu_button.pack(anchor="center", fill="both", expand=True)

        self.bind("<FocusOut>", lambda e: self._close_dropdown())

    def _toggle_dropdown(self):
        if self.dropdown_open:
            self._close_dropdown()
        else:
            self._open_dropdown()

    def _open_dropdown(self):
        self.dropdown_open = True
        
        self.dropdown_window = ctk.CTkToplevel(self)
        self.dropdown_window.overrideredirect(True)
        self.dropdown_window.configure(fg_color=self.bg_color)
        

        self.update_idletasks()
        x = self.menu_button.winfo_rootx()
        y = self.menu_button.winfo_rooty() + self.menu_button.winfo_height()
        width = self.menu_button.winfo_width()
   
        row_height = 35
        max_allowed_height = 200
        calculated_height = len(self.options_display) * row_height

        final_height = min(calculated_height, max_allowed_height)
        
        self.dropdown_window.geometry(f"{width}x{final_height}+{x}+{y}")
        self.dropdown_window.attributes("-topmost", True)
        self.dropdown_window.bind("<FocusOut>", lambda e: self._close_dropdown())


        scroll_frame = ctk.CTkScrollableFrame(
            self.dropdown_window,
            fg_color=self.bg_color,
            corner_radius=0,
            label_text="" # No header text
        )
        scroll_frame.pack(fill="both", expand=True, padx=0, pady=0)

        for display_value in self.options_display:
            btn = ctk.CTkButton(
                scroll_frame,
                text=display_value,
                text_color=self.text_color,
                fg_color="transparent",
                hover_color=self.hover_color,
                anchor="w",
                corner_radius=0,
                height=row_height - 5, # Accounting for minor internal padding
                command=lambda val=display_value: self._on_select_change(val)
            )
            btn.pack(fill="x", pady=1)
            
        self.dropdown_window.focus_set()

    def _close_dropdown(self):
        if self.dropdown_window:
            self.dropdown_window.destroy()
            self.dropdown_window = None
        self.dropdown_open = False

    def _on_select_change(self, value):
        lang = next((k for k, v in self.options.items() if v == value), None)
        self.set_value = lang
        
        self.menu_button.configure(text=value)
        self._close_dropdown()
        
        if self.callback:
            self.callback(self.set_value)

    def set(self, value=None):
        if value:
            self.set_value = value
        
        display_text = self.options.get(self.set_value, "Select an option")
        self.menu_button.configure(text=display_text)
    
    def get(self):
        return self.set_value