import tkinter as tk

# from interface.selectFolder import select_music_folder
import utils

from interface.fileContainer import FileListContainer

from PIL import Image, ImageTk


def loadWindow():
    songList = []
    folderPath = ''
    fileContainer = ''
    
    def getFolder():
        folderPath = tk.filedialog.askdirectory(title="Select your Music Folder")
        folder = utils.getFolderData(folderPath)
        if(folder):
            
            fileContainer = FileListContainer(root,
               {
                   'filename' : {'optional' : False},
                   'title' : {'optional' : True},
                   'artist' : {'optional' : True},
                   'genre' : {'optional' : True},
               }                               
                                              )
            fileContainer.pack(fill="both", expand=True, padx=10, pady=10)
            
            songList = folder
            for song in songList:
                metadata= utils.get_file_metadata(folder_path=folderPath, file_name=song['file'])
                fileContainer.add_file({
                    'filename': song['file'],
                    **metadata
                    })
            
        
        return
    
    
    root = tk.Tk()
    
    pil_img = Image.open('Imagem_do_WhatsApp_de_2024-02-08_as_14.31.09_50e2a151.jpg')
    icon = ImageTk.PhotoImage(pil_img)
    
    root.iconphoto(True, icon)
    root.title("Get Your Music Data(AI Powered).")
    root.geometry("800x600")
    root.config(background="#200a38")
    
    selectFolderBtn = tk.Button(root, text="Select a folder", command=getFolder)
    selectFolderBtn.pack(side="top", padx=30, pady=100)
    
    root.mainloop()
    return