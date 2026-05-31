from interface.buttons._btn import BtnModel
from config.config import app_config
from interface.icons import arrow_down_icon
class ApplyChangesBtn(BtnModel):
    def __init__(self, master, **kwargs):

        defaults = {
            "text":_("Apply changes"),
            "fg_color":app_config.get(section='theme', key='secondary_color'),
            "bg_color":app_config.get(section='theme', key='secondary_color'),
            "image":arrow_down_icon,
            "border_color":"#0320fc", 
            "hover_color":"#0320fc",
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

    def update_gui(self):
        self.configure(text=_("Apply changes"))