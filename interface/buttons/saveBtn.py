from interface.buttons._btn import BtnModel
from interface.icons import save_icon

class SaveBtn(BtnModel):
    def __init__(self, master, **kwargs):
        defaults = {
            "text": _("Save"),
            "image": save_icon
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)

    def save_finished(self):
        self.on_click(_("Saved!"))