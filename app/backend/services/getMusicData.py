import time

from google.genai import errors

import app.backend.services.gemini as gemini
from app.backend.utils.processManager import app_process
from app.config.config import app_config


def get_music_data():
    process = app_process.get()

    if process["data"] is None:
        process["data"] = []
        
    batch_size = app_config.get(section="system", key="api_batch_fetch")
    api_key = app_config.get(section="system", key="api_key")

    while process["progress"] < len(process["songs"]):
        fetch = process["songs"][process["progress"] : process["progress"] + batch_size]

        try:
            # edited_fetch = gemini.batchFetchData(musicList=fetch, api_key=api_key)
            # if edited_fetch:
            #     for count, entry in enumerate(edited_fetch, 1):
            #         entry['id'] = progress + count
            #     process["data"].extend(edited_fetch)
            process["data"].extend(fetch)
            
            process["progress"] += len(fetch)

            if process["progress"] > 10:
                raise ValueError("NÂO PASSARAS!")


            time.sleep(2)

        except errors.ServerError:
            print(f"Model is overloaded at index {process["data"]}. Waiting 30 seconds to retry this exact batch...")
            time.sleep(30)

            continue
        
        except Exception as e:
            app_process.update(process)
            return {"success": False, "message": str(e)}
    app_process.update(process)
    return {"success": True, "message": "Success"}

