import socket


addr = ("127.0.0.1", 8888)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    msg = input("Enter the message to send:\n")
    client.sendto(msg.encode('utf-8'), addr)
    answer = client.recvfrom(1024)
    if answer:
        print(f"answer from server: {answer[0].decode('utf-8')}")
    else:
        print("no answer from server")
