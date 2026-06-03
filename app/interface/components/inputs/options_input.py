import customtkinter as ctk

class OptionsInput(ctk.CTkFrame):
    def __init__(self, master, options, callback, preset = None):
        super().__init__(
            master
            )
        

        self.callback = callback
        self.options = options
        self.options_display = list(options.values()) 
        self.set_value = preset

        self.select = ctk.CTkOptionMenu(
            self,
            values=self.options_display,
            command=self._on_select_change
        )
        if self.set_value:
            self.select.set(self.options[self.set_value])

        self.select.pack(anchor="center")

    def _on_select_change(self, value):
        if self.callback:
            self.callback(next((k for k, v in self.options.items() if v == value), None))

    def set(self, value = None):
        if value:
            self.set_value = value
        self.select.set(self.options[self.set_value])
    
    def get(self):
        return next((k for k, v in self.options.items() if v == self.select.get()), None)
    
