import os
import io
import sys
import musicbrainzngs
from operator import itemgetter
import re


from tkinter import Tk, filedialog

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
musicbrainzngs.set_useragent("get_music_data-python", "0.1", "https://github.com/Mauricio-Sch-prog/get_music_data-python")

editedMusicList = []
generalGenreList = [
  "acoustic", "afrobeats", "alternative", "ambient", "americana", 
  "art-pop", "atmospheric-black-metal", "avant-garde", "baroque", "bebop", 
  "big-band", "black-metal", "bluegrass", "blues", "blues-rock", 
  "bossa-nova", "bounce", "breakbeat", "britpop", "bubblegum-pop", 
  "chamber-pop", "chicago-house", "chillwave", "city-pop", "classic-rock", 
  "classical", "contemporary-rnb", "cool-jazz", "country", "country-rock", 
  "crust-punk", "cyberpunk", "dance", "dancehall", "dark-ambient", 
  "dark-wave", "death-metal", "deathcore", "deep-house", "delta-blues", 
  "desert-rock", "disco", "doom-metal", "downtempo", "dream-pop", 
  "drill", "drum-and-bass", "dub", "dubstep", "edm", 
  "electro-swing", "electronic", "electronica", "emo", "enka", 
  "ethereal-wave", "eurodisco", "experimental", "fado", "flamenco", 
  "folk", "folk-rock", "free-jazz", "funk", "future-bass", 
  "g-funk", "garage-rock", "ghetto-house", "glitch", "gospel", 
  "gothic-rock", "grime", "grunge", "hard-bop", "hard-rock", 
  "hardcore-punk", "hardstyle", "heavy-metal", "highlife", "hip-hop", 
  "honky-tonk", "house", "hyperpop", "idm", "indie", 
  "indie-folk", "indie-pop", "industrial", "italo-disco", "j-pop", 
  "j-rock", "jazz", "jazz-fusion", "k-pop", "krautrock", 
  "latin", "latin-jazz", "lo-fi", "lo-fi-hip-hop", "madchester", 
  "math-rock", "melodic-death-metal", "metal", "minimal-techno", "mpb", 
  "neo-psychedelia", "neo-soul", "new-age", "new-wave", "no-wave", 
  "noise-rock", "nu-metal", "outlaw-country", "outrun", "p-funk", 
  "phonk", "pop", "pop-punk", "pop-rock", "post-hardcore", 
  "post-punk", "post-rock", "power-metal", "power-pop", "progressive-house", 
  "progressive-rock", "psychedelic-rock", "psytrance", "punk", "reggae", 
  "reggaeton", "rhythm-and-blue", "rock", "rock-and-roll", "rockabilly", 
  "roots-reggae", "salsa", "samba", "shoegaze", "ska", 
  "skate-punk", "smooth-jazz", "soul", "southern-rock", "space-rock", 
  "speed-metal", "stoner-rock", "surf-rock", "symphonic-metal", "symphonic-rock", 
  "synth-pop", "synthwave", "techno", "thrash-metal", "trance", 
  "trap", "trip-hop", "tropicalia", "uk-garage", "vaporwave", 
  "viking-metal", "visual-kei", "west-coast-hip-hop", "witch-house", "worldbeat", 
  "yacht-rock"
]

forbiddenKeyWords = [
    "amv",
    "lyrics",
    "kbps",
    "mp4",
    "mp3"
]

def clean_text(input_string, keywords):

    pattern = '|'.join(map(re.escape, keywords))
 
    cleaned_x = re.sub(pattern, '', input_string, flags=re.IGNORECASE)
    
    return ' '.join(cleaned_x.split())


def getGenre(tags):
    
    # print(sor)
    genre = False
    
    if tags: 
        sortedTags = sorted(tags, key=itemgetter('count'), reverse=True)
        for tag in sortedTags:
            if tag["name"] in generalGenreList:
                genre = tag["name"]
                break
            
        if not genre:
            genre = sortedTags[0]['name']
    else:
        genre = "undefined"
    
    return genre
    # return sortedTags

def select_music_folder():

    root = Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory(title="Select your Music Folder")

    if folder_selected:
        print(f"Selected: {folder_selected}")
        
        # List all files in the folder
        files = os.listdir(folder_selected)
        
        # Filter for music files (mp3, wav)
        songs = [f for f in files if f.endswith(('.mp3', '.wav', '.flac'))]
        
        print(f"\nFound {len(songs)} songs:")
        for count, song in enumerate(songs, 1):
            songData = searchMusic(song)
            print(songData)
            editedMusicList.append({
                "count": count,
                "file": song,
                "title": songData['title'],
                "author" : songData['artist-credit'][0]["artist"]['name'],
                "genre" : getGenre(songData["artist-credit"][0]["artist"].get("tag-list")),
            })
                

            
    else:
        print("No folder selected.")


def searchMusic(name):
    
    search_results = musicbrainzngs.search_recordings( recording=clean_text(name,forbiddenKeyWords))
    for entry in search_results['recording-list']:
        print("<--------------------->")
        print(entry)

    if search_results['recording-list']:
        first_match = search_results['recording-list'][0]
        song_id = first_match['id']
        data = musicbrainzngs.get_recording_by_id(song_id, ["artists", "tags"])
        musicData = data["recording"]
        return musicData
        
        
    return 

if __name__ == "__main__":
    # select_music_folder()
    data = searchMusic("HEAVY DAY (320 kbps).mp3")
    
    
    
    # print(editedMusicList)
    # for song in editedMusicList:
    #     print(f"\n<-------{song['title']}---------->")
    #     print(f"id {song['count']}")
    #     print(f"file name: {song['file']}")
    #     print(f"author: {song['author']}")
    #     print(f"genre: {song['genre']}")
    #     print(f"<---------->")
    
    
    