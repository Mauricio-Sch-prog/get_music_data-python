import customtkinter as ctk

class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, orientation="horizontal", **kwargs)
        
        self.set(0)
        
    def update_status(self, progress):
        self.after(0, lambda: self.set(progress))
        self.update_idletasks()