# asyncio, hello world

import asyncio

# example 1
@asyncio.coroutine
def hello_world():
    while True:
        print('hello world')
        yield from asyncio.sleep(1.0)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())
# loop.close()


# example 2
# asyncio, async def / await; PEP 492 Python3.5
async def hello_world_as():
    while True:
        print('hello world')
        await asyncio.sleep(1.0)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world_as())
# loop.close()

