import asyncio
import logging
import concurrent.futures


@asyncio.coroutine
def handle_connection(reader, writer):
    peername = writer.get_extra_info('peername')
    logging.info(f'Accepted connection from {peername}')
    while True:
        try:
            data = yield from asyncio.wait_for(reader.readline(), timeout=10.0)
            if data:
                writer.write(data)
            else:
                logging.info(f'Connection from {peername} closed by peer')
                break
        except concurrent.futures.TimeoutError:
            logging.info(f'Connection from {peername} closed by timeout')
            break
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    logging.basicConfig(level=logging.INFO)
    server_gen = asyncio.start_server(handle_connection, port=2007)
    server = loop.run_until_complete(server_gen)
    logging.info('Listening established on {}'.format(
        server.sockets[0].getsockname()
    ))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
