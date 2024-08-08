"""
Day 12 - Trying httpx for async support 
"""
import asyncio
import httpx

WORD = 'dog'
URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{WORD}"
REQUEST = httpx.get(URL, timeout=10).json()
DATA = REQUEST[0]
#print(DATA['phonetics'][0]['audio'])
async def fetch_data(url):
    """
    fetches dictionary api using httpx asynchronously 
    """
    async with httpx.AsyncClient() as client:
        result = (await client.get(url))
        print(result.text)
        print('\n')
        print(result.headers)
        print('\n')
        print(result.status_code)
        return result.json()[0]

async def find_data():
    """
    Gets name and meanings from data
    """
    data = await fetch_data(URL)
    word = data['word']
    meanings = data['meanings']
    print(word)
   
async def main():
    """
    Runs all async functions
    """
    await find_data()
#asyncio.run(main())
asyncio.run(fetch_data(URL))