from abc import ABC, abstractmethod
import pygame
import random


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class AbstractObject(ABC):

    def __init__(self, sprite, position):
        self.sprite = sprite
        self.position = position

    def draw(self, display):
        """
        :rtype display: ScreenEngine.GameSurface
        """
        display.draw_object(self.sprite, self.position)


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        super().__init__(icon, position)
        self.action = action

    def interact(self, engine, hero):
        engine.delete_object(self)
        self.action(engine, hero)


class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        super().__init__(icon, position)
        self.stats = stats
        self.max_hp = 1
        self.calc_max_hp()
        self.hp = self.max_hp

    def calc_max_hp(self):
        self.max_hp = 5 + self.stats["endurance"] * 2


class Hero(Creature):

    def __init__(self, stats: dict, icon: pygame.Surface):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):
        while self.exp >= 100 * (2 ** (self.level - 1)):
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_hp()
            self.hp = self.max_hp


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    def level_up(self):
        self.base.level_up()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    @abstractmethod
    def apply_effect(self):
        pass


class Berserk(Effect):
    """
    . increases hp by 20
    . increases strength by 5
    """

    def apply_effect(self):
        self.base.hp += min(self.base.max_hp, self.base.hp + 20)
        self.stats['strength'] += 5


class Blessing(Effect):
    """
    . increases basic characteristics by 2
    """

    def apply_effect(self):
        for stat in self.stats.keys():
            self.stats[stat] += 2


class Weakness(Effect):
    """
    . reduces strength, and endurance by 2
    """

    def apply_effect(self):
        self.stats['strength'] = max(self.stats['strength'] - 2, 1)
        self.stats['endurance'] = max(self.stats['endurance'] - 2, 1)


class Enemy(Creature, Interactive):

    def __init__(self, icon, stats, xp, position):
        super().__init__(icon, stats, position)
        self.xp = xp

    def interact(self, engine, hero):
        self.hp -= hero.stats['strength']
        if self.hp > 0:
            engine.hero = Weakness(hero)
            hero.hp -= self.stats['strength']
            if engine.hero.hp <= 0:
                engine.kill_hero()
        else:
            hero.exp += self.xp
            engine.hero.level_up()
            engine.delete_object(self)
