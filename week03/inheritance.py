import json


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None, age=0):
        super().__init__(name)
        self.breed = breed
        # private field
        self.__age = age

    def say(self):
        return f'{self.name} says waw'


class ExportJSON:
    def to_json(self):
        return json.dumps({
            'name': self.name,
            'breed': self.breed
        })


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # call method in MRO
        super().__init__(name, breed)
        # super(ExDog, self).__init(name)

    def get_breed(self):
        return f'breed: {self.name} - {self.breed} with age {self.__age}'

    # we really really want to get self.age
    def get_breed2(self):
        return f'breed: {self.name} - {self.breed} with age {self._Dog__age}'


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # explicitly call method of specific class
        super(Dog, self).__init__(name)
        self.breed = f'Woolen dog breed {breed}'


def main():
    dog = Dog('Sharik', 'Akita')
    print(dog.name)
    print(dog.say())

    jdog = ExDog('JSharik', 'Bulldog')
    print(jdog.to_json())

    print(issubclass(ExDog, Pet))

    print(ExDog.__mro__)

    dog = WoolenDog('Rax', breed='Dachshund')
    print(dog.breed)

    # example of private fields
    try:
        print(jdog.get_breed())
    except AttributeError:
        print('No such attribute')
    print(jdog.__dict__)
    print(jdog.get_breed2())


if __name__ == '__main__':
    main()
