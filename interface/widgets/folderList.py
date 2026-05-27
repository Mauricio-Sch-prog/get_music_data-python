import customtkinter as ctk
import threading

from utils import utils
from utils.getMusicData import get_music_data
from utils.folderDataManager import folder_manager

from CTkMessagebox import CTkMessagebox
from interface.widgets.listFrame import ListFrame
from interface.widgets.loadingProcessFrame import LoadingProcessFrame
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn

class FolderList(ctk.CTkFrame):
    def __init__(self, master, folderpath, close_callback, callback = None):
        super().__init__(master)
        
        self.folderpath = folderpath
        self.callback = callback
        self.close_callback = close_callback
        self.folderData = []

        self.loading_label = ctk.CTkLabel(self, text=_("Scanning music files, please wait..."), font=("Arial", 14))
        self.loading_label.pack(expand=True, fill="both", padx=20, pady=20)

        thread = threading.Thread(target=self._get_folderpath_data, daemon=True)
        thread.start()

    def _get_folderpath_data(self):
        local_data = folder_manager.get_folder_data(self.folderpath)
        local_data.sort(key=lambda x: x['file'].lower())
        self.folderData = local_data

        self.after(0, self._on_data_ready, self.folderData, self.close_callback)

    def _on_data_ready(self, folder_data, close_callback):
        self.loading_label.pack_forget()
        self.loading_label.destroy()

    
        self.list = ListFrame(
            self,
            model={
                'file' : {'optional' : False},
                'title' : {'optional' : True},
                'artist' : {'optional' : True},
                'genre' : {'optional' : True},
                'album' : {'optional' : True},
                'date' : {'optional' : True},
            },
            title=self.folderpath,
            data=folder_data,
        )
        self.get_data_btn = GetDataBtn(self, command=self._process_folder_data)
        self.close_folder_btn = CloseFolderBtn(self, command=close_callback)

        self._render_grid()

    def _process_folder_data(self):
        self.list.grid_forget()
        self.get_data_btn.grid_forget()
        self.close_folder_btn.grid_forget()
        
        (data, headers) = self.list._get_data()
        
        thread = threading.Thread(target=self._run_logic, args=(data, headers), daemon=True)
        thread.start()

    def _run_logic(self, data, headers):
        def on_complete(success, data, error):
            if success:
                self.after(0, lambda: self._handle_process_result(data, headers))
            else:
                print(error)
                self.after(0, lambda: self._render_grid())
                return

        result = LoadingProcessFrame(
            master= self,
            process= get_music_data,
            on_complete_callback=on_complete,
            songs = data,
            folderpath = self.folderpath,
        )
        result.pack(fill="both", expand=True, padx=10, pady=10)

    def _handle_process_result(self,result, headers):
        if len(result) != 0:
            if self.callback:
                 self.callback(
                    result=result, 
                    folderpath=self.folderpath, 
                    options=headers
                 )
        else:
            CTkMessagebox(title=_("No files"), message=_("No file changed"), icon="cancel")
            self._render_grid()

    def _render_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.list.grid(row=0, column=0, sticky="NSEW", columnspan=2)
        self.get_data_btn.grid(row=1, column=1, sticky="NSEW", pady=5)
        self.close_folder_btn.grid(row=1, column=0, sticky="NSEW", pady=5)

    def update_gui(self):
        if hasattr(self, 'list'):
            self.list.update_gui()
            self.close_folder_btn.update_gui()
            self.get_data_btn.update_gui()