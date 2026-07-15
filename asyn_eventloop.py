import asyncio

async def hanlek(a,b):
    print('%s/%s'%(a,b))
    return a/b

loop = asyncio.get_event_loop() # สร้างอีเวนต์ลูป
phonhan = loop.run_until_complete(hanlek(7,6)) # เอาอีเวนต์ลูปมารัน
print('ผลลัพธ์: %.3f'%phonhan)