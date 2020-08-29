import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # my Project Root
try:
    LOG_PATH = os.mkdir(f'{ROOT_DIR}\logs')
except FileExistsError:
    LOG_PATH = f'{ROOT_DIR}\logs'

#print(ROOT_DIR)
#print(LOG_PATH)


