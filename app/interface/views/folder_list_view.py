import threading

import customtkinter as ctk

from app.backend.utils.processManager import app_process
from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.buttons.get_data_btn import GetDataBtn
from app.interface.components.cards.list_card import ListCard
from app.interface.events import event_bus


class FolderListView(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master, bg_color="transparent")
        
        self.folder_data = data
    
        self.list = ListCard(
            self,
            model={
                'file' : {'optional' : False},
                'title' : {'optional' : True},
                'artist' : {'optional' : True},
                'genre' : {'optional' : True},
                'album' : {'optional' : True},
                'date' : {'optional' : True},
            },
            title=self.master.folder_path,
            data=self.folder_data,
        )
        self.close_folder_btn = CloseBtn(self, command=self.on_close_click)
        self.get_data_btn = GetDataBtn(self, command=self.on_get_data_click)

        self._render_grid()

    def on_close_click(self):
        event_bus.emit("NAVIGATE_TO_MENU")
        return
    
    def on_get_data_click(self):
        self.get_data_btn.on_click(_("loading"))
        
        threading.Thread(
            target=self._create_process,
            args=(),
            daemon=True,
        ).start()
    
    def _create_process(self):
        (data, headers) = self.list.get_data()
        app_process.create(self.master.folder_path , options = headers)
        self.after(0, lambda: self._start_data_enrichment())

    def _start_data_enrichment(self):
        event_bus.emit("START_DATA_ENRICHMENT")


    def _render_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.list.grid(row=0, column=0, sticky="NSEW", columnspan=2)
        self.get_data_btn.grid(row=1, column=1, sticky="NSEW", pady=5)
        self.close_folder_btn.grid(row=1, column=0, sticky="NSEW", pady=5)

    def update_gui(self):
        if hasattr(self, 'list'):
            self.list.update_gui()
            self.close_folder_btn.configure(text=_("Close folder"))
            self.get_data_btn.configure(text=_("Get data"))