import io
import sys
import interface.interface as interface

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == "__main__":
    interface.loadWindow()