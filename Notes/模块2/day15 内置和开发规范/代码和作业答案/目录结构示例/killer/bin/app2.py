import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.handler import start

if __name__ == '__main__':
    start()
