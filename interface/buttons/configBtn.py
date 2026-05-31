
from interface.buttons._btn import BtnModel
from interface.widgets.configFrame import ConfigFrame
from interface.icons import config_icon
from config.config import app_config

class ConfigBtn(BtnModel):
    def __init__(self, master, load = None, **kwargs):
        self.load = load
        self.config_frame = ConfigFrame(master)
        self.config_frame.state = False

        defaults = {
            "command":self._toggle_config,
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

    def _toggle_config(self):
        self.config_frame.state = not self.config_frame.state
        if self.config_frame.state:
            self.config_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)
            self.config_frame.lift()
        else:
            self.config_frame.place_forget()





