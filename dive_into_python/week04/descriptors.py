import random


class Descriptor:

    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Class1:
    attr = Descriptor()


class Value:

    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)


class Class2:
    attr = Value()


class MyDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value
        with open('../files/log.txt', 'w') as file:
            file.write(str(value) + '\n')


class Account:  # example for my descriptor
    amount = MyDescriptor(100)


class Class3:

    def method(self):
        pass


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Property:

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        return self.getter(obj)


class WithMyProperty:

    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    custom_pure = Property(custom_pure)


class StaticMethod:

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func


class ClassMethod:

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        if obj_type is None:
            obj_type = type(obj)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func


class Class4:

    __slots__ = ['anakin'] # list of attributes

    def __init__(self):
        self.anakin = 'the chasen one'


def main():
    instance = Class1()
    instance.attr
    instance.attr = 1
    del instance.attr

    instance = Class2()
    instance.attr = 10
    print(instance.attr)

    bobs_account = Account()
    bobs_account.amount = 150

    obj = Class3()
    print(obj.method)
    print(Class3.method)

    amy = User('Amy', 'Jones')
    print(amy.full_name)
    print(User.full_name)

    obj = WithMyProperty()
    print(obj.original)
    print(obj.custom_sugar)
    print(obj.custom_pure)

    obj = Class4()
    obj.luke = 'the chose one'


if __name__ == '__main__':
    main()
