
from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import config_icon
from app.config.config import app_config

class ConfigBtn(BtnModel):
    def __init__(self, master, load = None, **kwargs):
        defaults = {
            "text":None,
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "text_color":app_config.get(section='theme', key='text_color'),
            "corner_radius":5, 
            "hover_color":app_config.get(section='theme', key='accent_color'),
            "image":config_icon,
            "width":40,
            "height":40,
            "border_width":None,
            "anchor":"center",  
            "border_spacing":0,
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)






