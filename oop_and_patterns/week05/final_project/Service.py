import pygame
import random
import yaml
import os
import Objects as Objects

OBJECT_TEXTURE = os.path.join("texture", "objects")
ENEMY_TEXTURE = os.path.join("texture", "enemies")
ALLY_TEXTURE = os.path.join("texture", "ally")


def reload_game(engine, hero):
    global level_list
    level_list_max = len(level_list) - 1
    engine.level += 1
    hero.position = [1, 1]
    engine.objects = []
    generator = level_list[min(engine.level, level_list_max)]
    _map = generator['map'].get_map()
    engine.load_map(_map)
    engine.add_objects(generator['obj'].get_objects(_map))
    engine.add_hero(hero)


def restore_hp(engine, hero):
    engine.score += 0.1
    hero.hp = hero.max_hp
    engine.notify("HP restored")


def apply_blessing(engine, hero):
    if hero.gold >= (int(20 * 1.5 ** engine.level) -
                     2 * hero.stats["intelligence"]):
        engine.score += 0.2
        hero.gold -= (int(20 * 1.5 ** engine.level) -
                      2 * hero.stats["intelligence"])
        if random.randint(0, 1) == 0:
            engine.hero = Objects.Blessing(hero)
            engine.notify("Blessing applied")
        else:
            engine.hero = Objects.Berserk(hero)
            engine.notify("Berserk applied")
    else:
        engine.score -= 0.1


def remove_effect(engine, hero):
    if hero.gold >= (int(10 * 1.5 ** engine.level) -
                     2 * hero.stats["intelligence"] and "base" in dir(hero)):
        hero.gold -= int(10 * 1.5 ** engine.level) - \
                     2 * hero.stats["intelligence"]
        engine.hero = hero.base
        engine.hero.calc_max_hp()
        engine.notify("Effect removed")


def add_gold(engine, hero):
    if random.randint(1, 10) == 1:
        engine.score -= 0.05
        engine.hero = Objects.Weakness(hero)
        engine.notify("You were cursed")
    else:
        engine.score += 0.1
        gold = int(random.randint(10, 1000) * (1.1 ** (engine.hero.level - 1)))
        hero.gold += gold
        engine.notify(f"{gold} gold added")


class MapFactory(yaml.YAMLObject):

    @classmethod
    def from_yaml(cls, loader, node):
        _map = cls.Map()
        _obj = cls.Objects()
        config = loader.construct_mapping(node)
        for obj, count in config.items():
            if obj in object_list_prob['enemies']:
                prop = object_list_prob['enemies'][obj]
                units = [
                    Objects.Enemy(
                        prop['sprite'],
                        prop,
                        prop['experience'],
                        (random.randint(1, 39), random.randint(1, 39))
                    ) for _ in range(count)
                ]
                _obj.objects.extend(units)
            elif obj in object_list_prob['ally']:
                prop = object_list_prob['ally'][obj]
                units = [
                    Objects.Ally(
                        prop['sprite'],
                        prop['action'],
                        (random.randint(1, 39), random.randint(1, 39))
                    ) for _ in range(count)
                ]
                _obj.objects.extend(units)
            elif obj in object_list_prob['objects']:
                prop = object_list_prob['objects'][obj]
                units = [
                    Objects.Ally(
                        prop['sprite'],
                        prop['action'],
                        (random.randint(1, 39), random.randint(1, 39))
                    ) for _ in range(count)
                ]
                _obj.objects.extend(units)
            else:
                raise KeyError

        return {'map': _map, 'obj': _obj}

    @classmethod
    def create_map(cls):
        return cls.Map()

    @classmethod
    def create_objects(cls):
        return cls.Objects()


class BaseMap:

    def __init__(self, width=41, height=41):
        self.width = width
        self.height = height
        self.map = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or i == 40 or j == 40:
                    self.map[j][i] = wall
                elif i == 1 and j == 1:
                    self.map[j][i] = floor1
                else:
                    self.map[j][i] = [wall, floor1, floor2, floor3, floor1,
                                      floor2, floor3, floor1, floor2][
                        random.randint(0, 8)]

    def get_map(self):
        return self.map


class BaseObject:

    def __init__(self):
        self.objects = []

    def get_objects(self, _map):
        return self.objects


class EndMap(MapFactory):
    yaml_tag = "!end_map"

    class Map(BaseMap):
        def __init__(self):
            self.map = ['000000000000000000000000000000000000000',
                        '0                                     0',
                        '0                                     0',
                        '0  0   0   000   0   0  00000  0   0  0',
                        '0  0  0   0   0  0   0  0      0   0  0',
                        '0  000    0   0  00000  0000   0   0  0',
                        '0  0  0   0   0  0   0  0      0   0  0',
                        '0  0   0   000   0   0  00000  00000  0',
                        '0                                   0 0',
                        '0                                     0',
                        '000000000000000000000000000000000000000'
                        ]
            self.map = list(map(list, self.map))
            for i in self.map:
                for j in range(len(i)):
                    i[j] = wall if i[j] == '0' else floor1

    class Objects(BaseObject):
        pass


class RandomMap(MapFactory):
    yaml_tag = "!random_map"

    class Map(BaseMap):
        pass

    class Objects(BaseObject):

        def _set_objects(self, obj_type, obj_class, _map):
            min_coord = 2
            max_coord = 39
            for obj_name in object_list_prob[obj_type]:
                prop = object_list_prob[obj_type][obj_name]
                for i in range(random.randint(prop['min-count'],
                                              prop['max-count'])):
                    coord = (random.randint(min_coord, max_coord),
                             random.randint(min_coord, max_coord))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[1]][coord[0]] == wall:
                            intersect = True
                            coord = (random.randint(min_coord, max_coord),
                                     random.randint(min_coord, max_coord))
                            continue
                        for obj in self.objects:
                            if coord == obj.position or coord == (1, 1):
                                intersect = True
                                coord = (random.randint(min_coord, max_coord),
                                         random.randint(min_coord, max_coord))
                    if obj_class is Objects.Enemy:
                        self.objects.append(obj_class(prop['sprite'],
                                                      prop,
                                                      prop['experience'],
                                                      coord))
                    else:
                        self.objects.append(obj_class(prop['sprite'],
                                                      prop['action'],
                                                      coord))

        def get_objects(self, _map):
            self._set_objects('objects', Objects.Ally, _map)
            self._set_objects('ally', Objects.Ally, _map)
            self._set_objects('enemies', Objects.Enemy, _map)

            return self.objects


################################################################################
# My implementations
################################################################################


class EmptyMap(MapFactory):
    yaml_tag = '!empty_map'

    class Map(BaseMap):
        pass

    class Objects(BaseObject):
        pass


class SpecialMap(MapFactory):
    yaml_tag = '!special_map'

    class Map(BaseMap):
        pass

    class Objects(BaseObject):
        pass


################################################################################
# End of my implementations
################################################################################


wall = [0]
floor1 = [0]
floor2 = [0]
floor3 = [0]


def service_init(sprite_size: int, full=True):
    global object_list_prob, level_list

    global wall
    global floor1
    global floor2
    global floor3

    wall[0] = Objects.create_sprite(os.path.join("texture", "wall.png"),
                                    sprite_size)
    floor1[0] = Objects.create_sprite(os.path.join("texture", "Ground_1.png"),
                                      sprite_size)
    floor2[0] = Objects.create_sprite(os.path.join("texture", "Ground_2.png"),
                                      sprite_size)
    floor3[0] = Objects.create_sprite(os.path.join("texture", "Ground_3.png"),
                                      sprite_size)

    file = open("objects.yml", "r")

    object_list_tmp = yaml.load(file.read())
    if full:
        object_list_prob = object_list_tmp

    object_list_actions = {'reload_game': reload_game,
                           'add_gold': add_gold,
                           'apply_blessing': apply_blessing,
                           'remove_effect': remove_effect,
                           'restore_hp': restore_hp}

    for obj in object_list_prob['objects']:
        prop = object_list_prob['objects'][obj]
        prop_tmp = object_list_tmp['objects'][obj]
        prop['sprite'][0] = Objects.create_sprite(
            os.path.join(OBJECT_TEXTURE, prop_tmp['sprite'][0]), sprite_size)
        prop['action'] = object_list_actions[prop_tmp['action']]

    for ally in object_list_prob['ally']:
        prop = object_list_prob['ally'][ally]
        prop_tmp = object_list_tmp['ally'][ally]
        prop['sprite'][0] = Objects.create_sprite(
            os.path.join(ALLY_TEXTURE, prop_tmp['sprite'][0]), sprite_size)
        prop['action'] = object_list_actions[prop_tmp['action']]

    for enemy in object_list_prob['enemies']:
        prop = object_list_prob['enemies'][enemy]
        prop_tmp = object_list_tmp['enemies'][enemy]
        prop['sprite'][0] = Objects.create_sprite(
            os.path.join(ENEMY_TEXTURE, prop_tmp['sprite'][0]), sprite_size)

    file.close()

    if full:
        file = open("levels.yml", "r")
        level_list = yaml.load(file.read())['levels']
        level_list.append({'map': EndMap.Map(), 'obj': EndMap.Objects()})
        file.close()
