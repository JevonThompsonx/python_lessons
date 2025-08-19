"""
Day 13 - Beautiful soup
"""
import asyncio
from bs4 import BeautifulSoup as bs4
import httpx

URLS = [
    "http://www.dr-chuck.com/page1.html",
    "http://www.dr-chuck.com/page2.html",
]


async def GET_REQUEST(client, url):
    result = await client.get(url)
    return result.text

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(GET_REQUEST(client, url)) for url in URLS]
        results = await asyncio.gather(*tasks)
        for result in results:
            soup = bs4(result, 'html.parser')
            # print(soup)
            print(soup.title)
            print(soup.body)
asyncio.run(main())
