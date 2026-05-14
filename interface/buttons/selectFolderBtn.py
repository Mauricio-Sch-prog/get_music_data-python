import customtkinter as ctk
from customtkinter import filedialog
import threading
from CTkMessagebox import CTkMessagebox
import utils
from config import app_config
from interface.widgets.icons import folder_icon


class SelectFolderBtn(ctk.CTkButton):
    def __init__(self, parent, on_click_callback=None, **kwargs):
        self.callback = on_click_callback
        super().__init__(parent, image=folder_icon)
        self.configure(
            text="Select a folder",
            command=self.start_loading,
            corner_radius=20,
            bg_color=app_config['theme']['secondary_color'][0],
            fg_color=app_config['theme']['primary_color'][0],
            hover_color=app_config['theme']['success_color'][0],
            **kwargs
        )

    def start_loading(self):
        self.folderPath = filedialog.askdirectory(title="Select your Music Folder")
        self.configure(state="disabled")
        self.configure(text="Scanning files...")


        thread = threading.Thread(target=self.read_folder, daemon=True)
        thread.start()
        return
    
    def read_folder(self):
        data = utils.get_folder_data(self.folderPath)
        self.folderData = []

        for song in data:
                    metadata= utils.get_file_metadata(folder_path=self.folderPath, file_name=song['file'])
                    self.folderData.append({
                        'file': song['file'],
                        **metadata
                        })
        self.after(0, lambda:self.load_folder())

    def load_folder(self):
        self.configure(state="normal")
        self.configure(text="Select a folder")
        if(self.folderData and self.callback):
            self.callback()
            return
        CTkMessagebox(title="Error", message="Music folder not found!", icon="cancel")
        return
