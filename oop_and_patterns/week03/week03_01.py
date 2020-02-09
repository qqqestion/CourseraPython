from abc import ABC, abstractclassmethod
from oop_and_patterns.week03.test_decorator import Hero


class AbstractEffect(ABC, Hero):
    basic_characteristics = ['Strength', 'Perception', 'Endurance', 'Charisma',
                             'Intelligence', 'Agility', 'Luck']

    def __init__(self, base):
        self.base = base

    @abstractclassmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractclassmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractclassmethod
    def get_stats(self):
        return self.base.get_stats()


class AbstractPositive(AbstractEffect):

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    """
    . increase strength, endurance, agility, luck by 7
    . decrease perception, charisma, intelligence by 3
    . increase hp by 50
    """

    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Berserk')
        return effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        for increased_stat in ['Strength', 'Endurance', 'Agility', 'Luck']:
            stats[increased_stat] += 7
        for decreased_stat in ['Perception', 'Charisma', 'Intelligence']:
            stats[decreased_stat] -= 3
        return stats


class Blessing(AbstractPositive):

    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Blessing')
        return effects

    def get_stats(self):
        stats = self.base.get_stats()
        for increased_stat in self.basic_characteristics:
            stats[increased_stat] += 2
        return stats


class AbstractNegative(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Weakness(AbstractNegative):

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Weakness')
        return effects

    def get_stats(self):
        stats = self.base.get_stats()
        for decreased_stat in ['Strength', 'Endurance', 'Agility']:
            stats[decreased_stat] -= 4
        return stats


class EvilEye(AbstractNegative):

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('EvilEye')
        return effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats


class Curse(AbstractNegative):

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Curse')
        return effects

    def get_stats(self):
        stats = self.base.get_stats()
        for decreased_stat in self.basic_characteristics:
            stats[decreased_stat] -= 2
        return stats
