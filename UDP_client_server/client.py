import socket

# socket creation
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connection
server_addr = ('localhost', 10000)
client.connect(server_addr)
print("Connection estabished\n")

# send
msg = ""
while msg != "end":
    msg = input()
    client.send(msg.encode())

print("\nData sent successfully")

# end
print("Closing connection")
client.close()