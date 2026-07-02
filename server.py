import socket

HOST = '127.0.0.1'
PORT = 1000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server กำลังรอการเชื่อมต่อ...")

conn, addr = server.accept()
print("เชื่อมต่อจาก:", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    message = data.decode()
    print("Client:", message)

    reply = "Server ได้รับข้อความ: " + message
    conn.send(reply.encode())

conn.close()
server.close()