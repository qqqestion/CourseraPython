import random


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }

    def __str__(self):
        return f'{self.name} <{self.email}>'

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email


class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class Researcher:

    # if attribute not found
    def __getattr__(self, item):
        return 'Nothing found :('

    # calls always when we call any attribute
    def __getattribute__(self, item):
        print(f'Looking for {item}')
        return object.__getattribute__(self, item)


class Ignorant:

    # calls when we are trying to set value to any attribute
    def __setattr__(self, key, value):
        print(f'Not gonna set {key}!')


class Polite:

    # calls when we want to del our attribute
    def __delattr__(self, item):
        value = getattr(self, item)
        print(f'Goodbye {item}, you were {value}')
        object.__delattr__(self, item)


class Logger:

    def __init__(self, filename):
        self.filename = filename

    # every time we our function with logger as decorator is called
    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with open(self.filename, 'w') as f:
                f.write('Oh Danny boy...\n')
            return func(*args, **kwargs)

        return wrapped


class NoisyInt:

    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        noise = random.uniform(-1, 1)
        return self.value + obj.value + noise


class MyContainer:

    def __init__(self, iterable=None):
        iterable = list(iterable)
        self._data = iterable

    def __getitem__(self, key):
        if 0 <= key < len(self._data):
            return self._data[key]
        raise ValueError

    def __setitem__(self, key, value):
        if 0 <= key < len(self._data):
            self._data[key] = value
        else:
            raise ValueError

    def __str__(self):
        return str(self._data)


""" ITERATORS """


class SquareIterator:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


class IndexIterable:

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, index):
        return self.obj[index]


""" CONTEXT MANAGER """


class open_file:

    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


class suppress_exception:

    def __init__(self, ext_type):
        self.exc_type = ext_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type == self.exc_type:
            print('Nothing happend')
            return True


import time


class timer:

    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(f'Elapsed: {self.current_time()}')


def main():
    jane = User('Jane Doe', 'example@mail.com')
    print(jane.get_email_data())

    a = Singleton()
    b = Singleton()
    print(a is b)

    print(jane)

    joe = User('Joe Doe', 'example@mail.com')
    print(jane == joe)

    obj = Researcher()
    print(obj.attr)
    print(obj.method)
    print(obj.DFG2H3J00KLL)

    obj = Ignorant()
    obj.math = True

    obj = Polite()
    obj.attr = 0
    del obj.attr

    logger = Logger('../files/log.txt')

    @logger
    def completely_useless_function():
        pass

    completely_useless_function()

    a = NoisyInt(10)
    b = NoisyInt(20)
    for _ in range(3):
        print(a + b)

    container = MyContainer((1, 2, 3, 4))
    print(container)
    container[0] = 10
    print(container)
    print(container[3])

    """ ITERATOR """

    for num in SquareIterator(1, 4):
        print(num, end=' ')
    print()

    for letter in IndexIterable('str'):
        print(letter, end=' ')
    print()

    """ CONTEXT MANAGER """

    with open_file('../files/log.txt', 'r') as f:
        print(f.read())

    with suppress_exception(ZeroDivisionError):
        really_big_number = 1 / 0

    import contextlib

    with contextlib.suppress(ValueError):
        raise ValueError

    with timer() as t:
        time.sleep(1)
        print(f'Current: {t.current_time()}')
        time.sleep(1)


if __name__ == '__main__':
    main()
