class Class:
    pass


def dummy_factory():
    class ClassInternal:
        pass

    return ClassInternal


class Meta1(type):

    def __new__(cls, name, parents, attrs):
        print(f'Look at this, DUDE: Creating {name}')

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class A1(metaclass=Meta1):
    pass


class Meta2(type):

    def __init__(cls, name, bases, attrs):
        print(f'Look at this, DUDE: Initializing - {name}')

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta2): pass


class A2(Base): pass


class B2(Base): pass


from abc import ABCMeta, abstractclassmethod  # abstracts metheds


class Sender(metaclass=ABCMeta):

    @abstractclassmethod
    def send(self):
        """Do something"""


class Child1(Sender):
    pass


class Child2(Sender):

    def send(self):
        print('Sending')


# hot to create abstract method python
class PythonWay:

    def send(self):
        raise NotImplementedError


def main():
    obj = Class()
    print(type(obj))
    print(type(Class))

    Dummy = dummy_factory()
    print(Dummy() is Dummy())

    NewClass = type('NewClass', (), {})  # we create new class!
    print(NewClass)
    print(NewClass())

    print(f'A.class_id: "{A1.class_id}"')

    print(Base.registry)
    print(Base.__subclasses__())

    try:
        Child1()
    except TypeError as err:
        print('Child raise error: ', err)
    Child2()


if __name__ == '__main__':
    main()
