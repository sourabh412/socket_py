import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

server.bind(server_address)
server.listen(1)

print("Waiting for connection")

connection, client_addr = server.accept()

print(f"Connection extablished with {client_addr}")

data = connection.recv(1000)

print(f"Recieved : {data}")

connection.sendall(data)

connection.close()
server.close()