class Character:

    def __init__(self, name, xp=0, passed_quests=None, taken_quests=None):
        self.name = name
        self.xp = xp
        self.passed_quests = passed_quests or set()
        self.taken_quests = taken_quests or set()


def add_quest_spaek(char):
    quest_name = 'Talk to farmer'
    xp = 100
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f'Quest accepted: "{quest_name}"')
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f'Quest done: "{quest_name}"')
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp


def add_quest_hunt(char):
    quest_name = 'Hunt for rats'
    xp = 300
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f'Quest accepted: "{quest_name}"')
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f'Quest done: "{quest_name}"')
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp


def add_quest_carry(char):
    quest_name = 'Carry resources'
    xp = 200
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f'Quest accepted: "{quest_name}"')
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f'Quest done: "{quest_name}"')
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp


class QuestGiver:

    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def handle_quests(self, character):
        for quest in self.quests:
            quest(character)


if __name__ == '__main__':
    all_quests = [add_quest_carry, add_quest_hunt, add_quest_spaek]
    quest_giver = QuestGiver()
    for quest in all_quests:
        quest_giver.add_quest(quest)

    player = Character('Tom')
    print('Example1')
    quest_giver.handle_quests(player)
    print()

    print('Example2')
    player.taken_quests = {'Carry resources', 'Hunt for rats'}
    quest_giver.handle_quests(player)
    print()

    print('Example3')
    quest_giver.handle_quests(player)
    print()
