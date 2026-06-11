import threading

import customtkinter as ctk

from app.backend.utils.processManager import app_process
from app.config.config import app_config
from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.buttons.resume_btn import ResumeBtn
from app.interface.components.buttons.retry_btn import RetryBtn
from app.interface.components.buttons.save_btn import SaveBtn
from app.interface.events import event_bus


class ProcessManagerView(ctk.CTkFrame):
    def __init__(self, master, process):
        super().__init__(
            master, 
            fg_color="transparent",
            )
        self.process = process
        
        BUTTON_WIDTH = 220

        self.total_songs = len(process.get('songs', []))
        self.completed_songs = process.get('progress', 0)
        self.progress_ratio = self.completed_songs / self.total_songs if self.total_songs > 0 else 0


        self.frame = ctk.CTkFrame(
            self,
            fg_color=app_config.get(section="theme", key="list_primary_color"),
            bg_color="transparent",
        )

        self.label = ctk.CTkLabel(
            self.frame,
            text=_("Manager"),
            font=ctk.CTkFont(size=18, weight="bold")
        )

        self.result_label = ctk.CTkLabel(
            self.frame,
            text=_("{completed} out of {total} were modified")
            .format(
                completed=self.completed_songs,
                total=self.total_songs,
            ),
            font=ctk.CTkFont(size=13)
        )

        self.progress_bar = ctk.CTkProgressBar(
            self.frame, 
            height=8,
            progress_color=app_config.get(section="theme", key="success_color")
            )
        self.progress_bar.set(self.progress_ratio)

        self.resume_btn = ResumeBtn(
            self.frame,
            command=self.on_resume,
            text=_("Resume changed files"),
            width=BUTTON_WIDTH
        )

        self.save_process_btn = SaveBtn(
            self.frame,
            command=self.on_save,
            text=_("Save progress for later"),
            fg_color=app_config.get(section="theme", key="list_primary_color"),
            hover_color=app_config.get(section='theme', key='list_secondary_color'),
            width=BUTTON_WIDTH
        )

        self.retry_btn = RetryBtn(
            self.frame,
            command=self.on_retry,
            text=_("Retry process"),
            fg_color=app_config.get(section="theme", key="list_primary_color"),
            hover_color=app_config.get(section='theme', key='list_secondary_color'),
            width=BUTTON_WIDTH
        )

        self.close_btn = CloseBtn(
            self.frame,
            fg_color=app_config.get(section="theme", key="list_primary_color"),
            command=self.on_close,
            width=BUTTON_WIDTH
        )
        

        self.frame.pack()
        self.label.pack(pady=(20, 5), padx=20)
        self.result_label.pack(pady=(0,10), padx=20)
        self.progress_bar.pack(fill="x", pady=(0,20), padx=10)
        self.resume_btn.pack(pady=6, padx=20)
        self.save_process_btn.pack(pady=6, padx=20)
        self.retry_btn.pack(pady=6, padx=20)
        self.close_btn.pack(pady=(15, 20), padx=20)

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
        self.result_label.configure(
            text=_("{completed} out of {total} were modified")
            .format(
                completed=self.completed_songs,
                total=self.total_songs,
            )
        )
        self.resume_btn.configure(text=_("Resume changed files"))
        self.save_process_btn.configure(text=_("Save progress for later"))
        self.retry_btn.configure(text=_("Retry process"))