from abc import ABC, abstractclassmethod


class Creature(ABC):

    @abstractclassmethod
    def feed(self):
        pass

    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print('I eat grass')

    def move(self):
        print('I walk forward')

    def make_noise(self):
        print('WOOO!')


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def feed(self):
        self.base.feed()

    def move(self):
        self.base.move()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):

    def move(self):
        print('I swim forward')

    def make_noise(self):
        print('...')


class Predator(AbstractDecorator):

    def feed(self):
        print('I eat other animals')


class Fast(AbstractDecorator):

    def move(self):
        self.base.move()
        print('Fast!')


if __name__ == '__main__':
    animal = Animal()
    print('Example 1')
    animal.move()
    animal.feed()
    animal.make_noise()
    print()

    print('Example 2')
    swimming = Swimming(animal)
    swimming.move()
    swimming.feed()
    swimming.make_noise()
    print()

    print('Example 3')
    predator = Predator(swimming)
    predator.move()
    predator.feed()
    predator.make_noise()
    print()

    print('Example 4')
    fast = Fast(predator)
    fast.move()
    fast.feed()
    fast.make_noise()
    print()

    print('Example 5')
    faster = Fast(fast)
    faster.move()
    faster.feed()
    faster.make_noise()
    print()
