"""
Threads:
. looks like process
. thread has his own list of instructions
. each thread has stack
. thread spare memory and resources of process
. threads in Python has limits
"""
from threading import Thread


def main():
    """
    def f1(name):
        print('hello', name)

    th = Thread(target=f1, args=('Bob',))
    th.start()
    th.join()

    class PrintThread(Thread):

        def __init__(self, name):
            super().__init__()
            self.name = name

        def run(self):
            print('hello', self.name)

    th = PrintThread('Mike')
    th.start()
    th.join()

    from concurrent.futures import ThreadPoolExecutor, as_completed

    def f2(a):
        return a * a

    # .shutdown() in exit
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = [pool.submit(f2, i) for i in range(10)]

        for future in as_completed(results):
            print(future.result(), end=' ')
    """

    """
    Threads synchronization 
    """

    """
    from queue import Queue

    def worker(q, n):
        while True:
            item = q.get()
            if item is None:
                break
            print('process data', n, item)

    q = Queue(5)
    th1 = Thread(target=worker, args=(q, 1))
    th2 = Thread(target=worker, args=(q, 2))
    th1.start()
    th2.start()
    for i in range(50):
        q.put(i)
    # stops threads
    q.put(None)
    q.put(None)
    th1.join()
    th2.join()


    import threading

    class Point(object):

        def __init__(self):
            self._mutex = threading.RLock()
            self._x = 0
            self._y = 0

        def get(self):
            with self._mutex:
                return (self._x, self._y)

        def set(self, x, y):
            with self._mutex:
                self._x = x
                self._y = y

    a = threading.RLock()
    b = threading.RLock()

    def foo():
        try:
            a.acquire() # get lock
            b.acquire()
        finally:
            a.release()
            b.release()

    class Queue:

        def __init(self, size=5):
            self._size = size
            self._queue = []
            self._mutex = threading.RLock()
            self._empty = threading.Condition(self._mutex)
            self._full = threading.Condition(self._mutex)

        def put(self, val):
            with self._full:
                while len(self._queue) >= self._size:
                    self._full.wait()
                self._queue.append(val)
                self._empty.notify()

        def get(self):
            with self._empty:
                while len(self._queue) == 0:
                    self._empty.wait()
                ret = self._queue.pop(0)
                self._full.notify()
                return ret
    """

    """
    Global Interpreter Lock
    GIL
    for memory guarding 
    """

    from threading import Thread
    import time

    def count(n):
        while n > 0:
            n -= 1

    # series run
    t0 = time.time()
    count(100_000_00)
    count(100_000_00)
    print('Series run: ', time.time() - t0)

    # parallel run
    t0 = time.time()
    th1 = Thread(target=count, args=(100_000_000,))
    th2 = Thread(target=count, args=(100_000_000,))

    th1.start();
    th2.start()
    th1.join();
    th2.join()
    print('Parallel run: ', time.time() - t0)
    # if program needs only cpu resources, it will work more slowly with
    # multi-threads than with one thread (linear implementation)
    """
    a      r      a             r          a
      run  |------|     run     |----------| run
    ------>|  IO  |------------>|    IO    |----->
           |------|             |----------|
    a      r      a             r          a

    a - acquire GIL (get)
    r - release GIL 
    """


if __name__ == '__main__':
    main()
