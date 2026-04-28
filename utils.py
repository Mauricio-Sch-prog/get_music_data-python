import os
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen import MutagenError
from interface.progressBar import ProgressBar


def getFolderData(path):
    
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
            date = audio.get('date', ['Unknown'])[0]

            return {
                'artist': artist,
                'album': album,
                'genre': genre,
                'title': title,
                'date' : date,
            }
            
            
        except Exception:
            return {
                'artist': "Unknown",
                'album': "Unknown",
                'genre': "Unknown",
                'title': "Unknown",
                'date' : "Unknown",
            }
        
    else:
        print("File not found.")
        
    return


def change_file_metadate(folder_path, changed_files, parent, options = False, ):
    original_folder_path = Path(f'{folder_path}')
    bar = ProgressBar(parent)
    
    for count, entry in enumerate(changed_files):
        bar.updateStatus((count / len(changed_files)) * 100)
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
        
    bar.destroy()
    return