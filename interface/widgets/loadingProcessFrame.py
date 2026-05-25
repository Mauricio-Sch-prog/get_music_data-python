import customtkinter as ctk
import threading

from CTkMessagebox import CTkMessagebox
from interface.widgets.progressBar import ProgressBar 

class LoadingProcessFrame(ctk.CTkFrame):
    def __init__(self, master, process, on_complete_callback=None, **process_params):
        super().__init__(master)
        
        self.process = process
        self.process_params = process_params
        self.on_complete_callback = on_complete_callback

        self.configure(fg_color="transparent") 

        self.bar = ProgressBar(self)
        self.bar.place(relx=0.5, rely=0.5, anchor="center")

        thread = threading.Thread(target=self._run_process, daemon=True)
        thread.start()

    def _run_process(self):
        try:
            result = self.process(callback=self._route_progress_to_ui, **self.process_params)
            self.after(0, self._handle_completion, result)

        except Exception as e:
            self.after(0, self._handle_error, e)

    def _route_progress_to_ui(self, value):
        self.after(0, self._update_bar_safe, value)

    def _update_bar_safe(self, value):
        if hasattr(self, 'bar') and self.bar:
            self.bar.update_status(value) 

    def _handle_completion(self, result):
        self.destroy()
        if self.on_complete_callback:
            self.on_complete_callback(success=True, data=result, error=None)

    def _handle_error(self, error):
        self.destroy()
        CTkMessagebox(
                title=_("Something went wrong"), 
                message=error, 
                icon="cancel")

        if self.on_complete_callback:
            self.on_complete_callback(success=False, data=None, error=error)
        