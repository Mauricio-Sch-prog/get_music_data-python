import tkinter as tk
from tkinter import ttk

class FileListContainer(tk.Frame):
    def __init__(self, parent, model):
        super().__init__(parent)
        
        self.model = model
        self.header_frame = tk.Frame(self, background="#e0e0e0", bd=1, relief="raised")
        self.header_frame.pack(side="top", fill="x")
        
        for i in range(len(model)):
            self.header_frame.columnconfigure(i, weight=1, uniform="col_group")
    
        for i, (header, options) in enumerate(model.items()):
            if not options['optional']:
                tk.Label(
                    self.header_frame, 
                    text=header.capitalize(), 
                    font=("Arial", 10, "bold"), 
                    bg="#e0e0e0", 
                    anchor="w",
                ).grid(row=0, column=i, sticky="ew")
            else:
                tk.Checkbutton(
                    self.header_frame,
                    text=header.capitalize(),
                    anchor="e",
                ).grid(row=0, column=i, sticky="w")

        
        self.content_container = tk.Frame(self)
        self.content_container.pack(side="top", fill="both", expand=True)
        
        # 1. Create the Canvas and Scrollbar
        self.canvas = tk.Canvas(self.content_container, borderwidth=0, background="#ffffff", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.content_container, orient="vertical", command=self.canvas.yview)
        

        self.scrollable_frame = tk.Frame(self.canvas, background="#ffffff")
        self.scrollable_frame_row_count = 0
        

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

  
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
  
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        for i in range(len(model)):
            self.scrollable_frame.columnconfigure(i, weight=1, uniform="col_group")
        self.scrollable_frame.columnconfigure(4, minsize=16)
        

    def _on_frame_configure(self, event):
       
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        
        self.update_idletasks()
        canvas_width = self.content_container.winfo_width()
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
        

    def add_file(self, item):
        self.scrollable_frame_row_count +=1
        row_idx = self.scrollable_frame_row_count
        
        for count, (key, value) in enumerate(self.model.items()):
        
            tk.Label(self.scrollable_frame, text=item[key], bg="#f0f0f0", anchor="w").grid(row=row_idx, column=count, sticky="ew", padx=2, pady=2)