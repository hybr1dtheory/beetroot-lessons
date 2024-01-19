from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def handle_client(sckt: socket):
    while True:
        data = sckt.recv(1024)
        if not data:
            break
        sckt.send(data)
    sckt.close()


def echo_server():
    server = socket(AF_INET, SOCK_STREAM)
    serv_addr = ("127.0.0.1", 7777)
    server.bind(serv_addr)
    server.listen(5)  # max 5 connections
    print(f"Server listening on {serv_addr[0]}:{serv_addr[1]}")
    while True:
        client, addr = server.accept()
        print(f"Accept connection with {addr}")
        handler = Thread(target=handle_client, args=(client,))
        handler.start()


if __name__ == "__main__":
    echo_server()
