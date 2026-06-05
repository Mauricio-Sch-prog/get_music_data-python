import customtkinter as ctk

from app.config.config import app_config
from app.interface.components.icons import check_icon, x_icon


class HeadersCard(ctk.CTkFrame):
    def __init__(self, master, model, **kwargs):
        super().__init__(
            master=master, 
            height=30, 
            fg_color=app_config.get(section="theme", key='list_primary_color'),
            bg_color=app_config.get(section="theme", key='list_primary_color'),
            )
        self.pack(fill="x")
        self.data = {}
        self.primaryColor = app_config.get(section='theme', key='list_primary_color')
        self.secondaryColor = app_config.get(section='theme', key='secondary_color')
        self.hoverColor = app_config.get(section='theme', key='accent_color')
        self._get_header_text()
        
        for i, (key, value) in enumerate(model.items()):
            self.data[key] = False
            self.columnconfigure(i, weight=1, uniform="col")

            frame = ctk.CTkFrame(
                self,
                height=15,
                fg_color=self.primaryColor, 
                bg_color=self.primaryColor, 
                corner_radius=0,
            )
            frame.key = key

            frame.image_display = ctk.CTkLabel(
                frame,    
                text="",
                image=check_icon if value['optional'] else None,
                )
            
            frame.label_display = ctk.CTkLabel(
                frame, 
                text=self.header_text[key].capitalize(),
                )
            
            

            

            if value['optional']:   
                frame.image_display.pack(side="left", expand=True, anchor="e", padx=(0, 8))
                frame.hover_color = "#411313"
                frame.color = self.primaryColor

                def command(frame, image, target=key):
                    self.data[target] = not self.data[target]
                    if self.data[target]:
                        frame.color = self.primaryColor
                        image.configure(image = x_icon)
                    else:
                        frame.color = self.primaryColor
                        image.configure(image = check_icon)
                frame.command = command
   

                def _on_enter(event, b=frame):
                    b.configure(fg_color=self.hoverColor )

                def _on_leave(event, b=frame):
                    b.configure(fg_color=b.color)

                def _on_click(event, b=frame, c=frame.image_display):
                    if hasattr(b, 'command') and callable(b.command):
                        b.command(frame=b, image=c) 
                
                frame.bind("<Enter>", _on_enter)
                frame.bind("<Leave>", _on_leave)
                frame.bind("<Button-1>", _on_click)
                frame.configure(cursor="hand2")
                
                frame.image_display.bind("<Enter>", _on_enter)
                frame.image_display.bind("<Leave>", _on_leave)
                frame.image_display.bind("<Button-1>", _on_click)
                frame.image_display.configure(cursor="hand2")
                
                frame.label_display.bind("<Enter>", _on_enter)
                frame.label_display.bind("<Leave>", _on_leave)
                frame.label_display.bind("<Button-1>", _on_click)
                frame.label_display.configure(cursor="hand2")
                
            frame.label_display.pack(
                side="left" if value['optional'] else None, 
                expand=True, 
                anchor="w" if value['optional'] else None)
            frame.grid(row=0, column=i, sticky="NSEW")
            

    def _get_header_text(self):
        self.header_text = {
            'id' : 'id', 
            'file' : _('file'), 
            'title' : _('title'), 
            'artist' : _('artist'), 
            'genre' : _('genre'), 
            'album' : _('album'), 
            'date' : _('date')
        }
        
    def _get_data(self):
        return self.data
    
    def update_gui(self):
        self._get_header_text()

        for widget in self.winfo_children():
            widget.label_display.configure(text = self.header_text[widget.key].capitalize())
