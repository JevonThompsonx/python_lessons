"""
Day 11 - urllib & beautifulsoup
"""
import urllib.request as urlReq, urllib.error as urlError, urllib.parse as urlParse

with urlReq.urlopen("https://example.com") as exampleUrl:
    for line in exampleUrl:
        print(line.strip().decode())
