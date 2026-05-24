import gettext

from config.config import app_config
import sys
from pathlib import Path

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent


class LaguageSettingsManager():
    def __init__(self):
        self.app = None
        self.locale_dir = BASE_DIR / "get_music_data-python" / "locales"


    def change_laguage(self, laguage = None):
        lang_code = laguage if laguage else app_config.get(section="system", key="language")
        
        es_translations = gettext.translation(
            'base', 
            localedir=self.locale_dir, 
            languages=[lang_code], 
            fallback=True
        )
        
        es_translations.install()
        
        if self.app:
            self._update_ui()

    def set_app(self, app):
        self.app = app
    
    def _update_ui(self):
        self.app.update_gui()

laguage_settings = LaguageSettingsManager()