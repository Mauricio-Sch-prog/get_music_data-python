import customtkinter as ctk

class ApplyChangesBtn(ctk.CTkButton):
    def __init__(self, master , command= None, **kwargs):
        super().__init__(master, command=command)
        self.configure(
            text="Apply changes",
            fg_color="#0320fc",
            **kwargs,
        )
        self.pack(anchor='center')