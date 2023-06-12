import socket
import threading

server_addr = ('localhost', 10002)

def server_thread(client_conn, client_addr):
    print(f"Connection established with {client_addr}")
    print("Waiting for data transfer...\n")
    data = ""
    while True:
        if data == "end":
            break
        data = client_conn.recv(1028).decode()
        print(data)
    print("\nData transfer complete...")
    print(f"Closing connection with {client_addr}")
    client_conn.close()

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen(1)
    print("Waiting for connection...")

    while True:
        client_conn, client_addr = server.accept()
        t = threading.Thread(target=server_thread, args=(client_conn, client_addr,))
        t.start()
