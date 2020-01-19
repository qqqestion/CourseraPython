# create socket, server
import socket

# https://docs.python.org/3/library/socket.html
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 127.0.0.1 local host
sock.bind(('127.0.0.1', 10001))  # max port 65535
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    # process data
    print(data.decode('utf-8'))

conn.close()
sock.close()
