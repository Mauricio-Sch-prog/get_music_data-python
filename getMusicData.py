import gemini
from google.genai import errors
import time
from interface.widgets.progressBar import ProgressBar
from tkinter import messagebox
from config import app_config

def getMusicData(songs: list, parent):
    songListData = []
  
    bar = ProgressBar(parent)
    # for i in range(0, len(songs), 10):
    #     progress = ((i + 10) / len(songs))
    #     bar.updateStatus(progress)
    #     time.sleep(0.3)
    
    
    # for i in range(0, len(songs), app_config.get(section="system", key="api_batch_fetch")):
    #     fetch = songs[i : i + app_config.get(section="system", key="api_batch_fetch")]
        
    #     try:
    #         editedFetch = gemini.batchFetchData(fetch)
    #         if editedFetch:
    #             for count, entry in enumerate(editedFetch, 1):
    #                 entry['id'] = i + count
    #             songListData.extend(editedFetch)
    #     except errors.ServerError:
    #         print("Model is overloaded. Skipping this batch or waiting longer...")
    #         time.sleep(30)
    #         continue
        
    #     except Exception as e:
    #         bar.destroy()
    #         messagebox.showerror("Something went wrong", e)
    #         return songListData
    
    #     bar.updateStatus((i + app_config.get(section="system", key="api_batch_fetch")) / len(songs))
    #     time.sleep(4)
        
    bar.destroy()
    return songListData