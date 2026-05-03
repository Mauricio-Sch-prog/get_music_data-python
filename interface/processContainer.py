from interface.listContainer import ListContainer
import customtkinter as ctk
import utils
from getMusicData import getMusicData
import threading

class ProcessContainer(ctk.CTkFrame):
    def __init__(self, parent, folderPath, folder, ):
        
    
        super().__init__(parent, bg_color="#200a38", fg_color="#200a38")
        
        self.fileContainer = ListContainer(self,
               model={
                   'filename' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               },
                title=folderPath                               
                                              )
        
        self.fileContainer.pack(fill="both", expand=True, padx=10, pady=10)
        
        
        def processFolderData():
            self.fileContainer.pack_forget()
            self.nextBtn.pack_forget()
            self.closeFolderBtn.pack_forget()
            thread = threading.Thread(target=run_logic)
            thread.start()
        
        def run_logic():
            result = getMusicData(folder,self)
            if len(result) != 0:
                self.renderResultContainer(result=result, folderPath=folderPath)
            else:
                self.fileContainer.pack(fill="both", expand=True, padx=10, pady=10)
                self.nextBtn.pack(anchor='center')
                self.closeFolderBtn.pack(anchor='center')
            return
        
        def closeFolder():
            self.destroy()
            return
        
        
        self.nextBtn = ctk.CTkButton(self, text="Get data", command=processFolderData, bg_color="#200a38", fg_color="#200a38")
        self.nextBtn.configure(border_width=2, corner_radius=5, border_color="#0e741d", hover_color="#0e741d")
        self.nextBtn.pack(anchor='center')
        
        self.closeFolderBtn = ctk.CTkButton(self, text="close folder", command=closeFolder, fg_color="#200a38")
        self.closeFolderBtn.configure(border_width=2, corner_radius=5, border_color="#fc030b", hover_color="#fc030b")
        self.closeFolderBtn.pack(anchor='center')
        
        for song in folder:
            self.metadata= utils.get_file_metadata(folder_path=folderPath, file_name=song['file'])
            self.fileContainer.add_file({
                'filename': song['file'],
                **self.metadata
                })
            
    def renderResultContainer(self, result, folderPath):

        model = utils.get_changed_files_model(result=result,options=self.fileContainer.get_list_data())
                
        print(model)
        self.resultContainer = ListContainer(self,
                    model,
                 title="Changed files")
        
        self.resultContainer.pack(fill="both", expand=True, padx=10, pady=10)
        
        for song in result:
            self.resultContainer.add_file(song, options= {'main': 'id'})
        
        def applyChanges():
            self.fileContainer.pack_forget()
            self.applyChangesBtn.pack_forget()
            
            thread = threading.Thread(target=applyChangesLogic)
            thread.start()
            
        def applyChangesLogic():
            utils.change_file_metadate(changed_files=result,folder_path=folderPath, options=self.fileContainer.get_list_data(), parent=self)
            self.after(100, self.destroy)
            
            
        self.applyChangesBtn = ctk.CTkButton(self, text="Apply changes", command=applyChanges, fg_color="#0320fc")
        self.applyChangesBtn.pack(anchor='center')