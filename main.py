from fastapi import FastAPI
import schedule
import time
import threading
import requests
import os

app = FastAPI()

# Define ROOT_DIR and FILE_PATH first
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(ROOT_DIR, "keywords.txt")

# Read the keywords form the file and delte the content of the file after reading
def read_file():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            contents = file.readlines()
        
        # Clear the content of the file after reading
        with open(FILE_PATH, 'w') as file:
            file.write('')

        return contents
    else:
        return []


# Call the read_file function
word = read_file()
print(word)
