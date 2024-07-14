import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = ROOT_DIR + "/keywords.txt"

def read_file():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            contents = file.readlines()
            return contents
    else:
        return []