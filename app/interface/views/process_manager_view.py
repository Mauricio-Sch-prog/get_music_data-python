import threading

import customtkinter as ctk

from app.backend.utils.processManager import app_process
from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.buttons.resume_btn import ResumeBtn
from app.interface.components.buttons.retry_btn import RetryBtn
from app.interface.components.buttons.save_btn import SaveBtn
from app.interface.events import event_bus


class ProcessManagerView(ctk.CTkFrame):
    def __init__(self, master, process,
            ):
        
        super().__init__(master=master)
        self.process = process
        
        self.label = ctk.CTkLabel(
            self,
            text=_("Manager")
        )

        self.result_label = ctk.CTkLabel(
            self,
            text=_(f"{process['progress']} out of {len(process['songs'])} were modified")
        )

        self.resume_btn = ResumeBtn(
            self,
            command=self.on_resume,
            text=_("Resume changed files"),
        )

        self.save_process_btn = SaveBtn(
            self,
            command=self.on_save,
            text=_("Save progress for later"),
        )

        self.retry_btn = RetryBtn(
            self,
            command=self.on_retry,
            text=_("Retry process"),
        )

        self.close_btn = CloseBtn(
            self,
            command=self.on_close,
        )

        self.label.pack()
        self.result_label.pack()
        self.resume_btn.pack()
        self.save_process_btn.pack()
        self.retry_btn.pack()
        self.close_btn.pack()

    def on_resume(self):
        self.resume_btn.on_click()
        event_bus.emit("START_LOADING_RESULTS")

    def on_retry(self):
        self.retry_btn.on_click()
        event_bus.emit("START_DATA_ENRICHMENT")
    
    def on_save(self):
        self.save_process_btn.on_click(text=_("Saving progress"))
        thread = threading.Thread(target=self._on_save_logic, daemon=True)
        thread.start()
    
    def _on_save_logic(self):
        app_process.save()
        self.after(0, lambda:self._on_save_end())
    
    def _on_save_end(self):
        self.save_process_btn.on_click(text=_("Progress saved!"))

    def on_close(self):
        self.close_btn.on_click()
        event_bus.emit("NAVIGATE_TO_MENU")

    def update_gui(self):
        self.label.configure(text=_("Manager"))
        self.result_label.configure(_(f"{self.process['progress']} out of {len(self.process['songs'])} were modified"))
        self.resume_btn.configure(text=_("Resume changed files"))
        self.save_process_btn.configure(text=_("Save progress for later"))
        self.retry_btn.configure(text=_("Retry process"))