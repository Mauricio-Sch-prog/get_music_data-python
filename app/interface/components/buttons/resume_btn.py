from app.interface.components.buttons._btn import BtnModel
from app.interface.components.icons import resume_icon


class ResumeBtn(BtnModel):
    def __init__(self, master, **kwargs):
        defaults = {
            "text": _("Resume"),
            "image": resume_icon
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
