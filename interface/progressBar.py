import customtkinter as ctk

class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, parent):
        # Initialize the CTk version
        super().__init__(parent, width=200, orientation="horizontal")
        
        # CTk ProgressBars are 'determinate' by default
        # Set initial progress to 0
        self.set(0)
        
        # Standard packing
        self.pack(anchor='center', pady=20)
        
    def updateStatus(self, progress):
        """
        Updates the progress bar.
        :param progress: Float between 0.0 and 1.0
        """
        # CTk uses .set() instead of ['value']
        self.set(progress)
        
        # update_idletasks() ensures the UI refreshes immediately
        self.update_idletasks()