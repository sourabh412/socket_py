import socket
import os

# main server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost', 10000)
print("socket created")

server.bind(server_addr)
print("socket binded")

server.listen(1)
print("socket listening")

while(True):
    conn, client_addr = server.accept()
    print(f"Connection established with {client_addr}")
    new_pid = os.fork()

    if new_pid == 0:
        data = ""
        print("\nRecieving\n")

        while True:
            if data == "end":
                break
            data = conn.recv(1028).decode()
            print(data)
        
        print("\nData recieved successfully")

        print("Closing connection")
        conn.close()
    
    else:
        conn.close()
