import customtkinter as ctk
from customtkinter import filedialog
import threading
from CTkMessagebox import CTkMessagebox
import utils.utils as utils
from config.config import app_config
from interface.icons import folder_icon


class SelectFolderBtn(ctk.CTkButton):
    def __init__(self, parent, on_click_callback=None, **kwargs):
        self.callback = on_click_callback
        super().__init__(parent, image=folder_icon)
        self.configure(
            text=_("Select a folder"),
            command=self._start_loading,
            corner_radius=20,
            bg_color=app_config.get(section='theme', key='secondary_color'),
            fg_color=app_config.get(section='theme', key='primary_color'),
            hover_color=app_config.get(section='theme', key='success_color'),
            text_color=app_config.get(section='theme', key='text_color'),
            **kwargs
        )

    def _start_loading(self):
        self.folderPath = filedialog.askdirectory(title=_("Select your Music Folder"))
        self.configure(state="disabled")
        self.configure(text=_("Scanning files..."))

        thread = threading.Thread(target=self._read_folder, daemon=True)
        thread.start()
        return
    
    def _read_folder(self):
        self.folderData = None
        if not self.folderPath:
            return self._load_folder()
        self.folderData = utils.get_folder_data(self.folderPath)

        self.after(0, lambda:self._load_folder())

    def _load_folder(self):
        self.configure(
            state="normal",
            text=_("Select a folder"),
            )
        if(self.folderData and self.callback):
            self.callback()
            return
        
        if not self.folderPath:
            CTkMessagebox(
                title=_("Folder not selected"), 
                message=_("No folder was selected"), 
                icon="cancel")
        
        else:
             CTkMessagebox(
                title=_("Error"), 
                message=_("Music folder not found!"), 
                icon="cancel")
        return
    
    def update_gui(self):
        self.configure(text=_("Select a folder"))
