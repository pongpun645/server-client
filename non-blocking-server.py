import socket

HOST = "127.0.0.1"
PORT = 5000

def recv_all(conn):
    data = b""

    while True:
        packet = conn.recv(1024)

        if not packet:
            break

        data += packet

    return data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server กำลังรอการเชื่อมต่อ...")

conn, addr = server.accept()
print("เชื่อมต่อจาก:", addr)

# รับข้อมูลทั้งหมด
data = recv_all(conn)

print("ข้อความที่ได้รับ:")
print(data.decode())

# ส่งข้อความตอบกลับ
conn.sendall(b"Server received all data")

conn.close()
server.close()