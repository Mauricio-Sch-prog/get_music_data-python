import io
import sys
from app.config.set_config import init_config
from app.interface.app import App


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


if __name__ == "__main__":
    init_config()
    app = App()