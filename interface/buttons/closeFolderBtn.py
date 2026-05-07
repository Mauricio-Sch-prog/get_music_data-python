import customtkinter as ctk

class CloseFolderBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, command=command)
        self.configure(
            text="Close folder",
            fg_color="#200a38",
            border_width=2,
            corner_radius=5, 
            border_color="#fc030b", 
            hover_color="#fc030b",
            **kwargs,
        )
        self.pack(anchor='center')