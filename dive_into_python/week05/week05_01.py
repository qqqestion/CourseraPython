import socket
import time
import json


class ClientError(IOError):
    """ClientError class for Client class for tcp server.
    Week 5. Coursera Python"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class Client:
    """Client class for tcp server.
    Week 5. Coursera Python"""

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout or socket.getdefaulttimeout()

    def put(self, metric, value, timestamp=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.settimeout(self.timeout)
        timestamp = timestamp or int(time.time())
        sock.sendall(f'put {metric} {value} {timestamp}\n'.encode('utf8'))
        response = sock.recv(1024).decode('utf8').split('\n')
        if response[0] != 'ok':
            raise ClientError
        sock.close()

    def get(self, metric):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.settimeout(self.timeout)
        sock.sendall(f'get {metric}\n'.encode('utf8'))
        try:
            response = sock.recv(1024).decode('utf8').strip().split('\n')
            result = dict()
            if len(response) == 1 and response[0] == 'ok':
                return result
            elif response[0] == 'error':
                raise ClientError
            data_response = response[1:]
            for line in data_response:
                key, val, time = line.split()
                if key not in result:
                    result[key] = []
                result[key].append((int(time), float(val)))
        except Exception:
            raise ClientError
        finally:
            sock.close()

        return result
