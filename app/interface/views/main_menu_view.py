import customtkinter as ctk
from customtkinter import filedialog

from app.interface.components.buttons._btn import BtnModel
from app.interface.components.buttons.select_folder_btn import SelectFolderBtn
from app.interface.events import event_bus


class MainMenuView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master
        )
        self.select_folder_btn = SelectFolderBtn(self, command=self.on_select)
        self.select_folder_btn.pack()

        self.load_saved_processes_btn = BtnModel(self, text = _("Saved processes"),command=self.on_load_saved)
        self.load_saved_processes_btn.pack()


    def on_select(self):

        path = filedialog.askdirectory(title=_("Select your Music Folder"))
        self.select_folder_btn.on_click(text=_("Scanning files..."))

        if path:
            event_bus.emit("START_FOLDER_SCAN", path)
        else:
            self.select_folder_btn.on_click_end(text=_("Select a folder"))
            event_bus.emit("SHOW_ERROR_MESSAGE", _("No folder was selected"))

    def on_load_saved(self):
        event_bus.emit("LOAD_SAVED_PROCESSES")

    def update_gui(self):
        self.select_folder_btn.configure(text=_("Select a folder"))