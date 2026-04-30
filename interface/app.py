from customtkinter import filedialog
import customtkinter as ctk
import utils
from interface.processContainer import ProcessContainer

class App(ctk.CTk):
    def __init__(self,):
        super().__init__()
        
        self.title("Get Your Music Data(AI Powered).")
        self.geometry("800x600")
        self.configure(fg_color="#200a38")
        self.iconbitmap('icon.ico')
        
        self.selectFolderBtn = ctk.CTkButton(self, text="Select a folder", command=self.getFolder)
        self.selectFolderBtn.configure(corner_radius=20, bg_color="#200a38")
        self.selectFolderBtn.pack(side="top", padx=30, pady=100)
        
        
        self.mainloop()
    
    def getFolder(self):
        self.folderPath = filedialog.askdirectory(title="Select your Music Folder")
        self.folder = utils.getFolderData(self.folderPath)
        if(self.folder):
            self.loadFolder()

    def loadFolder(self):
        def onCloseFolder(event):
            print(event.widget)
            print(str(self.fileList))
            if str(event.widget) == str(self.fileList):
                self.selectFolderBtn.pack(side="top", padx=30, pady=100)
            else:
                pass
        
        self.selectFolderBtn.pack_forget()
        self.fileList = ProcessContainer(parent=self, folderPath=self.folderPath , folder=self.folder)
        self.fileList.pack(fill="both", expand=True, padx=10, pady=10)
        self.fileList.bind("<Destroy>", onCloseFolder)
