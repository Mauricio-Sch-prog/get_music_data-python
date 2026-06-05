from app.config.language_settings import language_settings
from app.interface.events import event_bus
from app.interface.views.folder_list_view import FolderListView
from app.interface.views.loading_view import LoadingView
from app.interface.views.main_menu_view import MainMenuView
from app.interface.views.process_manager_view import ProcessManagerView
from app.interface.views.result_list_view import ResultListView
from app.interface.views.saved_processes_view import SavedProcessesView


class Router:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        language_settings.set_update_gui_callback(self._update_gui)

        event_bus.subscribe("NAVIGATE_TO_MENU", self.show_menu)
        event_bus.subscribe("NAVIGATE_TO_LOADING", self.show_loading)
        event_bus.subscribe("UPDATE_LOADING_PROGRESS", self.update_loading_bar_progress)
        event_bus.subscribe("NAVIGATE_TO_FOLDER", self.show_folder)
        event_bus.subscribe("NAVIGATE_TO_POST_PROCESS", self.show_manager)
        event_bus.subscribe("NAVIGATE_TO_RESULTS", self.show_results)
        event_bus.subscribe("NAVIGATE_TO_SAVED_PROCESSES", self.show_saved_processes)

    def _clear(self):
        if self.current_view:
            self.current_view.destroy()

    def _update_gui(self):
        if self.current_view:
            self.current_view.update_gui()

    def show_menu(self):
        self._clear()
        self.current_view = MainMenuView(self.root)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))

    def show_loading(self, message="Processing...", progress = None):
        self._clear()
        self.current_view = LoadingView(self.root, text=message, progress= progress)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))

    def update_loading_bar_progress(self, message=None, progress=None):
        self.current_view.update_bar(progress=progress, text=message)

    def show_folder(self, data):
        self._clear()
        self.current_view = FolderListView(self.root, data=data)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))

    def show_manager(self, process):
        self._clear()
        self.current_view = ProcessManagerView(self.root, process=process)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))

    def show_results(self, data, model):
        self._clear()
        self.current_view = ResultListView(self.root, data, model)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))

    def show_saved_processes(self, data):
        self._clear()
        self.current_view = SavedProcessesView(self.root, data)
        self.current_view.pack(fill="both", expand=True, padx=20, pady=(60, 20))
 