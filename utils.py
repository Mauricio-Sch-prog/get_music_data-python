import os
from pathlib import Path
from mutagen.easyid3 import EasyID3


def getFolderData(path):
    print(f"Selected: {path}")
    
    files = os.listdir(path)
    
    songs = [f for f in files if f.endswith(('.mp3', '.wav', '.flac'))]
    
    songsWithId = []
    
    for count, song in enumerate(songs, 1):
        entry = {
            "id": count,
            "file": song
        }
        songsWithId.append(entry)
    print(f"\nFound {len(songs)} songs:")
    return songsWithId
            
            
            

def get_file_metadata(folder_path, file_name):

    file_path = Path(F'{folder_path}/{file_name}')
    if file_path.exists():
        try:
            audio = EasyID3(file_path)
    
            artist = audio.get('artist', ['Unknown'])[0]
            album = audio.get('album', ['Unknown'])[0]
            genre = audio.get('genre', ['Unknown'])[0]
            title = audio.get('title', ['Unknown'])[0]

            return {
                'artist': artist,
                'album': album,
                'genre': genre,
                'title': title
            }
            
            
        except Exception as e:
            print(e)
            return {
                'artist': "Unknown",
                'album': "Unknown",
                'genre': "Unknown",
                'title': "Unknown"
            }
        
    else:
        print("File not found.")
        
    return
