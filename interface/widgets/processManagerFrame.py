import customtkinter as ctk
import datetime
import threading

from config.data import app_data
from utils.getMusicData import get_music_data


from interface.widgets.loadingProcessFrame import LoadingProcessFrame
from interface.buttons._btn import Btn
from interface.buttons.resumeBtn import ResumeBtn
from interface.buttons.saveBtn import SaveBtn 
from interface.buttons.retryBtn import RetryBtn

class ProcessManagerFrame(ctk.CTkFrame):
    def __init__(
            self, 
            master, 
            process_result, 
            resume_callback, 
            retry_callback,
            folderpath ):
        super().__init__(
            master=master
        )

        self.folderpath = folderpath
        self.process_result = process_result
        self.resume_callback = resume_callback
        self.retry_callback = retry_callback
        
        self.label = ctk.CTkLabel(
            self,
            text=_("Manager")
        )

        self.result_label = ctk.CTkLabel(
            self,
            text=_(f"{process_result['progress']} out of {len(process_result['songs'])} were modified")
        )

        self.resume_btn = ResumeBtn(
            self,
            command=self._on_resume,
            text=_("Resume changed files"),
        )

        self.save_process_btn = SaveBtn(
            self,
            command=self._on_save,
            text=_("Save progress for later"),
        )

        self.retry_btn = RetryBtn(
            self,
            command=self._on_retry,
            text=_("Retry process"),
        )
        self.label.pack()
        self.result_label.pack()
        self.resume_btn.pack()
        self.save_process_btn.pack()
        self.retry_btn.pack()

    def _on_resume(self):
        self.destroy()
        self.after(0, self.resume_callback, self.process_result)

    def _on_retry(self):
        self.retry_btn.on_click()
        self.destroy()
        self.after(0, self.retry_callback, self.process_result)
    
    def _on_save(self):
        self.save_process_btn.on_click()
        self.save_process_btn.text = _("Save progress for later")
        thread = threading.Thread(target=self._on_save_logic, daemon=True)
        thread.start()
    
    def _on_save_logic(self):
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
        self.after(0, lambda:self._on_save_end())
    
    def _on_save_end(self):
        self.save_process_btn.save_finished()
