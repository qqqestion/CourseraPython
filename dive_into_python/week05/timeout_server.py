# create socket with timeout and handling exceptions
# server

import socket

with socket.socket() as sock:
    sock.bind(('', 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        # if we don't connect to the server in 5 sec, we get exception
        # socket.timeout
        # handling this exception we can as we want
        conn.settimeout(5)  # timeout := None/0/gt 0
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print('close connection by timeout')
                    break
                if not data:
                    break
                print(data.decode('utf8'))
