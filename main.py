import io
import sys
from interface.app import App
from config import start_settings

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    start_settings()
    App()