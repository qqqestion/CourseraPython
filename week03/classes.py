class Robot:
    """It's doc string of Robot class Hi there """
    pass


class Planet1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Planet {self.name}'


class Planet2:
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet2.count += 1


class Human:

    def __del__(self):
        print('Goodbye!')


class Planet3:

    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print('__init__ called')
        self.name = name


if __name__ == '__main__':
    print(Robot.__doc__)

    solar_system = []
    planets_name = [
        'Mercury', 'Venus', 'Earth', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune'
    ]
    for name in planets_name:
        planet = Planet1(name)
        solar_system.append(planet)
    print(*solar_system, sep=', ')

    earth = Planet2('Earth')
    mars = Planet2('Mars')
    print(Planet2.count)

    human = Human()
    del human

    earth = Planet3('Earth')
