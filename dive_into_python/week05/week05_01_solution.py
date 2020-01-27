import socket
import time


class ClientError(Exception):
    """Client error"""
    pass


class Client:
    """Client class"""

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error:
            raise ClientError('Connection cannot be created')

    def _read(self):
        data = b''

        while not data.endswith('\n\n'):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ClientError('Error reading data from server', err)

        return data

    def _send(self, data):
        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise ClientError('Error sending data to server', err)

    def put(self, metric, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        self._send(f'put {metric} {value} {timestamp}\n'.encode())
        raw_data = self._read()

        if raw_data == 'ok\n\n':
            return
        raise ClientError('Server return error')

    def get(self, metric):
        self._send(f'get {metric}\n'.encode())
        raw_data = self._read()
        data = dict()
        status, payload = raw_data.split('\n', maxsplit=1)
        payload = payload.strip()

        if status != 'ok':
            raise ClientError('Server returns an error')
        elif payload == '':
            return data

        try:
            for row in payload.splitlines():
                key, value, timestamp = row.split()
                if not key in data:
                    data[key] = []
                data[key].append((int(timestamp), float(value)))
        except Exception as err:
            raise ClientError('Server returns invalid data', err)

        return data

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError('Error cloning connection', err)
