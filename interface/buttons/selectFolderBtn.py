
from interface.buttons._btn import BtnModel
from customtkinter import filedialog
import threading
from CTkMessagebox import CTkMessagebox
import utils.utils as utils
from config.config import app_config
from utils.folderDataManager import folder_manager
from interface.icons import folder_icon


class SelectFolderBtn(BtnModel):
    def __init__(self, master, on_click_callback=None, **kwargs):
        self.callback = on_click_callback

        defaults = {
            "text":_("Select a folder"),
            "image":folder_icon,
            "command":self._select_folder,
            "corner_radius":20,
            "border_width" : None,
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "fg_color":app_config.get(section='theme', key='primary_color'),
            "hover_color":app_config.get(section='theme', key='success_color'),
            "text_color":app_config.get(section='theme', key='text_color'),
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

    def _select_folder(self):
        self.folder_path = filedialog.askdirectory(title=_("Select your Music Folder"))
        self.on_click(text=_("Scanning files..."))

        thread = threading.Thread(target=self._read_folder, daemon=True)
        thread.start()
        return
    
    def _read_folder(self):
        self.folderData = folder_manager.get_folder_data(self.folder_path)
        self.after(0, lambda:self._load_folder())

    def _load_folder(self):
        self.on_click_end(text=_("Select a folder"))
        if len(self.folderData) and self.callback:
            self.callback()
            return
        
        if not self.folder_path:
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
