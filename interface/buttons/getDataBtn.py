import customtkinter as ctk

class GetDataBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, command=command)
        self.configure(
            text="Get data",
            fg_color="#200a38",
            bg_color="#200a38", 
            border_width=2,
            corner_radius=5, 
            border_color="#0e741d", 
            hover_color="#0e741d",
            **kwargs
        )
        self.pack(anchor='center')

