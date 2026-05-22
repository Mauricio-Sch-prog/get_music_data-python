import customtkinter as ctk

class OptionsInputFrame(ctk.CTkFrame):
    def __init__(self, master, options, callback, preset = None):
        super().__init__(
            master
            )
        

        self.callback = callback
        self.options = options
        self.options_display = list(options) 
        self.preset = preset

        self.select = ctk.CTkOptionMenu(
            self,
            values=self.options_display,
            command=self._on_select_change
        )
        if self.preset:
            self.select.set(self.preset)

        self.select.pack(anchor="center")

    def _on_select_change(self, value):
        if self.callback:
            self.callback(self.options[value])
