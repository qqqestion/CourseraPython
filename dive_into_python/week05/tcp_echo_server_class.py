import asyncio
import logging
import concurrent.futures


class EchoServer:
    """Echo server class"""

    def __init__(self, host, port, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self._server = asyncio.start_server(
            self.handle_connection, host=host, port=port
        )

    def start(self, and_loop=True):
        self._server = self._loop.run_until_complete(self._server)
        logging.info('Listening establish on {}'.format(
            self._server.sockets[0].getsockname()
        ))
        if and_loop:
            self._loop.run_forever()

    def stop(self, and_loop=True):
        self._server.close()
        if and_loop:
            self._loop.close()

    @asyncio.coroutine
    def handle_connection(self, reader, writer):
        peername = writer.get_extra_info('peername')
        logging.info(f'Accepted connection from {peername}')
        while not reader.at_eof():
            try:
                data = yield from asyncio.wait_for(
                    reader.read(1024), timeout=5
                )
                logging.info(f"data is written: {data.decode()}")
                writer.write(data)
            except concurrent.futures.TimeoutError:
                logging.info(f'Connection from {peername} closed by concurrent.futures.TimeoutError')
                break
            except asyncio.exceptions.TimeoutError:
                logging.info(f'Connection from {peername} closed by asyncio.exceptions.TimeoutError')
                break
        writer.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    server = EchoServer('127.0.0.1', 2007)
    try:
        server.start()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
