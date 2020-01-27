# handling some connections at once
# server
import socket

with socket.socket() as sock:
    sock.bind(('', 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        print('connected client:', addr)
        # process or thread for connection's handling
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf8'))
