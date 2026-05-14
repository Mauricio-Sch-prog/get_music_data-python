
import customtkinter as ctk
from interface.widgets.headersFrame import Headers
from config import app_config

class ListContainer(ctk.CTkFrame):
    def __init__(self, parent, model: dict, title, data, options={'main': False}):
        super().__init__(parent, bg_color="#200a38")
        self.data = [item | {"status": False} for item in data]
        self.model_keys = {k: v for k, v in model.items() if v.get('optional') != 'Ignore'}
        self.options = options
        
        
        self.rows = []
        self.row_height = 35 
        self.visible_rows = 15 
        self.buffer_rows = 3     
        self.total_render = self.visible_rows + self.buffer_rows
        if len(self.data) < self.total_render:
            self.total_render = len(self.data)
        
        self.content_height = len(self.data) * self.row_height
        
        ctk.CTkLabel(self, text=title, font=("Arial", 12, "bold")).pack(pady=5)
        
        self.header_frame = Headers(self,model=self.model_keys)

        self.canvas = ctk.CTkCanvas(self, bg="#252525", highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self._scroll_sync)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.configure(scrollregion=(0, 0, 0, self.content_height))

    
        for i in range(self.total_render):
            row_widgets = self._create_row_widgets()
            obj_id = self.canvas.create_window(0, i * self.row_height, 
                                              window=row_widgets['frame'], 
                                              anchor="nw", 
                                              width=self.canvas.winfo_width())
            row_widgets['obj_id'] = obj_id
            self.rows.append(row_widgets)

        self.canvas.bind("<Configure>", self._on_resize)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel) 
        
        self._update_view()
        self.pack(fill="both", expand=True, padx=10, pady=10)

    def _create_row_widgets(self):
        frame = ctk.CTkFrame(self.canvas, fg_color="#333333", corner_radius=0, height=self.row_height)
        widgets = {'frame': frame, 'cells': []}
        
        for i, key in enumerate(self.model_keys):
            frame.columnconfigure(i, weight=1, uniform="col")
            if self.options.get('main') == key:
                w = ctk.CTkCheckBox(frame, text="")
            else:
                w = ctk.CTkLabel(frame, text="", compound="right")
            w.grid(row=0, column=i, padx=5)
            widgets['cells'].append(w)
            
        return widgets

    def _update_view(self, *args):
        scroll_top = self.canvas.yview()[0]
        start_index = int((scroll_top * self.content_height) / self.row_height)
        
        start_index = max(0, min(start_index, len(self.data) - self.total_render))

        for i in range(len(self.rows)):
            data_idx = start_index + i
            row_widgets = self.rows[i]
            
            if data_idx < len(self.data):
                item = self.data[data_idx]
                for cell_idx, key in enumerate(self.model_keys):
                        
                    widget = row_widgets['cells'][cell_idx]
                    val = str(item.get(key, ""))

                    # if item['status']:
                    #    widget.configure(bg_color=app_config['theme']['secondary_color'][0])
                    # else:
                    #    widget.configure(bg_color=app_config['theme']['primary_color'][0])
                    
                    if isinstance(widget, ctk.CTkCheckBox):
                        if item['status']:
                            widget.select()
                        else:
                            widget.deselect()
                        
                            
                        widget.configure(text=val, command=lambda idx=data_idx: self._toggle(idx))
                    else:
                        widget.configure(text=val)
                

                new_y = data_idx * self.row_height
                self.canvas.coords(row_widgets['obj_id'], 0, new_y)
                row_widgets['frame'].lift()
            else:
                self.canvas.coords(row_widgets['obj_id'], 0, -500)

    def _toggle(self, index):
        self.data[index]['status'] = not self.data[index]['status']
        self._update_view()

    def _on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
        self._update_view()

    def _on_resize(self, event):
        for row in self.rows:
            self.canvas.itemconfig(row['obj_id'], width=event.width)
        self._update_view()

    def _scroll_sync(self, first, last):

        self.scrollbar.set(first, last)
        self._update_view()

    def _get_data(self):
        files = [file for file in self.data if not file['status']]
        headers = self.header_frame._get_data()
        return (files, headers)

