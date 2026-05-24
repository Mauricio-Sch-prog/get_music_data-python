from interface.widgets.listFrame import ListFrame
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn
from interface.buttons.applyChangesBtn import ApplyChangesBtn
import customtkinter as ctk
import threading
import utils.utils as utils
from utils.getMusicData import get_music_data
from CTkMessagebox import CTkMessagebox
from config.config import app_config
from interface.widgets.folderList import FolderList
from interface.widgets.resultList import ResultList

class ProcessContainer(ctk.CTkFrame):
    def __init__(self, parent, folderPath, close_callback=None):
        super().__init__(parent)
        self.configure(
            bg_color=app_config.get(section='theme', key='secondary_color'),
            fg_color=app_config.get(section='theme', key='secondary_color'),
        )
        
        self.close_callback = close_callback
        self.result_list = None

        self._load_folder_list(path = folderPath)
        

    def _load_folder_list(self, path):
        self.folder_list = FolderList(
            self,
            folderpath=path,
            close_callback=self._close_process,
            callback=self._load_result_list
        )
        self.folder_list.pack(fill="both", expand=True, padx=10, pady=10)

            
    def _load_result_list(self, result, folderpath, options):
        self.folder_list.pack_forget()
        self.result_list = ResultList(
            self,
            data=result,
            folderpath=folderpath,
            options=options,
            close_callback=self._close_process,
        )

        self.result_list.pack(fill="both", expand=True, padx=10, pady=10)


    def _close_process(self):
            self.destroy()
            self.close_callback()
            return
    

    def update_gui(self):
        self.folder_list.update_gui()
        if self.result_list:
            self.result_list.update_gui()
            self.result_list.title.configure(text=_("Changed files"))
        return
