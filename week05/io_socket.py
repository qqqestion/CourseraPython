"""
nonblocking input/output
linux = epoll
macOS = poll
"""

import socket
import select

sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

# как обработать запросы для conn1 и conn2
# одновременно без потоков?
conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)

my_poll = select.poll()
my_poll.register(conn1.fileno(), select.POLLIN | select.POLLOUT)
my_poll.register(conn2.fileno(), select.POLLIN | select.POLLOUT)
# my_epoll = select.epoll()
# my_epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
# my_epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}

# Неблокирующий ввод/вывод, обучающий пример
# Цикл обработки событий в epoll

while True:
    events = my_poll.poll(1)
    # events = my_epoll.poll(1)

    for fileno, event in events:
        if event & select.POLLIN:  # EPOLLIN
            # обработка чтения из сокета
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.POLLOUT:  # EPOLLOUT
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))
