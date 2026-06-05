import os

from app.backend.utils import utils


class FolderDataManager:
    def get_folder_data(self, folder_path = None):
        if not folder_path:
            return []
        files = os.listdir(folder_path)
        folder_songs = [f for f in files if f.endswith(('.mp3', '.wav', '.flac'))]
        data = []
        
        for count, song in enumerate(folder_songs, 1):
            metadata = utils.get_file_metadata(folder_path=folder_path, file_name=song)
            entry = {
                "id": count,
                "file": song,
                **metadata
            }
            data.append(entry)
        print(f"\nFound {len(folder_songs)} songs:")
        return data
    
    def validate_folder(self, folder_path):
        folder_songs = self.get_folder_data(folder_path)
        if not len(folder_songs) > 0:
            return False
        else:
            return True
        
    def check_files_exists(self, data, folder_path):
        folder_songs = self.get_folder_data(folder_path)
        files_in_folder = {song["file"] for song in folder_songs}
    
        exist_in_folder = [song for song in data if song["file"] in files_in_folder]
        missing = [song for song in data if song["file"] not in files_in_folder]
    
        return {"present": exist_in_folder, "missing": missing}
    
folder_manager = FolderDataManager()