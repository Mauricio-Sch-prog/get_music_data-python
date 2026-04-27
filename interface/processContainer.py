from interface.container import ListContainer
import tkinter as tk
import utils
from getMusicData import getMusicData
import threading

class ProcessContainer(tk.Frame):
    def __init__(self, parent, folderPath, folder):
        
    
        super().__init__(parent)
        
        self.fileContainer = ListContainer(self,
               {
                   'filename' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
                   'album' : {'optional' : True},
                   'date' : {'optional' : True},
               }                               
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
            self.renderResultContainer(result=result, folderPath=folderPath)
            return result
        
        
        def closeFolder():
            self.destroy()
            return
        
        
        self.nextBtn = tk.Button(self, text="Get data", command=processFolderData, background="#03fc28")
        self.nextBtn.pack(anchor='center')
        
        self.closeFolderBtn = tk.Button(self, text="close folder", command=closeFolder, background="#fc030b")
        self.closeFolderBtn.pack(anchor='center')
        
        for song in folder:
            self.metadata= utils.get_file_metadata(folder_path=folderPath, file_name=song['file'])
            self.fileContainer.add_file({
                'filename': song['file'],
                **self.metadata
                })
            
    def renderResultContainer(self, result, folderPath):
        print(result)
        self.resultContainer = ListContainer(self,{
                   'id' : {'optional' : False},
                   'file' : {'optional' : False},
                   'title' : {'optional' : False},
                   'artist' : {'optional' : False},
                   'genre' : {'optional' : False},
                   'album' : {'optional' : False},
                   'date' : {'optional' : False},
               })
        
        self.resultContainer.pack(fill="both", expand=True, padx=10, pady=10)
        
        for song in result:
            self.resultContainer.add_file(song)
        
        def applyChanges():
            utils.change_file_metadate(changed_files=result,folder_path=folderPath, options=self.fileContainer.get_list_data())
            
            
        self.applyChangesBtn = tk.Button(self, text="Apply changes", command=applyChanges, background="#0320fc")
        self.applyChangesBtn.pack(anchor='center')