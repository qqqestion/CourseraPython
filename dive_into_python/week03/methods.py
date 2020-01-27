from datetime import date


class Human1:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f'Welcome to {self.name}, {human.name}!')
        self.population.append(human)


class Human2:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f'Hello, I am {self._name}')

    def say_how_old(self):
        self._say(f'I am {self._age} years old')


def extract_description(user_string):
    return 'opening of the football championship'


def extract_date(user_string):
    return date(2018, 6, 14)


class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f'Event "{self.description}" at {self.date}'

    # decorator that return new instance of cls
    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


class Human3:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


class Robot1:
    """Robot v.1 with power
    robot = Robot1(power=100)
    robot.power = 200
    robot.power
    >> 200
    robot.power = -20
    robot.power
    >> -20 # incorrect power can't be negative
    del robot.power
    >> # nothing prints
    """

    def __init__(self, power):
        # power can't be negative
        self.power = power


class Robot2:
    """Robot v.2 with setter, getter, and deleter for power
    robot = Robot2(power=100)
    robot.power = 200
    robot.power
    >> 200
    robot.power = -20
    robot.power
    >> 0
    del robot.power
    >> make robot useless"""

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('make robot useless')
        del self._power


class Robot3:
    """Robot v.3 with setter
    robot = Robot3(100)
    robot.power
    >> 100"""

    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        return self.power


def main():
    planet = Planet('Earth')
    planet.add_human(Human1('Bob'))

    bob = Human2('Bob', age=29)
    bob.say_name()
    bob.say_how_old()

    event_description = 'Tell about @classmethod'
    event_date = date.today()

    event = Event(event_description, event_date)
    print(event)

    event = Event.from_string('add to my calender opening of the football '
                              'championship at the 14th of June 2018')
    print(event)

    print(Human3.is_age_valid(35))
    human = Human3('Old Bobby')
    print(human.is_age_valid(235))

    robot = Robot1(100)
    robot.power = 200
    print('Robot power:', robot.power)
    robot.power = -20
    print('Robot power:', robot.power)

    new_robot = Robot2(100)
    new_robot.power = 200
    print('New robot power:', new_robot.power)
    new_robot.power = -20
    print('New robot power:', new_robot.power)


if __name__ == '__main__':
    main()
