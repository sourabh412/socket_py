import socket
import sys

# socket creation
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("localhost", 10000)

# bind
server.bind(server_addr)

# listen
server.listen(1)
print("Waiting for connection")

# accept
conn, client_addr = server.accept()
print(f"Connection established with {client_addr}")

# recv
data = ""
print("\nRecieving\n")

while True:
    if data == "end":
        break
    data = conn.recv(1028).decode()
    print(data)

print("\nData recieved successfully")

# end
print("Closing connection")
conn.close()
server.close()