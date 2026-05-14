
from interface.processFrame import ProcessContainer
from interface.root import Root
from interface.buttons.selectFolderBtn import SelectFolderBtn
from interface.buttons.configBtn import ConfigBtn




class App():
    def __init__(self):
        super().__init__()
        self.root = Root()
        self.load = self._load_widgets
        self.selectBtn = SelectFolderBtn(
            self.root,
            on_click_callback=self.load_folder
        )

        self.configBtn = ConfigBtn(
            self.root,
            load=self._load_widgets
        )

        self.root.bind("WM_DELETE_WINDOW", self.on_closing)

        self._load_widgets()
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



    def _load_widgets(self):
        self.configBtn.pack(anchor='nw', padx=5, pady=5)
        self.selectBtn.pack(side="top", padx=30, pady=30)


    def on_closing(self):
        self.root.destroy()
