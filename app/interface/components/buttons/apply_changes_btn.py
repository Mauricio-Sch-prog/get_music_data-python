from app.config.config import app_config
from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import arrow_down_icon


class ApplyChangesBtn(BtnModel):
    def __init__(self, master, **kwargs):

        defaults = {
            "text":_("Apply changes"),
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "image":arrow_down_icon,
            "border_color":app_config.get(section='theme', key='success_color'), 
            "hover_color":app_config.get(section='theme', key='success_color'),
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


        