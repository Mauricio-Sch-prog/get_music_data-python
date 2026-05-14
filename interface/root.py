import customtkinter as ctk
from tkinter import PhotoImage
from config import app_config

class Root(ctk.CTk):
    def __init__(self):
        super().__init__()


        ctk.set_appearance_mode("dark")
        self.title("Get Your Music Data(AI Powered).")
        self.geometry("800x600")
        self.configure(fg_color=app_config['theme']['secondary_color'][0])
        icon_image = PhotoImage(file="icon.png")
        self.iconphoto(False, icon_image)
        