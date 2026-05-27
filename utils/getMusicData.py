import utils.gemini as gemini
from google.genai import errors
import time
from tkinter import messagebox
from config.config import app_config

  


def get_music_data(
        songs: list, 
        callback = None, 
        progress = 0,
        data = None,
        **kwargs,
        ):

    if data is None:
        data = []
        
    batch_size = app_config.get(section="system", key="api_batch_fetch")
    api_key = app_config.get(section="system", key="api_key")

    while progress < len(songs):
        fetch = songs[progress : progress + batch_size]

        try:
            # edited_fetch = gemini.batchFetchData(musicList=fetch, api_key=api_key)
            # if edited_fetch:
            #     for count, entry in enumerate(edited_fetch, 1):
            #         entry['id'] = progress + count
            #     data.extend(edited_fetch)
            data.extend(fetch)
            
            progress += len(fetch)
            
            if callback:
                callback(progress / len(songs))

            if progress > 10:
                raise ValueError("NÂO PASSARAS!")


            time.sleep(2)

        except errors.ServerError:
            print(f"Model is overloaded at index {progress}. Waiting 30 seconds to retry this exact batch...")
            time.sleep(30)

            continue
        
        except Exception as e:
            return {"data": data, "progress": progress, "songs": songs, "success": False, "message": str(e)}

    return {"data": data, "progress": progress, "songs": songs, "success": True, "message": "Success"}

