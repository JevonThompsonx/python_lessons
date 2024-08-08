"""
Day 10 part 2 with urllib to simplify using sockets
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
URL_DICTIONARY = {}
with urllib.request.urlopen("http://data.pr4e.org/romeo.txt") as LINK_HANDLE:
    for line in LINK_HANDLE:
        line = line.decode().rstrip()
        for word in line.split():
            print(word)
            if word in URL_DICTIONARY:
                URL_DICTIONARY[word] += 1
            else:
                URL_DICTIONARY[word] = 1
print(URL_DICTIONARY)
