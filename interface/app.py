
from interface.processContainer import ProcessContainer
from interface.root import Root
from interface.buttons.selectFolderBtn import SelectFolderBtn




class App():
    def __init__(self):
        super().__init__()
        self.root = Root()
        self.selectBtn = SelectFolderBtn(
            self.root,
            on_click_callback=self.load_folder
        )

        self.root.mainloop()


    def load_folder(self):
        def on_close_folder():
            self.selectBtn.pack(side="top", padx=30, pady=100)
        
        self.selectBtn.pack_forget()
        self.fileList = ProcessContainer(
            parent=self.root, 
            folderPath=self.selectBtn.folderPath,
            folderData=self.selectBtn.folderData, 
            callback=on_close_folder)
        print

