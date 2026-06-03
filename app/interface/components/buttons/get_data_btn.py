from app.interface.components.buttons._btn import BtnModel
from app.config.config import app_config
from app.interface.components.icons import arrow_right_icon
class GetDataBtn(BtnModel):
    def __init__(self, master , **kwargs):
        defaults = {
            "text":_("Get data"),
            "image":arrow_right_icon,
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "text_color":app_config.get(section='theme', key='text_color'),
            "border_color":app_config.get(section='theme', key='success_color'), 
            "hover_color":app_config.get(section='theme', key='success_color'),
            "anchor":"center",
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


