import gemini
from google.genai import errors
import time
from interface.progressBar import ProgressBar
from tkinter import messagebox

def getMusicData(songs: list, parent):
    songListData = [{'title': 'Battleworn', 'date': 0, 'artist': 'Antti Martikainen', 'album': 'Unknown Album', 'genre': 'Epic Symphonic Metal', 'file': 'Battleworn (epic symphonic metal).mp3', 'id': 1}, {'file': 'Bear Ghost - Necromancin Dancin - Lyric Video.mp3', 'genre': 'Rock', 'album': 'Unknown Album', 'date': 0, 'artist': 'Bear Ghost', 'title': 'Necromancin Dancin', 'id': 2}, {'genre': 'Eurobeat', 'file': 'BEAT OF THE RISING SUN (320 kbps).mp3', 'title': 'Beat Of The Rising Sun', 'date': 0, 'artist': 'Dave Rodgers', 'album': 'Unknown Album', 'id': 3}, {'title': "Because I'm Awesome", 'date': 0, 'artist': 'The Dollyrots', 'album': 'Unknown Album', 'genre': 'Pop Punk', 'file': "Because I'm Awesome (320 kbps).mp3", 'id': 4}, {'title': "Stayin' Alive", 'date': 0, 'artist': 'Bee Gees', 'album': 'Unknown Album', 'genre': 'Disco', 'file': "Bee Gees - Stayin' Alive (Official Music Video) (320 kbps).mp3", 'id': 5}, {'genre': 'Nu-metal', 'file': 'Before My Body Is Dry.mp3', 'title': 'Before My Body Is Dry', 'date': 0, 'artist': 'Hiroyuki Sawano (feat. Mika Kobayashi & David Whitaker)', 'album': 'NOT KNOWN', 'id': 6}, {'file': 'BIG BLAST SIDELINES (320 kbps).mp3', 'genre': 'Unknown', 'album': 'Unknown Album', 'date': 0, 'artist': 'Unknown', 'title': 'No official title found', 'id': 7}, {'date': 2014, 'artist': 'Daisuke Ishiwatari & Naoki Hashimoto', 'genre': 'Heavy Metal, Video Game Music', 'file': 'Big Blast Sonic (320 kbps).mp3', 'title': 'Big Blast Sonic', 'album': 'Guilty Gear Xrd -Sign-', 'id': 8}, {'date': 2014, 'genre': 'Video Game Music', 'artist': 'Daisuke Ishiwatari & Naoki Hashimoto', 'title': 'Birthday Train', 'album': 'Guilty Gear Xrd -Sign-', 'file': 'Birthday Train (320 kbps).mp3', 'id': 9}, {'title': 'Black Rover (Blinding Sunrise Cover)', 'album': 'Black Clover', 'file': 'BLACK CLOVER - OP3 - Black Rover __ Blinding Sunrise Cover.mp3', 'genre': 'Metalcore', 'artist': 'Blinding Sunrise (cover of Vickeblanka)', 'date': 2018, 'id': 10}, {'date': 2018, 'artist': 'Vickeblanka', 'genre': 'J-pop', 'file': 'Black Clover Opening 3 Full『Black Rover』by Vickeblanka _ Lyrics.mp3', 'title': 'Black Rover', 'album': 'Black Clover', 'id': 11}, {'title': 'Everything I Lost', 'album': 'Bleach OST', 'file': 'Bleach OST_ Everything I Lost _ Episode 16 SHINJI THEME Soundtrack_LVKOsWZm8Ms.mp3', 'genre': 'Anime Soundtrack, Orchestral', 'artist': 'Shiro Sagisu (feat. Yoko Takahashi & The London Freedom Gospel Choir)', 'date': 2005, 'id': 12}, {'genre': 'J-pop, Acid Jazz', 'artist': 'Coda', 'date': 2013, 'title': 'Bloody Stream', 'album': "JoJo's Bizarre Adventure: Battle Tendency", 'file': 'BLOODY STREAM (320 kbps).mp3', 'id': 13}, {'date': 2021, 'genre': 'Video Game Soundtrack, Instrumental', 'artist': 'HOYO-MiX (Composed by Dimeng Yuan)', 'title': 'Blossoms of Summer Night', 'album': 'Genshin Impact', 'file': 'Blossoms of Summer Night.mp3', 'id': 14}, {'title': 'Judgement', 'genre': 'Rock', 'file': 'Blue Lock - Opening 2 Full『Judgement』by Ash Da Hero (Lyrics KAN-ROM-ENG) (320 kbps).mp3', 'artist': 'ASH DA HERO', 'album': 'Judgement', 'date': 2023, 'id': 15}, {'date': 2017, 'file': 'Blumenkranz_zRI5uW6DLXg.mp3', 'artist': 'Cyua', 'album': 'Attack on Titan Season 2 Original Soundtrack', 'genre': 'Anime Song', 'title': 'Blumenkranz', 'id': 16}, {'genre': 'Synthpop, Dance Rock, Pop Rock, Ballad', 'file': 'Bonnie Tyler - Holding Out For A Hero (Official HD Video) (320 kbps).mp3', 'artist': 'Bonnie Tyler', 'album': 'Secret Dreams and Forbidden Fire', 'date': 1984, 'title': 'Holding Out For A Hero', 'id': 17}, {'title': 'Boop', 'genre': 'Soundtrack', 'file': 'Boop by Jeff Williams and Casey Lee Williams with Lyrics.mp3', 'artist': 'Jeff Williams and Casey Lee Williams', 'album': 'RWBY: Volume 2 Soundtrack', 'date': 2014, 'id': 18}, {'file': 'Break a Spell.mp3', 'artist': 'Naoki', 'album': 'Guilty Gear Xrd Rev 2 Original Soundtrack', 'genre': 'Video Game Soundtrack, Rock', 'date': 2017, 'title': 'Break a Spell', 'id': 19}, {'title': 'Snakes', 'date': 2021, 'file': 'Miyavi & PVRIS - Snakes _ Arcane League of Legends _ Riot Games Music.mp3', 'artist': 'MIYAVI & PVRIS', 'album': 'Arcane League of Legends (Soundtrack)', 'genre': 'Rock, Soundtrack', 'id': 20}, {'date': 2022, 'genre': 'Anime Opening Theme, Soundtrack', 'file': 'Mob Psycho 100 III - Opening 1.mp3', 'artist': 'MOB CHOIR', 'album': '1', 'title': '1', 'id': 21}]
    # songListData = []
  
    bar = ProgressBar(parent)
    
    
    
    # for i in range(0, len(songs), 10):
    #     fetch = songs[i : i + 10]
        
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
    
    #     bar.updateStatus(((i + 10) / len(songs)) * 100)
    #     time.sleep(4)
        
    bar.destroy()
    return songListData