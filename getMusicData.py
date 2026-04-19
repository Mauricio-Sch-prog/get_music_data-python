import gemini

def getSongListData(songs: list):
    songListData = []
    
    for i in range(0, len(songs), 10):
        fetch = songs[i : i + 10]
        
        editedFetch = gemini.batchFetchData(fetch)
        for count, entry in enumerate(editedFetch, 1):
            entry['id'] = i + count
        
        songListData.extend(editedFetch)
        
    return songListData