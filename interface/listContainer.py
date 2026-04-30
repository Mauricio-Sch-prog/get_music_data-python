import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class ListContainer(ctk.CTkFrame):
    def __init__(self, parent , model : dict, title):
        super().__init__(parent, bg_color="#200a38")
        
        self.model = {}
        
        for key, val in model.items():
            if(model[key]['optional'] == 'Ignore'):
                print(f"Removendo {key} dos headers")
                continue
            self.model[key] = model[key]
        
        print(f"Modelo: {self.model}")
        self.headers = ", ".join(self.model)
        self.data = {}
        
        
        ctk.CTkLabel(self, text=title, fg_color="#200a38", font=("Arial", 10, "bold"), anchor="w").pack(side="top")
        
        self.header_frame = ctk.CTkFrame(self, bg_color="#e0e0e0", border_width=1, border_color="gray", corner_radius=0)
        self.header_frame.pack(side="top", fill="x")
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#ffffff", label_text="")
        self.scrollable_frame.pack(side="top", fill="both", expand=True)
        
        for i in range(len(self.model)):
            self.header_frame.columnconfigure(i, weight=1, uniform="col_group")
            self.scrollable_frame.columnconfigure(i, weight=1, uniform="col_group")
    
        for i, (header, options) in enumerate(self.model.items()):
            if not options['optional']:
                ctk.CTkLabel(
                    self.header_frame, 
                    text=header.capitalize(), 
                    font=("Arial", 10, "bold"), 
                    fg_color="#cf2020",
                    bg_color="#e0e0e0", 
                ).grid(row=0, column=i, sticky="ew")
            else:
                check = self.data[header] = ctk.CTkCheckBox(
                    self.header_frame,
                    text=header.capitalize(),
                    fg_color="#cf2020",
                    command=self.get_list_data
                )
                check.grid(row=0, column=i, sticky="w")
                self.data[header] = check
                
                
        self.scrollable_frame_row_count = 0
        
        
        
    def get_list_data(self):
        
        data = {}
        for val in self.data:
            data[val] = self.data[val].get()
        print(data)

        return data

    def add_file(self, item, options = {'main': False}):
        self.scrollable_frame_row_count +=1
        row_idx = self.scrollable_frame_row_count
        
        for count, (key, value) in enumerate(self.model.items()):
            if(key in self.headers):
                if not options['main'] == key:
                    ctk.CTkLabel(self.scrollable_frame, text=item[key], bg_color="#3d3d3d").grid(row=row_idx, column=count, sticky="ew", padx=2, pady=2)
                else:
                    ctk.CTkCheckBox(self.scrollable_frame, text=item[key], bg_color="#3d3d3d").grid(row=row_idx, column=count, sticky="ew", padx=2, pady=2)