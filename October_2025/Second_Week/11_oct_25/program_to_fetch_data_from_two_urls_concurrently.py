import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_data():
    url1="https://example.com"
    url2="https://httpbin.org/get"
    data1,data2 = await asyncio.gather(fetch(url1),fetch(url2))
    print(data1[:100],data2[:100])


asyncio.run(fetch_data())



