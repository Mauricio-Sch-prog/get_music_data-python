import customtkinter as ctk
import threading

from utils import utils

from interface.widgets.listFrame import ListFrame
from interface.buttons.applyChangesBtn import ApplyChangesBtn
from interface.buttons.closeFolderBtn import CloseFolderBtn

class ResultList(ctk.CTkFrame):
    def __init__(self, master, data, folderpath, options, close_callback, callback = None):
        super().__init__(
            master,
        )

        self.close_callback = close_callback
        self.callback = callback
        self.folderpath = folderpath
        self._get_list_model(sample=data[0], options=options)

        self.list = ListFrame(
            self,
            model=self.model,
            title=_("Changed files"),
            data=data,
            custom= {'main': 'id'})
        
        self.close_folder_btn = CloseFolderBtn(self, command=close_callback)
        self.apply_changes_btn = ApplyChangesBtn(self, command=self._apply_changes)

        self._render_grid()


    def _get_list_model(self, sample, options):
        optionKeys = ", ".join(options)
        model = {}
        for key, value in sample.items():
            if(key in optionKeys and options[key] == 1):
                model[key] = {'optional' : "Ignore"}
            else:
                model[key] = {'optional' : False}
        
        orderedModel = {}
        order = ["id", 'file', 'title', 'artist', 'genre', 'album', 'date']
        for orderKey in order:
            for key, value in model.items():
                if key in orderKey:
                    orderedModel[key] = value
    
        self.model = orderedModel

    def _apply_changes(self):
        self.list.grid_forget()
        self.apply_changes_btn.grid_forget()
        self.close_folder_btn.grid_forget()
        
        thread = threading.Thread(target=self._run_logic)
        thread.start()

    def _run_logic(self):
        (data, headers) = self.list._get_data()
        utils.change_file_metadate(changed_files=data,folderpath=self.folderpath, options=headers, parent=self)
        self.after(100, self.close_callback)


    def _render_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.list.grid(row=0, column=0,sticky="NSEW", columnspan=2)
        self.close_folder_btn.grid(row=1, column=0, sticky="NSEW", pady=5)
        self.apply_changes_btn.grid(row=1, column=1, sticky="NSEW", pady=5)

    def update_gui(self):
        self.list.title.configure(text=_("Changed files"))
        self.list.update_gui()
        self.close_folder_btn.update_gui()
        self.apply_changes_btn.update_gui()