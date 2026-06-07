import customtkinter as ctk

from app.config.config import app_config
from app.interface.components.buttons._btn import BtnModel
from app.interface.components.buttons.resume_btn import ResumeBtn
from app.interface.components.icons import x_icon_2
from app.interface.events import event_bus


class ProcessCard(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(
            master, 
            corner_radius=10, 
            border_width=1,
            bg_color="transparent",
            fg_color=app_config.get(section="theme", key='list_primary_color'),
        )

        self.data = data

        self.total_songs = len(data.get('songs', []))
        self.completed_songs = data.get('progress', 0)
        self.progress_ratio = self.completed_songs / self.total_songs if self.total_songs > 0 else 0

        self.frame = ctk.CTkFrame(
            self, 
            fg_color=app_config.get(section="theme", key='list_primary_color'),
            bg_color=app_config.get(section="theme", key='list_primary_color'),
            )

        self.folder_path_label = ctk.CTkLabel(
            self.frame,
            text=data['folder_path'],
            text_color=app_config.get(section="theme", key='text_color'),
            font=ctk.CTkFont(weight="bold", size=14),
            anchor="w"
        )

        self.label = ctk.CTkLabel(
            self.frame,
            text=_(f"{self.completed_songs} out of {self.total_songs} songs modified"),
            text_color=app_config.get(section="theme", key='text_color'),
            font=ctk.CTkFont(size=12),
            anchor="w"
        ) 

        self.missing_label = ctk.CTkLabel(
            self.frame,
            text=_(f"Missing songs: {len(self.data.get('missing', []))}"),
            font=ctk.CTkFont(size=11),
            text_color=app_config.get(section="theme", key='text_color'),
            anchor="w"
        )

        self.progress_bar = ctk.CTkProgressBar(
            self.frame, 
            height=8,
            progress_color=app_config.get(section="theme", key="success_color")
            )
        self.progress_bar.set(self.progress_ratio)

        self.resume_process_btn = ResumeBtn(self.frame, command=self.on_resume)

        self.remove_process_btn = BtnModel(
            self.frame,
            text=_("Remove"),
            image=x_icon_2,
            fg_color=app_config.get(section="theme", key='list_primary_color'),
            bg_color="transparent",
            hover_color=app_config.get(section="theme", key='list_secondary_color'),
            command=self.on_remove,
        )
        


        self.frame.pack(side="left", fill="both", expand=True, padx=15, pady=10)
        self.folder_path_label.pack(fill="x", pady=(0, 2))
        self.label.pack(fill="x")
        self.missing_label.pack(fill="x", pady=(0, 5))
        self.progress_bar.pack(fill="x", pady=(5, 0))

        self.remove_process_btn.pack(side="left", padx = 4, pady = (8,0))
        self.resume_process_btn.pack(side="right", padx = 4, pady = (8,0))
        

    def on_resume(self):
        self.resume_process_btn.on_click()
        event_bus.emit("RELOAD_PROCESS", self.data['id'])

    def on_remove(self):
        self.remove_process_btn.on_click()
        event_bus.emit("REMOVE_SAVED_PROCESS", self.data['id'])
        self.destroy()

    def update_gui(self):
        self.label.configure(text=_(f"{self.completed_songs} out of {self.total_songs} songs modified")) 
        self.missing_label.configure(text=_(f"Missing songs: {len(self.data.get('missing', []))}"),)

        self.resume_process_btn.configure(text=_("Resume"))
        self.remove_process_btn.configure(text=_("Remove"))