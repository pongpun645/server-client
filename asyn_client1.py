from socketio import AsyncClient
import asyncio
from aioconsole import ainput

# การตั้งค่าพื้นฐาน
IpAddress = '127.0.0.1' 
PORT = '9000' # **เช็คให้ตรงกับพอร์ตฝั่ง Server**
clientName = 'Deadpool'
roomName = 'Marvel'

sio = AsyncClient()
FullIp = f'http://{IpAddress}:{PORT}'

@sio.event
async def connect():
    print('Connected to server')
    await sio.emit('join_chat', {'room': roomName, 'name': clientName})

@sio.event
async def get_message(message):
    if clientName == message['from']:
        print('You : ' + message['message'])
    else:
        print(message['from'] + ' : ' + message['message'])

async def send_message():
    while True:
        await asyncio.sleep(0.01)
        messageToSend = await ainput()
        await sio.emit('send_chat_room', {'message': messageToSend, 'name': clientName, 'room': roomName})

async def connectToServer():
    await sio.connect(FullIp)
    await sio.wait()

async def main():
    await asyncio.gather(
        connectToServer(),
        send_message()
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
async def send_message():
    while True:
        await asyncio.sleep(0.01)
        messageToSend = await ainput()
        await sio.emit('send_chat_room', {'message': messageToSend, 'name': clientName, 'room': roomName})

async def connectToServer():
    await sio.connect(FullIp)
    await sio.wait()

async def main(IpAddress):
    await asyncio.gather(
        connectToServer(),
        send_message()
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main(FullIp))