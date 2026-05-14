import customtkinter as ctk

class batchSliderFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure()

        self.text = ctk.CTkLabel(
            self,
            text="Batch fetch per api request"
        )