from interface.buttons._btn import BtnModel
from interface.icons import repeat_icon

class RetryBtn(BtnModel):
    def __init__(self, master, **kwargs):
        defaults = {
            "text": _("Retry"),
            "image": repeat_icon
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
