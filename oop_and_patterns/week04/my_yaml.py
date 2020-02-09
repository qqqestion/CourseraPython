from abc import ABC, abstractmethod
import yaml

hero_yaml = '''
--- !Character
factory:
  !factory assassin
name:
  7NaGiBaTo
'''


class HeroFactory(ABC):
    @abstractmethod
    def create_hero(self, name):
        pass

    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_spell(self):
        pass


class WarriorFactory(HeroFactory):
    def create_hero(self, name):
        return Warrior(name)

    def create_weapon(self):
        return Claymore()

    def create_spell(self):
        return Power()


class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Warrior {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Warrior {self.name} casts {self.spell.cast()}")
        self.spell.cast()


class Claymore:
    def hit(self):
        return "Claymore"


class Power:
    def cast(self):
        return "Power"


class MageFactory(HeroFactory):
    def create_hero(self, name):
        return Mage(name)

    def create_weapon(self):
        return Staff()

    def create_spell(self):
        return Fireball()


class Mage:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Mage {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Mage {self.name} casts {self.spell.cast()}")
        self.spell.cast()


class Staff:
    def hit(self):
        return "Staff"


class Fireball:
    def cast(self):
        return "Fireball"


class AssassinFactory(HeroFactory):
    def create_hero(self, name):
        return Assassin(name)

    def create_weapon(self):
        return Dagger()

    def create_spell(self):
        return Invisibility()


class Assassin:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Assassin {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Assassin {self.name} casts {self.spell.cast()}")


class Dagger:
    def hit(self):
        return "Dagger"


class Invisibility:
    def cast(self):
        return "Invisibility"


def factory_constructor(loader, node):
    data = loader.construct_scalar(node)
    if data == 'assassin':
        return AssassinFactory
    elif data == 'mage':
        return MageFactory
    elif data == 'warrior':
        return WarriorFactory
    else:
        raise ValueError('Unknown token')


class Character(yaml.YAMLObject):
    yaml_tag = '!Character'

    def create_hero(self):
        hero = self.factory.create_hero(self.factory, self.name)

        weapon = self.factory.create_weapon(self.factory)
        ability = self.factory.create_spell(self.factory)

        hero.add_weapon(weapon)
        hero.add_spell(ability)

        return hero


if __name__ == '__main__':
    loader = yaml.Loader
    loader.add_constructor('!factory', factory_constructor)
    hero = yaml.load(hero_yaml).create_hero()
    hero.hit()
    hero.cast()



