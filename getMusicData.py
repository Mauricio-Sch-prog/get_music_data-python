import gemini
from interface.progressBar import ProgressBar

def getMusicData(songs: list, parent):
    songListData = []
    
    progressBar = ProgressBar(parent)
    progressBar.pack(anchor='center')
    
    
    for i in range(0, len(songs), 7):
        fetch = songs[i : i + 7]
        
        editedFetch = gemini.batchFetchData(fetch)
        for count, entry in enumerate(editedFetch, 1):
            entry['id'] = i + count
        songListData.extend(editedFetch)
        progressBar.updateStatus(((i + 7) / len(songs)) * 100)
        
        
    return songListData