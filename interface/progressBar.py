import tkinter as tk
from tkinter import ttk

class ProgressBar(ttk.Progressbar):
    def __init__(self, parent):
        super().__init__(parent, length=200, mode="determinate", orient="horizontal")
        self['value'] = 0
        self.update_idletasks()
        
        
    def updateStatus(self, progress):
        self['value'] = progress
        self.update_idletasks()
        return
        