import socket 

Host = '127.0.0.1'
Port = 1000

client = socket .socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host,Port))

while True :
    msg = input("hello world:")
    
    if msg.lower()== "exit":
        break
    client.send(msg.encode())

    data = client.recv(1024)
    print(data.decode())

client.close()