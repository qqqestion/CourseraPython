from abc import ABC, abstractclassmethod


class A:
    @abstractclassmethod
    def do_something(self):
        print('Hi!')


a = A()
a.do_something()


class AABC(ABC):
    @abstractclassmethod
    def do_something(self):
        print('Hi!')


# a = AABC()
a.do_something()


class B(AABC):
    def do_something(self):
        print('Hi2')

    def do_something_else(self):
        print('Hello')


b = B()
