import customtkinter as ctk
from tkinter import PhotoImage

class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Get Your Music Data(AI Powered).")
        self.geometry("800x600")
        self.configure(fg_color="#200a38")
        icon_image = PhotoImage(file="icon.png")
        self.iconphoto(False, icon_image)   
        