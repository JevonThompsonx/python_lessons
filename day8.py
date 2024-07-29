"""
Some more Regex practice
"""
import re
with open('regexEx3.txt','r',encoding='utf-8') as FILE_HANDLE:
    FILE_READ = FILE_HANDLE.read()
    priceMatch = re.findall(r'\w+\:\s\$([0-9,.]+)',FILE_READ)
    priceList = []
    for price in priceMatch:
        parsedPrice = re.sub(',','',price)
        newPrice = float(parsedPrice)
        priceList.append(newPrice)
    #print(f'Prices: {priceList}')
    titleMatch = re.findall(r'Title:\s([a-zA-Z0-9- ]+)',FILE_READ)
    #print(titleMatch)

    ratingMatch = re.findall(r"Rating: ([0-9. ]+)",FILE_READ)
    TITLE_LOOP_VAR = 0
    for title in titleMatch:
        print(f"{title} is ${priceMatch[TITLE_LOOP_VAR]} with a rating of {ratingMatch[TITLE_LOOP_VAR]}")
        TITLE_LOOP_VAR += 1
    