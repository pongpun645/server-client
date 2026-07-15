import aiohttp, asyncio

async def aioioio():
    async with aiohttp.ClientSession() as ses:
        # ลองเพิ่ม path /posts/1 เพื่อดึงข้อมูลโพสต์ที่ 1 มาดู
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        
        async with ses.get(url) as r:
            print('url: ', r.url)
            print('status: ', r.status)
            print('charset: ', r.charset)
            
            # ดึงข้อมูลเนื้อหาที่เป็น JSON 
            data = await r.json()
            print('--- data ---')
            print(data)

asyncio.run(aioioio())