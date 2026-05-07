import customtkinter as ctk

class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=200, orientation="horizontal", **kwargs)
        
        self.set(0)
        self.pack(anchor='center', pady=20)
        
    def updateStatus(self, progress):
        self.after(0, lambda: self.set(progress))
        self.update_idletasks()