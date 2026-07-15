import paramiko

hostname = "192.168.1.124"
username = "pongpun"
passwd = "123456789"
port = 22

try:
    p = paramiko.Transport((hostname, port))
    p.connect(username=username, password=passwd)
    print("[*] Connected to " + hostname + "via SSH")
    
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Starting file download")
    sftp.get("/home/6806022510645/test.txt", "/Users/watcharachai/Downloads/d.txt")
    print("[*] File download complete")
    
    print("[*] Starting file upload")
    sftp.put("/Users/6806022510645/Downloads/d.txt", "/home/watcharachai/u.txt")
    print("[*] File upload complete")
    
    p.close()
    print("[*] Disconnected from server")

except Exception as err:
    print("[!] " + str(err))