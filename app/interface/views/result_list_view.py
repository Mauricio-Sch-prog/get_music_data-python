import threading

import customtkinter as ctk

from app.backend.utils.processManager import app_process
from app.interface.components.buttons.apply_changes_btn import ApplyChangesBtn
from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.cards.list_card import ListCard
from app.interface.events import event_bus


class ResultListView(ctk.CTkFrame):
    def __init__(self, master, data, model):
        super().__init__(
            master,
        )

        self.data = data        
        self.model = model

        self.list = ListCard(
            self,
            model=self.model,
            title=_("Changed files"),
            data=self.data,
            custom= {'main': 'id'})

        self.close_folder_btn = CloseBtn(self, command=self.on_close)
        self.apply_changes_btn = ApplyChangesBtn(self, command=self.apply_changes)

        self._render_grid()


    def on_close(self):
        self.close_folder_btn.on_click()
        event_bus.emit("NAVIGATE_TO_MENU")


    def apply_changes(self):
        self.apply_changes_btn.on_click()

        threading.Thread(
            target=self._fetch_list_data,
            args=(), 
            daemon=True
        ).start()
        

    def _fetch_list_data(self):
        (data, headers) = self.list.get_data()
        process = app_process.get()
        process['data'] = data
        self.after(0, self.end_fetch_list_data)
        

    def end_fetch_list_data(self):
        event_bus.emit("START_APPLY_CHANGES")


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
        self.close_folder_btn.configure(text=_("Close folder"))
        self.apply_changes_btn.configure(text=_("Apply changes"))