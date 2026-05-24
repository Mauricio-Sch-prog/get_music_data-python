import customtkinter as ctk
import threading

from utils import utils
from utils.getMusicData import get_music_data

from CTkMessagebox import CTkMessagebox
from interface.widgets.listFrame import ListFrame
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn

class FolderList(ctk.CTkFrame):
    def __init__(self, master, folderpath, close_callback, callback = None):
        super().__init__(
            master,
        )
        
        self.folderpath = folderpath
        self.callback = callback

        self._get_folderpath_data()

        self.list = ListFrame(self,
               model={
                   'file' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               },
                title=self.folderpath,
                data=self.folderData,
                                              )
        self.get_data_btn = GetDataBtn(self, command=self._process_folder_data)
        self.close_folder_btn = CloseFolderBtn(self, command=close_callback)

        self._render_grid()

    def _get_folderpath_data(self):
        self.folderData = []
        data = utils.get_folder_data(self.folderpath)

        for song in data:
                    metadata= utils.get_file_metadata(folder_path=self.folderpath, file_name=song['file'])
                    self.folderData.append({
                        'file': song['file'],
                        **metadata
                        })
                    
        self.folderData.sort(key=lambda x: x['file'].lower())

    def _process_folder_data(self):
        self.list.grid_forget()
        self.get_data_btn.grid_forget()
        self.close_folder_btn.grid_forget()
        thread = threading.Thread(target=self._run_logic)
        thread.start()


    def _run_logic(self):
        (data, headers) = self.list._get_data()
        result = get_music_data(data,self)
        if len(result) != 0:
            if self.callback:
                 self.callback(
                    result=result, 
                    folderpath=self.folderpath, 
                    options = headers
                    )
        else:
            CTkMessagebox(title=_("No files"), message=_("No file changed"), icon="cancel")
            self._render_grid()

    def _render_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.list.grid(row=0, column=0,sticky="NSEW", columnspan=2)
        self.get_data_btn.grid(row=1, column=1, sticky="NSEW", pady=5)
        self.close_folder_btn.grid(row=1, column=0, sticky="NSEW", pady=5)

    
    def update_gui(self):
        self.list.update_gui()
        self.close_folder_btn.update_gui()
        self.get_data_btn.update_gui()