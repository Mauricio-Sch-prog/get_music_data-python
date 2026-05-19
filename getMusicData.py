import gemini
from google.genai import errors
import time
from interface.widgets.progressBar import ProgressBar
from tkinter import messagebox
from config import app_config

def getMusicData(songs: list, parent):
    songListData = []
    songListData = [{'title': 'Elfland', 'date': 2020, 'genre': 'Video Game Soundtrack', 'album': 'Otherworld Legends OST', 'file': 'Otherworld Legends OST - Elfland Theme.mp3', 'artist': 'Elecrystal Studio', 'id': 1, 'status': False}, {'title': 'Human', 'file': "Rag'N'Bone Man - Human [Tradução] (Clipe Oficial) ᴴᴰ.mp3", 'artist': "Rag'n'Bone Man", 'date': 2016, 'genre': 'Soul, Alternative Rock, Blues, Pop', 'album': 'Human', 'id': 2, 'status': False}, {'title': 'Master of Tartarus -Reload-', 'file': 'Persona 3 Reload - Master of Tartarus -Reload- (320 kbps).mp3', 'artist': 'Shoji Meguro, Atlus Sound Team', 'date': 2024, 'genre': 'J-Rock, Video Game Soundtrack', 'album': 'Persona 3 Reload Original Soundtrack', 'id': 3, 'status': False}, {'date': 2015, 'genre': 'J-Pop, Hip-Hop, Video Game Soundtrack', 'album': 'Persona 3 The Movie #3: Falling Down OST', 'file': 'Light In Starless Sky - Persona 3 The Movie.mp3', 'artist': 'Lotus Juice, Yumi Kawamura, Shoji Meguro', 'title': 'Light in Starless Sky', 'id': 4, 'status': False}, {'title': 'Crystals', 'date': 2012, 'genre': 'Electronic, Synthwave, Video Game Music, Soundtrack', 'album': 'Hotline Miami Official Soundtrack', 'file': "M.O.O.N. - 'Crystals' [Hotline Miami Soundtrack]_AVblOqZBlJw.mp3", 'artist': 'M|O|O|N', 'id': 5, 'status': False}, {'date': 1978, 'genre': 'Pop Rock, Power Pop, Hard Rock', 'album': 'Jazz', 'file': "Queen - Don't Stop Me Now (Official Video) (320 kbps).mp3", 'artist': 'Queen', 'title': "Don't Stop Me Now", 'id': 6, 'status': False}, {'date': 2013, 'genre': 'Symphonic Metal', 'album': 'RWBY Volume 1 Soundtrack', 'file': 'RWBY - I Burn (feat. Rena) 【Intense Symphonic Metal Cover】.mp3', 'artist': 'Jeff Williams, Casey Lee Williams, Lamar Hall', 'title': 'I Burn', 'id': 7, 'status': False}, {'title': 'Rell, the Iron Maiden (Champion Theme)', 'date': 2020, 'genre': 'Video Game Soundtrack', 'album': 'League of Legends: Rell, the Iron Maiden (Original Game Soundtrack)', 'file': 'Rell, The Iron Maiden Champion Theme (ft. Ecca Vandal) - League of Legends.mp3', 'artist': 'League of Legends, Ecca Vandal', 'id': 8, 'status': False}, {'date': 2017, 'genre': 'Acid Jazz, J-Pop, Video Game Soundtrack', 'album': 'Persona 5 Original Soundtrack', 'file': 'Persona 5 OST 102 - Freedom and Security_byTldJdeg3M.mp3', 'artist': 'Shoji Meguro, Lyn Inaizumi', 'title': 'Freedom and Security', 'id': 9, 'status': False}, {'title': '99.9', 'date': 2019, 'genre': 'J-Pop, Anime Soundtrack', 'album': '99.9', 'file': 'Mob Psycho 100 Season 2 Opening Full『MOB CHOIR feat sajou no hana 99 9』【ENG Sub】(2).mp3', 'artist': 'MOB CHOIR feat. sajou no hana', 'id': 10, 'status': False}, {'file': 'Persona 5 The Phantom X OST - Ambitions and Visions_fDHPTOKxRw8.mp3', 'artist': 'Lyn Inaizumi, Ryota Kozuka, ATLUS Sound Team', 'date': 2024, 'genre': 'J-Pop, Video Game Soundtrack', 'album': 'Persona 5 The Phantom X Original Soundtrack', 'title': 'Ambitions and Visions', 'id': 11, 'status': False}, {'title': "Ballad of the Outlaw (Logan's theme)", 'date': 2020, 'genre': 'Video Game Soundtrack', 'album': 'Otherworld Legends OST', 'file': 'Otherworld Legends OST - Logan Boss Theme ll #CBOST.mp3', 'artist': 'Elecrystal Studio', 'id': 12, 'status': False}, {'genre': 'Heavy Metal, Power Metal', 'album': 'Grasp of the Undying', 'date': 2017, 'title': 'Tear of the Goddess', 'file': 'Pentakill - Tear of the Goddess [OFFICIAL AUDIO] _ League of Legends Music (320 kbps).mp3', 'artist': 'Pentakill', 'id': 13, 'status': False}, {'date': 2018, 'title': 'Monster Surprised You', 'file': 'Monster Surprised You - Xenoblade Chronicles 2 OST [084] (320 kbps).mp3', 'artist': 'Kenji Hiramatsu', 'genre': 'Video Game Soundtrack / Instrumental', 'album': 'Xenoblade Chronicles 2 Original Soundtrack', 'id': 14, 'status': False}, {'artist': 'Red Hot Chili Peppers', 'title': 'Parallel Universe', 'file': 'Parallel Universe.mp3', 'date': 1999, 'album': 'Californication', 'genre': 'Alternative Rock, Progressive Rock, Hard Rock', 'id': 15, 'status': False}, {'album': 'Persona 4 The Golden Animation Original Soundtrack', 'genre': 'J-Pop / Anime Soundtrack', 'date': 2014, 'artist': 'Shihoko Hirata', 'title': 'Next Chance to Move On', 'file': 'Next Chance to Move On_4qcAXBg5yGo.mp3', 'id': 16, 'status': False}, {'genre': 'Anime Soundtrack / J-Pop', 'album': 'Persona 5 The Animation Original Soundtrack', 'date': 2018, 'title': 'Found a Light', 'file': 'Persona 5 The Animation - Found a light (Subtitled) (320 kbps).mp3', 'artist': 'Lyn Inaizumi', 'id': 17, 'status': False}, {'album': 'Paradise', 'genre': 'J-Pop / Pop / Hip-Hop', 'date': 2019, 'artist': 'Rude-α', 'title': 'Paradise', 'file': 'Rude-α 『Paradise』.mp3', 'id': 18, 'status': False}, {'date': 2017, 'artist': 'ATLUS Sound Team', 'title': 'Price', 'file': 'P5 OST 52 Price (320 kbps).mp3', 'album': 'Persona 5 Original Soundtrack', 'genre': 'Video Game Soundtrack / Acid Jazz', 'id': 19, 'status': False}, {'genre': 'Video Game Soundtrack / J-Pop / Acid Jazz', 'album': 'Persona 5 Strikers Original Soundtrack', 'date': 2020, 'title': 'Axe to Grind', 'file': 'P5S OST 17 Axe to Grind (320 kbps).mp3', 'artist': 'Lyn Inaizumi', 'id': 20, 'status': False}]
    batch_size = app_config.get(section="system", key="api_batch_fetch")
    api_key = app_config.get(section="system", key="api_key")
  
    bar = ProgressBar(parent)
    # for i in range(0, 3000, 10):
    #     progress = ((i + 10) / 3000)
    #     bar.updateStatus(progress)
    #     time.sleep(0.3)
    
    
    # for i in range(0, len(songs), batch_size):
    #     fetch = songs[i : i + batch_size]
        
    #     try:
    #         editedFetch = gemini.batchFetchData(musicList= fetch, api_key = api_key)
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
    
    #     bar.updateStatus((i + batch_size) / len(songs))
    #     time.sleep(4)
        
    bar.destroy()
    return songListData