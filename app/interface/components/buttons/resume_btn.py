from app.config.config import app_config
from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import arrow_down_icon


class ResumeBtn(BtnModel):
    def __init__(self, master, **kwargs):
        defaults = {
            "text":_("Resume"),
            "image": arrow_down_icon,
            "border_width" : None,
            "bg_color": "transparent",
            "fg_color":app_config.get(section='theme', key='primary_color'),
            "hover_color":app_config.get(section='theme', key='success_color'),
            "text_color":app_config.get(section='theme', key='text_color'),
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
