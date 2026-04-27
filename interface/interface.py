import tkinter as tk
from tkinter import filedialog

# from interface.selectFolder import select_music_folder
import utils

from interface.processContainer import ProcessContainer

from PIL import Image, ImageTk


def loadWindow():
    
    def getFolder():
        folderPath = filedialog.askdirectory(title="Select your Music Folder")
        folder = utils.getFolderData(folderPath)
        if(folder):
            
            def onCloseFolder(event):
                if event.widget == fileList:
                    selectFolderBtn.pack(side="top", padx=30, pady=100)
                else:
                    pass
        
            selectFolderBtn.pack_forget()
            fileList = ProcessContainer(parent=root, folderPath=folderPath , folder=folder)
            fileList.pack(fill="both", expand=True, padx=10, pady=10)
            fileList.bind("<Destroy>", onCloseFolder)
            
        return
    
    
    root = tk.Tk()
    
    pil_img = Image.open('icon.jpg')
    icon = ImageTk.PhotoImage(pil_img)
    
    root.iconphoto(True, icon)
    root.title("Get Your Music Data(AI Powered).")
    root.geometry("800x600")
    root.config(background="#200a38")
    
    selectFolderBtn = tk.Button(root, text="Select a folder", command=getFolder)
    selectFolderBtn.pack(side="top", padx=30, pady=100)
    
    root.mainloop()
    return