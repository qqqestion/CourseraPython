import asyncio


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(MetricsServer, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ServerError(Exception):
    """Just to raise my exception"""
    pass


class MetricsServer(asyncio.Protocol):
    """
    metric_data - all metrics, for the whole server
    connection_count - obviously, but don't really know if it's right
    """
    metric_data = dict()
    connection_count = 0

    def connection_made(self, transport):
        """
        connection count += 1
        :param transport:
        :return:
        """
        self.transport = transport
        MetricsServer.connection_count += 1

    def connection_lost(self, *args, **kwargs):
        """
        if there is no connections raise KeyboardInterrupt to close server
        :param args:
        :param kwargs:
        :return:
        """
        MetricsServer.connection_count -= 1
        if MetricsServer.connection_count == 0:
            raise KeyboardInterrupt

    def _parse_request(self, request):
        """
        checks form of requests, if everything is OK, return parsed request
        :param request:
        :return:
        """
        if request[-1] != '\n':
            raise ServerError('request doesn\'t have end of line symbol')

        command, payload = request.split(maxsplit=1)
        payload = payload.strip()

        if command == 'put':
            key, timestamp, value = payload.split()
            return command, (key, timestamp, value)
        elif command == 'get':
            return command, (payload,)
        else:
            raise ServerError('unknown command')

    def _get(self, key):
        """
        response - ENCODED answer on the requested key
        :param key:
        :return:
        """
        response = b'ok\n'
        if key == '*':
            for metric, recording_list in MetricsServer.metric_data.items():
                for value, timestamp in recording_list:
                    response += f'{metric} {value} {timestamp}\n'.encode('utf8')
        else:
            for value, timestamp in MetricsServer.metric_data.get(key, []):
                response += f'{key} {value} {timestamp}\n'.encode('utf8')
        response += b'\n'
        return response

    def _add_data(self, key, value, timestamp):
        """
        check types of value, timestamp. don't know if it's needed
        if last input in metric_data[key] was timestamp we pop
        tuple(old_value, timestamp); if there is no key in metric_data we
        add empty list; in the end we append tuple(new_value, timestamp)
        :param key:
        :param value:
        :param timestamp:
        :return:
        """
        if not isinstance(value, float) or not isinstance(timestamp, int):
            raise ServerError('invalid type')
        last_time = MetricsServer.metric_data.get(
            key, [(None, None)]
        )[-1][1]
        if last_time == timestamp:
            MetricsServer.metric_data[key].pop()
        elif last_time is None:
            MetricsServer.metric_data[key] = []
        MetricsServer.metric_data[key].append((value, timestamp))

    def data_received(self, data):
        """
        calls when data received
        handling any exceptions so that we can respond about error (maybe
        wrong idea)
        :param data:
        :return:
        """
        try:
            command, args = self._parse_request(data.decode('utf8'))
            if command == 'put':
                key, value, timestamp = args
                self._add_data(key, float(value), int(timestamp))
                self.transport.write(b'ok\n\n')
            elif command == 'get':
                key = args[0]
                response = self._get(key)
                self.transport.write(response)
        except Exception as err:
            self.transport.write('error\nwrong command\n'.encode('utf8'))

# run_server('127.0.0.1', 8888)
