import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('localhost',10000)

client.connect(server_addr)

message = input()

print(f"Sending : {message}")
client.sendall(message.encode())

print(f"Original : {message}")

data = client.recv(1000).decode()
print(f"Echo : {data}")

client.close()