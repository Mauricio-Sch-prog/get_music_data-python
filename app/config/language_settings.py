import gettext

from app.config.set_config import LANGUAGE_LOCALE
from app.config.config import app_config

class LanguageSettingsManager():
    def __init__(self):
        self.update_gui_callback = None



    def change_language(self, language = None):
        lang_code = language if language else app_config.get(section="system", key="language")
        
        es_translations = gettext.translation(
            'base', 
            localedir=LANGUAGE_LOCALE, 
            languages=[lang_code], 
            fallback=True
        )
        
        es_translations.install()
        
        if self.update_gui_callback:
            self._update_gui()

    def set_update_gui_callback(self, update_gui_callback):
        self.update_gui_callback = update_gui_callback

    def _update_gui(self):
        print("updating gui")
        if self.update_gui_callback:
            self.update_gui_callback()

language_settings = LanguageSettingsManager()