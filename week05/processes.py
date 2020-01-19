"""
Specifications of the process
. PID - process ID
. amount of RAM
. stack
. list of open file
. input/output

Console: top - shows list of working processes
ps aux | head -1; ps aux | grep {file_name.py}
strace -p {PID} for linux :(
lsof -p {PID} - list of open file

os.fork() - copy current process
"""
import time
import os


def main():
    # pid = os.getpid()
    # while True:
    #     print(pid, time.time())
    #     time.sleep(2)

    # pid = os.fork()
    # if pid == 0:
    #     while True:
    #         print('child: ', os.getpid())
    #         time.sleep(5)
    # else:
    #     print('parent: ', os.getpid())
    #     os.wait()

    # foo = 'bar'
    # if os.fork() == 0:
    #     # child process
    #     foo = 'bar'
    #     print('child:', foo)
    # else:
    #     # parent process
    #     print('parent:', foo)
    #     os.wait()

    # f = open('files/log.txt', 'r')
    # foo = f.readline()
    # if os.fork() == 0:
    #     # child
    #     foo = f.readline()
    #     print('child:', foo)
    # else:
    #     # parent
    #     foo = f.readline()
    #     print('parent:', foo)

    from multiprocessing import Process

    def f(name):
        print('hello', name)

    p = Process(target=f, args=('Bob',))
    p.start()  # create process
    p.join()  # p.wait()

    class PrintProcess(Process):

        def __init__(self, name):
            super().__init__()
            self.name = name

        def run(self):
            print('Hello', self.name)

    p = PrintProcess('Mike')
    p.start()
    p.join()


if __name__ == '__main__':
    main()
