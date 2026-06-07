from app.config.config import app_config
from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import close_icon


class CloseBtn(BtnModel):
    def __init__(self, master ,**kwargs):
        defaults = {
            "text":_("Close"),
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "image":close_icon,
            "border_color":"#e74c3c", 
            "hover_color":"#e74c3c",
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
