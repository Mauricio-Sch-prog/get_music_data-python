import customtkinter as ctk
from config import app_config

class Headers(ctk.CTkFrame):
    def __init__(self, master, model, **kwargs):
        super().__init__(master=master, height=30, fg_color="#252525")
        self.pack(fill="x")
        self.data = {}
        self.primaryColor = app_config['theme']['primary_color'][0]
        self.secondaryColor = app_config['theme']['secondary_color'][0]
        self.hoverColor = app_config['theme']['accent_color'][0]

        for i, (key, value) in enumerate(model.items()):
            self.data[key] = False
            self.columnconfigure(i, weight=1, uniform="col")

            label = ctk.CTkLabel(self, text=key.capitalize(),fg_color=self.primaryColor)
            label.grid(row=0, column=i)

            if value['optional']:   
                def command(label, target=key):
                    self.data[target] = not self.data[target]
                    if self.data[target]:
                        label.color = self.secondaryColor
                    else:
                        label.color = self.primaryColor
   
                label.hover_color = "#411313"
                label.color = self.primaryColor
                label.command = command

                def _on_enter(event, b=label):
                    b.configure(fg_color=self.hoverColor )

                def _on_leave(event, b=label):
                    b.configure(fg_color=b.color)

                def _on_click(event, b=label):
                    if hasattr(b, 'command') and callable(b.command):
                        b.command(label=b) 
                
                label.bind("<Enter>", _on_enter)
                label.bind("<Leave>", _on_leave)
                label.bind("<Button-1>", _on_click)
                label.configure(cursor="hand2")
        
    def _get_data(self):
        return self.data