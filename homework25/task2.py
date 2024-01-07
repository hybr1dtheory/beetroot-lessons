import socket
from string import ascii_uppercase, ascii_lowercase
from re import fullmatch, DOTALL


def encode_caesar(msg: str, key: int) -> str:
    """Encode a string (msg) with caesar`s cipher with a shift (key).
    Only english letters will be encoded, other symbols will remain as they are"""
    low_alpha = ' ' + ascii_lowercase
    up_alpha = ' ' + ascii_uppercase
    l = len(low_alpha)
    res = ''
    for c in msg:
        if c.isalpha():
            if c.islower():
                res += low_alpha[(low_alpha.index(c) + key) % l]
            else:
                res += up_alpha[(up_alpha.index(c) + key) % l]
        else:
            res += c
    return res


def check_msg(msg: str) -> bool:
    """Check message format (must be <some text> --<key>)"""
    m = fullmatch(r'.+ --\d+', msg, flags=DOTALL)
    return bool(m)


addr = ("127.0.0.1", 12345)
l_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
l_sock.bind(addr)
l_sock.listen(1)
print(f'Serving HTTP on port {addr[1]} ...')
while True:
    client_conn, client_addr = l_sock.accept()
    msg = client_conn.recv(2048)
    if check_msg(msg.decode('utf-8').strip()):
        args = msg.decode('utf-8').strip().split(' --')
        msg, key = args[0], int(args[1])
        result = encode_caesar(msg, key)
        client_conn.sendall(result.encode('utf-8'))
    else:
        client_conn.sendall("Wrong message format (must be <some text> --<key>)".encode('utf-8'))
    client_conn.close()
