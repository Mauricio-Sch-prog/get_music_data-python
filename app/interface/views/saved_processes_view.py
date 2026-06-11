import customtkinter as ctk

from app.interface.components.buttons.close_btn import CloseBtn
from app.interface.components.cards.process_card import ProcessCard
from app.interface.events import event_bus


class SavedProcessesView(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master, fg_color="transparent")
        self.data = data
        
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=20, pady=(10, 5))
        
        self.label = ctk.CTkLabel(
            self.header_frame, 
            text=_("Saved Processes"), 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack(side="left")
        
        self.close_btn = CloseBtn(self.header_frame, command=self.on_close)
        self.close_btn.pack(side="right")

        self.scroll_container = ctk.CTkScrollableFrame(
            self, 
            label_text=None,
            fg_color="transparent"
        )
        self.scroll_container.pack(fill="both", expand=True, padx=10, pady=10)


        self._load_cards()

    def _load_cards(self):
        for key, value in self.data.items():
            card = ProcessCard(self.scroll_container, value)
            card.pack(fill="x", pady=8, padx=5)

    def on_close(self):
        self.close_btn.on_click()
        event_bus.emit("NAVIGATE_TO_MENU")

    def update_gui(self):
        self.label.configure(text=_("Saved Processes"))
        self.close_btn.configure(text=_("Close"))
        for widget in self.scroll_container.winfo_children():
            widget.update_gui()