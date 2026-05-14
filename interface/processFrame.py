from interface.widgets.listFrame import ListContainer
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn
from interface.buttons.applyChangesBtn import ApplyChangesBtn
import customtkinter as ctk
import threading
import utils
from getMusicData import getMusicData
from CTkMessagebox import CTkMessagebox
from config import app_config

class ProcessContainer(ctk.CTkFrame):
    def __init__(self, parent, folderPath, folderData, callback=None):
        super().__init__(parent)
        self.configure(
            bg_color=app_config['theme']['secondary_color'][0],
            fg_color=app_config['theme']['secondary_color'][0],
        )
        
        self.callback = callback
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.folderData=folderData
        
        self.fileContainer = ListContainer(self,
               model={
                   'file' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               },
                title=folderPath,
                data=folderData,
                                              )
        
        
        def process_folder_data():

            self.fileContainer.pack_forget()
            self.getDataBtn.pack_forget()
            self.closeFolderBtn.pack_forget()
            thread = threading.Thread(target=run_logic)
            thread.start()
        
        def run_logic():
            (data, headers) = self.fileContainer._get_data()
            result = getMusicData(data,self)
            if len(result) != 0:
                self.renderResultContainer(result=result, folderPath=folderPath)
            else:
                CTkMessagebox(title="No files", message="No file changed", icon="cancel")
                self.fileContainer.pack(fill="both", expand=True, padx=10, pady=10)
                self.nextBtn.pack(anchor='center')
                self.closeFolderBtn.pack(anchor='center')
        
        
        self.getDataBtn = GetDataBtn(self, command=process_folder_data)
        self.closeFolderBtn = CloseFolderBtn(self, command=self.close_folder)
        
            
    def close_folder(self):
            self.destroy()
            self.callback()
            return
            
    def renderResultContainer(self, result, folderPath):
        (data, headers) = self.fileContainer._get_data()
        model = utils.get_changed_files_model(result=result,options=headers)
        print(model)
        self.resultContainer = ListContainer(self,
                    model,
                 title="Changed files",
                 data=result,
                 options= {'main': 'id'})
        
        self.resultContainer.pack(fill="both", expand=True, padx=10, pady=10)
        
        
        def applyChanges():
            self.fileContainer.pack_forget()
            self.applyChangesBtn.pack_forget()
            
            thread = threading.Thread(target=applyChangesLogic)
            thread.start()
            
        def applyChangesLogic():
            (data, headers) = self.fileContainer._get_data()
            utils.change_file_metadate(changed_files=data,folder_path=folderPath, options=headers, parent=self)
            self.after(100, self.close_folder)
            

        self.applyChangesBtn = ApplyChangesBtn(self, command=applyChanges)
        self.closeFolderBtn.pack(anchor='center')