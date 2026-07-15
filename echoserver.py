import asyncio

async def handle(reader, writer):
    addr = writer.get_extra_info('peername')
    message = f"{addr!r} is connected !!!!"
    print(message)
    
    try:
        while True:
            data = await reader.read(100)
            
            # 🛠️ จุดแก้ไขที่ 1: ตรวจสอบว่า Client ตัดการเชื่อมต่อหรือไม่ (กรณี data เป็นค่าว่าง)
            if not data:
                break
                
            message = data.decode().strip()
            
            # พิมพ์ข้อความที่ฝั่ง Server ดูก่อน
            print(f"Received from {addr!r}: {message}")
            
            # ส่งข้อมูลกลับไปหา Client (Echo)
            writer.write(data)
            await writer.drain()
            
            # 🛠️ จุดแก้ไขที่ 2: ตรวจสอบคำสั่ง exit
            if message.lower() == "exit":
                break
    except Exception as e:
        print(f"Error with connection {addr!r}: {e}")
    finally:
        # บล็อกนี้จะทำงานเสมอเมื่อออกจากลูป เพื่อปิดการเชื่อมต่อให้สนิท
        print(f"{addr!r} connection is closed.")
        writer.close()
        await writer.wait_closed() # ปิด Socket อย่างปลอดภัยใน Asyncio

async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())