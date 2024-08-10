"""
Day 13b - creating my own asyncio loop w/o help using dictionary api
- okay with less help...
"""

import asyncio
import httpx

WORD_LIST = ["banana", "pretty", "dog", "cat"]


async def get_request(client, word):
    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    REQUEST = await client.get(URL)
    return REQUEST.text


async def collect_defs():
    async with httpx.AsyncClient() as client:
        TASKS = [asyncio.create_task(get_request(client, word)) for word in WORD_LIST]
        RESULTS = await asyncio.gather(*TASKS)
        for result in RESULTS:
            # print(result)
            print(result)
            print("\n")


asyncio.run(collect_defs())
