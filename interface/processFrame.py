from interface.widgets.listFrame import ListFrame
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn
from interface.buttons.applyChangesBtn import ApplyChangesBtn
import customtkinter as ctk
import threading
import utils.utils as utils
from utils.getMusicData import getMusicData
from CTkMessagebox import CTkMessagebox
from config.config import app_config

class ProcessContainer(ctk.CTkFrame):
    def __init__(self, parent, folderPath, folderData, callback=None):
        super().__init__(parent)
        self.configure(
            bg_color=app_config.get(section='theme', key='secondary_color'),
            fg_color=app_config.get(section='theme', key='secondary_color'),
        )
        
        self.callback = callback
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.folderData=folderData
        self.load_folder_in_list(data = folderData, path = folderPath)
        

    def load_folder_in_list(self, data, path):
        self.fileContainer = ListFrame(self,
               model={
                   'file' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               },
                title=path,
                data=data,
                                              )
        def process_folder_data():
            self.fileContainer.grid_forget()
            self.getDataBtn.grid_forget()
            self.closeFolderBtn.grid_forget()
            thread = threading.Thread(target=run_logic)
            thread.start()
        
        def run_logic():
            (data, headers) = self.fileContainer._get_data()
            result = getMusicData(data,self)
            if len(result) != 0:
                self.renderResultContainer(result=result, folderPath=path)
            else:
                CTkMessagebox(title=_("No files"), message=_("No file changed"), icon="cancel")
                render_grid()
        
        def render_grid():
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1) 
            self.grid_rowconfigure(1, weight=0)
            self.fileContainer.grid(row=0, column=0,sticky="NSEW", columnspan=2)
            self.getDataBtn.grid(row=1, column=1, sticky="NSEW", pady=5)
            self.closeFolderBtn.grid(row=1, column=0, sticky="NSEW", pady=5)
        
        self.getDataBtn = GetDataBtn(self, command=process_folder_data)
        self.closeFolderBtn = CloseFolderBtn(self, command=self.close_folder)
        render_grid()


    def close_folder(self):
            self.destroy()
            self.callback()
            return
            
    def renderResultContainer(self, result, folderPath):
        (data, headers) = self.fileContainer._get_data()
        model = utils.get_changed_files_model(result=result,options=headers)
        self.resultContainer = ListFrame(self,
                    model,
                 title=_("Changed files"),
                 data=result,
                 options= {'main': 'id'})
        
        
        
        def applyChanges():
            self.fileContainer.grid_forget()
            self.applyChangesBtn.grid_forget()
            self.closeFolderBtn.grid_forget()
            
            thread = threading.Thread(target=applyChangesLogic)
            thread.start()
            
        def applyChangesLogic():
            (data, headers) = self.resultContainer._get_data()
            utils.change_file_metadate(changed_files=data,folder_path=folderPath, options=headers, parent=self)
            self.after(100, self.close_folder)
            


        self.applyChangesBtn = ApplyChangesBtn(self, command=applyChanges)

        self.resultContainer.grid(row=0, column=0,sticky="NSEW", columnspan=2)
        self.applyChangesBtn.grid(row=1, column=1, sticky="NSEW", pady=5)
        self.closeFolderBtn.grid(row=1, column=0, sticky="NSEW", pady=5)

    def update_gui(self):
        self.getDataBtn.update_gui()
        self.closeFolderBtn.update_gui()
        return
