import os
import io
import sys
import gemini


from tkinter import Tk, filedialog

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

editedMusicList = []
def select_music_folder():

    root = Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory(title="Select your Music Folder")

    if folder_selected:
        print(f"Selected: {folder_selected}")
        
        files = os.listdir(folder_selected)
        
        songs = [f for f in files if f.endswith(('.mp3', '.wav', '.flac'))]
        
        print(f"\nFound {len(songs)} songs:")
        return songs
                

            
    else:
        print("No folder selected.")

if __name__ == "__main__":
    
    songs = select_music_folder()
    
    if songs:
        modifiedSongs = gemini.putAitoWork(songs)
        print(" MODIFIED SONG LIST")
        print(modifiedSongs)
        for song in modifiedSongs:
            print("<------------------------------------>")
            print(song['title'])
            print(song['file'])
            print(song['author'])
            print(song['genre'])
    
        
    