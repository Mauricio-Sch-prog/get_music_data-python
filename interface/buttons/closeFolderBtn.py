from interface.buttons._btn import BtnModel
from config.config import app_config
from interface.icons import close_icon

class CloseFolderBtn(BtnModel):
    def __init__(self, master ,**kwargs):
        defaults = {
            "text":_("Close folder"),
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "image":close_icon,
            "border_color":"#fc030b", 
            "hover_color":"#fc030b",
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

    def update_gui(self):
        self.configure(text=_("Close folder"))