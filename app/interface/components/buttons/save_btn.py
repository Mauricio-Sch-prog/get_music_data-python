from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import save_icon


class SaveBtn(BtnModel):
    def __init__(self, master, **kwargs):
        defaults = {
            "text": _("Save"),
            "image": save_icon
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)