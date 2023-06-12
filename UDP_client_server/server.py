import socket

# creating connection
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind
server_addr = ('localhost', 10000)
server.bind(server_addr)

# listen
# server.listen(1)
print("Waiting for connection")

# accept
# conn, client_addr = server.accept()
# print("Connection established\n")

# recv
data = ""

while True:
    data, client_addr = server.recvfrom(1028)
    if data == b'end':
        break
    print(f"msg from {client_addr}\n{data.decode()}\n")

print("\nData recieved successfully")

# end
print("Closing connection")
# conn.close()
server.close()