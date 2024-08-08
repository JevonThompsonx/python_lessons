"""
Day 12 - trying request instead of urllib -easier 
"""

import requests
DICTIONARY_WORD = input("Give me a word to search: ")
URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{DICTIONARY_WORD}"
RESPONSE=requests.get(URL,timeout=10)
RESPONSE.raise_for_status()
DATA = RESPONSE.json()
DATA = DATA[0]
print(DATA)
print(DATA['word'])
print(DATA['phonetics'][0]['audio'])
#much easier
