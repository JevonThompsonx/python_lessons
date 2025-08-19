"""
Day 13b - creating my own asyncio loop w/o help using dictionary api
- okay with less help...
"""

import asyncio
import httpx

WORD_LIST = ["banana", "pretty", "dog", "cat"]


async def get_request(client, word):
    """
    gets request from given link with given client
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    request = await client.get(url)
    return request.text


async def collect_defs():
    """
    Gathers all the requests from the given word list
    """
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(get_request(client, word)) for word in WORD_LIST]
        results= await asyncio.gather(*tasks)
        for result in results:
            # print(result)
            print(result)
            print("\n")


asyncio.run(collect_defs())
