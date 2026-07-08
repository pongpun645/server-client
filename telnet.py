import getpass
import telnetlib3

HOST = "172.16.161.136"
user =  input("Enter your remote account:  ")
password = getpass.getpass()

tn  = telnetlib3.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii')+ b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"ls\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
