import customtkinter as ctk
from config import app_config
from interface.widgets.icons import check_icon
from interface.widgets.icons import x_icon

class Headers(ctk.CTkFrame):
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

            image = ctk.CTkLabel(
                frame,    
                text="",
                image=check_icon if value['optional'] else None,
                )
            
            label = ctk.CTkLabel(
                frame, 
                text=key.capitalize(),
                )
            
            

            

            if value['optional']:   
                image.pack(side="left", expand=True, anchor="e", padx=(0, 8))
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

                def _on_click(event, b=frame, c=image):
                    if hasattr(b, 'command') and callable(b.command):
                        b.command(frame=b, image=c) 
                
                frame.bind("<Enter>", _on_enter)
                frame.bind("<Leave>", _on_leave)
                frame.bind("<Button-1>", _on_click)
                frame.configure(cursor="hand2")
                
                image.bind("<Enter>", _on_enter)
                image.bind("<Leave>", _on_leave)
                image.bind("<Button-1>", _on_click)
                image.configure(cursor="hand2")
                
                label.bind("<Enter>", _on_enter)
                label.bind("<Leave>", _on_leave)
                label.bind("<Button-1>", _on_click)
                label.configure(cursor="hand2")
                
            label.pack(
                side="left" if value['optional'] else None, 
                expand=True, 
                anchor="w" if value['optional'] else None)
            frame.grid(row=0, column=i, sticky="NSEW")
            
        
    def _get_data(self):
        return self.data