import customtkinter as ctk

from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import arrow_down_icon, x_icon
from app.interface.events import event_bus


class ProcessCard(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)

        self.folder_path_label = ctk.CTkLabel(
            master,
            text=data['folder_path']
        )

        self.label = ctk.CTkLabel(
            master,
            text=_(f"{data['progress']} out of {len(data['songs'])} were modified in this process")
        ) 

        self.missing_label = ctk.CTkLabel(
            master,
            text=_(f"current missing songs: {len(data['missing'])}")
        )

        self.remove_process_btn = BtnModel(
            self, 
            image=x_icon, 
            text=None,
            command=self.on_remove
            )

        self.resume_process_btn = BtnModel(
            self, 
            image=arrow_down_icon, 
            text=None,
            command = self.on_resume
            )

        self.folder_path_label.pack()
        self.label.pack()
        self.missing_label.pack()
        self.resume_process_btn.pack()
        self.remove_process_btn.pack()
        
        self.data = data

    def on_resume(self):
        self.resume_process_btn.on_click()
        event_bus.emit("RELOAD_PROCESS", self.data['id'])

    def on_remove(self):
        self.remove_process_btn.on_click()
        event_bus.emit("REMOVE_SAVED_PROCESS", self.data['id'])
        self.destroy()