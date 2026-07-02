import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = """
สวัสดี Server
นี่คือข้อความหลายบรรทัด
ทดสอบการส่งข้อมูลทั้งหมดด้วย recv_all()
"""

client.sendall(message.encode())

# แจ้งว่าไม่มีข้อมูลส่งแล้ว
client.shutdown(socket.SHUT_WR)

# รับข้อความตอบกลับ
reply = client.recv(1024)

print(reply.decode())

client.close()