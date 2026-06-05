import threading

import customtkinter as ctk

from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.cards.process_card import ProcessCard
from app.interface.events import event_bus


class SavedProcessesView(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Saved processes")
        self.label.pack()
        self.data = data
        self.close_btn = CloseBtn(self, command=self.on_close)
        self.close_btn.pack()


        threading.Thread(
            target=self._load_cards,
            args=(),
            daemon=True
        ).start()

    def _load_cards(self):
        for key, value in self.data.items():
            ProcessCard(self, value).pack()

    def on_close(self):
        self.close_btn.on_click()
        event_bus.emit("NAVIGATE_TO_MENU")