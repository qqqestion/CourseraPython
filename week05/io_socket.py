"""
nonblocking input/output
linux = epoll
macOS = kqueue
"""
import select
import socket


sock = socket.socket()
sock.bind(('', 10001))
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)

poll = select.poll()
poll.register(conn1.fileno(), select.POLLIN | select.POLLOUT)
poll.register(conn2.fileno(), select.POLLIN | select.POLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}

# event handling loop
while True:
    events = poll.poll(1)
    for fileno, event in events:
        if event & select.POLLIN:
            data = conn_map[fileno].recv(1024)
            print(data.decode('utf8'))
        elif event & select.POLLOUT:
            conn_map[fileno].send('ping'.encode('utf8'))


