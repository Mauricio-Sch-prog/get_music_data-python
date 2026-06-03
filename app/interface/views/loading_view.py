import customtkinter as ctk
from app.interface.components.cards.progress_bar_card import ProgressBarCard

class LoadingView(ctk.CTkFrame):
    def __init__(self, master, text, progress = None):
        super().__init__(master)
        self.text = ctk.CTkLabel(
            self,
            text = text
        )

        if progress:
            self.loading_bar = ProgressBarCard(
                self
            )
            self.loading_bar.pack()


        self.text.pack()

    def update_bar(self, progress = None, text=None):
        self.text.configure(text=text if text else "")
        if progress:
            if self.loading_bar:
                self.loading_bar.update_status(progress)
            else:
                self.loading_bar = ProgressBarCard(self)
                self.loading_bar.update_status(progress)
        