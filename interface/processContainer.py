from interface.widgets.listContainer import ListContainer
from interface.buttons.closeFolderBtn import CloseFolderBtn
from interface.buttons.getDataBtn import GetDataBtn
from interface.buttons.applyChangesBtn import ApplyChangesBtn
import customtkinter as ctk
import utils
from getMusicData import getMusicData
import threading

class ProcessContainer(ctk.CTkFrame):
    def __init__(self, parent, folderPath, folderData, callback=None):
        super().__init__(parent, bg_color="#200a38", fg_color="#200a38")
        
        self.callback = callback
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.folderData=folderData
        
        self.fileContainer = ListContainer(self,
               model={
                   'filename' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               },
                title=folderPath,
                data=folderData      
                                              )
        
        
        def process_folder_data():
            self.fileContainer.pack_forget()
            self.getDataBtn.pack_forget()
            self.closeFolderBtn.pack_forget()
            thread = threading.Thread(target=run_logic)
            thread.start()
        
        def run_logic():
            result = getMusicData(folderData,self)
            if len(result) != 0:
                self.renderResultContainer(result=result, folderPath=folderPath)
            else:
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

        model = utils.get_changed_files_model(result=result,options=self.fileContainer.get_list_data())
                
        self.resultContainer = ListContainer(self,
                    model,
                 title="Changed files",
                 data=result,
                 options= {'main': 'id'})
        
        self.resultContainer.pack(fill="both", expand=True, padx=10, pady=10)
        
        for song in result:
            self.resultContainer.add_file(song)
        
        def applyChanges():
            self.fileContainer.pack_forget()
            self.applyChangesBtn.pack_forget()
            
            thread = threading.Thread(target=applyChangesLogic)
            thread.start()
            
        def applyChangesLogic():
            utils.change_file_metadate(changed_files=result,folder_path=folderPath, options=self.fileContainer.get_list_data(), parent=self)
            self.after(100, self.close_folder)
            

        self.applyChangesBtn = ApplyChangesBtn(self, command=applyChanges)
        self.closeFolderBtn.pack(anchor='center')