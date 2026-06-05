
from pathlib import Path

from mutagen import MutagenError
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3

from app.interface.events import event_bus


def get_file_metadata(folder_path, file_name):
    
    file_path = Path(folder_path) / file_name

    default_metadata = {
        'artist': "Unknown",
        'album': "Unknown",
        'genre': "Unknown",
        'title': "Unknown",
        'date': "Unknown",
    }

    if file_path.exists():
        try:
            with open(file_path, 'rb') as f:
                audio = EasyID3(f)
        
                return {
                    'artist': audio.get('artist', ['Unknown'])[0],
                    'album': audio.get('album', ['Unknown'])[0],
                    'genre': audio.get('genre', ['Unknown'])[0],
                    'title': audio.get('title', ['Unknown'])[0],
                    'date': audio.get('date', ['Unknown'])[0],
                }
        except Exception:
            return default_metadata
    else:
        print(f"File not found: {file_path}")
        return default_metadata


def change_file_metadata(folder_path, changed_files, options = False):
    original_folder_path = Path(f'{folder_path}')
    

    
    for count, entry in enumerate(changed_files):
        event_bus.emit("UPDATE_LOADING_PROGRESS", message=_(f"modifying {entry}"), progress=(count / len(changed_files)) * 100)
        # bar.updateStatus()
        file_path = original_folder_path / entry['file']
        if not file_path.exists():
            print(f'not found file path: {file_path}')
            continue
        
        try:
            
            try:
                song = EasyID3(file_path)
            except MutagenError:
                print(f"No ID3 header found for {entry['filename']}. Creating one...")
                new_tag = ID3()
                new_tag.save(file_path)
                song = EasyID3(file_path)
            
            song = EasyID3(file_path)
            for key, value in entry.items():
                if key == 'file' or key == 'id':
                    continue
                if not options[key]:
                    song[key] = str(value)
            song.save()
            
        except Exception as e:
            print(f"Error processing {entry['file']}: {e}")
        
    return


def get_changed_files_model(result, options):
    optionKeys = ", ".join(options)
    model = {}
    for key, value in result[0].items():
        if(key in optionKeys and options[key] == 1):
            model[key] = {'optional' : "Ignore"}
        else:
            model[key] = {'optional' : False}
    
    orderedModel = {}
    order = ["id", 'file', 'title', 'artist', 'genre', 'album', 'date']
    for orderKey in order:
        for key, value in model.items():
            if key in orderKey:
                orderedModel[key] = value
   
            
    return orderedModel