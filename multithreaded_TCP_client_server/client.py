import socket

server_addr = ('localhost', 10002)

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client:
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