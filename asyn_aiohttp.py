import aiohttp, asyncio

async def aioioio():
    async with aiohttp.ClientSession() as ses:
        url = 'https://jsonplaceholder.typicode.com'
        async with ses.get(url) as r:
            print('url: ',r.url)
            print('status: ',r.status)
            print('charset: ',r.charset)

asyncio.run(aioioio())