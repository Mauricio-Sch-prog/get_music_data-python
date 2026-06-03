
from app.backend.utils import utils
from app.interface.root import Root
from app.interface.components.buttons.config_btn import ConfigBtn
import threading
from app.interface.router import Router
from app.interface.events import event_bus
from app.interface.views.config_view import ConfigView
from CTkMessagebox import CTkMessagebox
from app.backend.services.folderDataManager import folder_manager
from app.backend.services.getMusicData import get_music_data
from app.backend.utils.processManager import app_process

class App():
    def __init__(self):
        self.root = Root()

        self.router = Router(self.root)

        self.config_overlay = ConfigView(self.root, on_close_request=self.toggle_config)
        self.config_overlay.state = False
        self.config_btn = ConfigBtn(self.root, command=self.toggle_config)
        self.config_btn.place(x=10, y=10)

        event_bus.subscribe("START_FOLDER_SCAN", self.handle_folder_scan)
        event_bus.subscribe("START_DATA_ENRICHMENT", self.handle_data_enrichment)
        event_bus.subscribe("START_LOADING_RESULTS", self._load_result)
        event_bus.subscribe("START_APPLY_CHANGES", self._apply_changes)
        event_bus.subscribe("SHOW_ERROR_MESSAGE", self.display_error)

        event_bus.emit("NAVIGATE_TO_MENU")

        self.root.mainloop()

    def handle_folder_scan(self, folder_path):
        event_bus.emit("NAVIGATE_TO_LOADING", _("Scanning files..."))
        
        threading.Thread(
            target=self._bg_scan_worker, 
            args=(folder_path,), 
            daemon=True
        ).start()

    def _bg_scan_worker(self, folder_path):
        self.root.folder_path = folder_path
        folder_data = folder_manager.get_folder_data(folder_path)
        folder_data.sort(key=lambda x: x['file'].lower())
        
        self.root.after(0, lambda: self._finalize_scan(folder_data))

    def _finalize_scan(self, folder_data):
        if folder_data and len(folder_data) > 0:
            event_bus.emit("NAVIGATE_TO_FOLDER", folder_data)
        else:
            self.root.folder_path = None
            event_bus.emit("NAVIGATE_TO_MENU")
            self.display_error(_("Music folder not found or empty!"))

    def handle_data_enrichment(self):
        
        event_bus.emit("NAVIGATE_TO_LOADING", _("Talking to ai..."), 0)
        
        threading.Thread(
            target=self._bg_ai_worker, 
            daemon=True
        ).start()

    def _bg_ai_worker(self):
        response = get_music_data()
        process = app_process.get()
        self.root.after(0, lambda: self._finalize_enrichment(response, process))

    def _finalize_enrichment(self, response, process):
        if not response['success']:
            event_bus.emit("NAVIGATE_TO_POST_PROCESS", process)
            self.display_error(response['message'])
        else:
            event_bus.emit("START_LOADING_RESULTS")
  
    def _load_result(self):
        event_bus.emit("NAVIGATE_TO_LOADING", _("Loading results..."))
        
        threading.Thread(
            target=self._bg_data_fetch_worker,
            args=(), 
            daemon=True
        ).start()
    
    def _bg_data_fetch_worker(self):
        process = app_process.get()
        model = utils.get_changed_files_model(process['data'], process['options'])
        validated_files = folder_manager.check_files_exists(data=process['data'], folder_path=process['folder_path'])
        process['data'] = validated_files['present']
        app_process.update(process)

        self.root.after(0, lambda:self._finalize_load_result(process['data'], model))

    def _finalize_load_result(self, data, model):
        event_bus.emit("NAVIGATE_TO_RESULTS", data, model)

    def _apply_changes(self):
        event_bus.emit("NAVIGATE_TO_LOADING", _("Applying changes..."), 1)
        threading.Thread(
            target=self._bg_data_mod_worker,
            args=(), 
            daemon=True
        ).start()

    def _bg_data_mod_worker(self):
        process = app_process.get()
        utils.change_file_metadata(
            changed_files=process['data'],
            folder_path=process['folder_path'], 
            options=process['options']
            )
        self.root.after(0, lambda:self._finalize_changes())

    def _finalize_changes(self):
        event_bus.emit("NAVIGATE_TO_MENU")

    def display_error(self, message="Error"):
        CTkMessagebox(title=_("Error"), message=message, icon="cancel")

    def toggle_config(self):
        if self.config_overlay.state:
            self.config_overlay.state = False
            self.config_overlay.place_forget()
        else:
            self.config_overlay.state = True
            self.config_overlay.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)
            self.config_overlay.lift()
        