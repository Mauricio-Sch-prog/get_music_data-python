import customtkinter as ctk
import datetime

from interface.buttons.btn import Btn

from interface.icons import save_icon
from interface.icons import repeat_icon
from config.data import app_data

class ProcessManagerFrame(ctk.CTkFrame):
    def __init__(self, master, process_result, resume_callback, folderpath ):
        super().__init__(
            master=master
        )

        self.folderpath = folderpath
        self.process_result = process_result
        self.resume_callback = resume_callback
        
        self.label = ctk.CTkLabel(
            self,
            text=_("Manager")
        )

        self.result_label = ctk.CTkLabel(
            self,
            text=_(f"{process_result['progress']} out of {len(process_result['songs'])} were modified")
        )

        self.resume_btn = Btn(
            self,
            command=self._on_resume,
            text=_("Resume changed files"),
        )

        self.save_process_btn = Btn(
            self,
            command=self._on_save,
            text=_("Save progress for later"),
            image=save_icon
        )

        self.retry_btn = Btn(
            self,
            command=self._on_retry,
            text=_("Retry process"),
            image=repeat_icon
        )
        self.label.pack()
        self.result_label.pack()
        self.resume_btn.pack()
        self.save_process_btn.pack()
        self.retry_btn.pack()

    def _on_resume(self):
        self.destroy()
        self.after(0, self.resume_callback, self.process_result["data"])
        return

    def _on_retry(self):
        return
    
    def _on_save(self):
        id = datetime.datetime.now()
        app_data.add_data(
            key="unchanged_processes",
            value={
                "id" : id.isoformat(),
                "folderpath" : self.folderpath,
                "songs" : self.process_result["songs"],
                "progress" : self.process_result["progress"],
                "data" : self.process_result["data"],
            }
        )
        return