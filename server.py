
import socket

print("initializing socket connection")

ip_address = "127.0.0.1"
port_number = 666

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port_number))

print("socket initialized")

server_socket.listen(1)
server_socket.accept()

cs,address = server_socket.accept()

print("Got connection from client {}".format(address)) 
msg = cs.recv(1024).decode('utf-8')

while msg!='quit':
    msg = cs.recv(1024).decode('utf-8')
    print(msg)
    cs.send(msg.encode('utf-8'))

cs.close()
server_socket.close()
