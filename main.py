import io
import sys
from interface.app import App
from setConfig import init_config


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    init_config()
    App()