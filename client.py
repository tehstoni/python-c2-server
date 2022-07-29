
import socket

ip_address = "127.0.0.1";
port_number = 666

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cs.connect((ip_address, port_number))

msg = input("Enter msg to send: ")

while msg!='quit':
    cs.send(msg.encode('utf-8'))
    #msg = cs.recv(1024).decode('utf-8')
    print(msg)
    msg = input("Enter msg to send: ")

cs.close()