import socket


addr = ("127.0.0.1", 8888)
timeout = 60
answer = "Your message was successfully received"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind(addr)
    while True:
        server.settimeout(timeout)
        print(f"waiting for data {timeout} seconds")
        try:
            data = server.recvfrom(1024)
            msg = data[0]
            client_addr = data[1]
        except socket.timeout:
            print(f"Time is out. {timeout} sec have passed.")
            break
        print(f"Message {msg.decode('utf-8')} was received from {client_addr[0]}:{client_addr[1]}")
        server.sendto(answer.encode('utf-8'), client_addr)
