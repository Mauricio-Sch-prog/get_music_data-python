import datetime

from app.backend.services.folderDataManager import folder_manager
from app.config.data import app_data

class ProcessManager():
    def __init__(self):
        self.process = None

    def create(self, folder_path, options):
        id = datetime.datetime.now()
        self.process={
            "id" : id.isoformat(),
            "folder_path" : folder_path,
            "songs": folder_manager.get_folder_data(folder_path),
            "progress": 0,
            "data": None,
            "options": options
        }

    def get(self):
        if self.process:
            return self.process
    
    def update(self, updated_process):
        if self.process:
            self.process.update(updated_process)

    def save(self):
        if self.process:
            app_data.add_data(key="saved_processes", value=self.process)

app_process = ProcessManager()