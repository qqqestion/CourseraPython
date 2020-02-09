class Character:

    def __init__(self, name, xp=0, passed_quests=None, taken_quests=None):
        self.name = name
        self.xp = xp
        self.passed_quests = passed_quests or set()
        self.taken_quests = taken_quests or set()


QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = 'QSPEAK', 'QHUND', 'QCARRY'


class Event:

    def __init__(self, kind):
        self.kind = kind


class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, character, event):
        if self.__successor is not None:
            self.__successor.handle(character, event)


class QuestSpeak(NullHandler):

    def handle(self, character, event):
        if event.kind == QUEST_SPEAK:
            quest_name = 'Talk to farmer'
            xp = 100
            if quest_name not in (
                    character.passed_quests | character.taken_quests):
                print(f'Quest accepted: "{quest_name}"')
                character.taken_quests.add(quest_name)
            elif quest_name in character.taken_quests:
                print(f'Quest done: "{quest_name}"')
                character.passed_quests.add(quest_name)
                character.taken_quests.remove(quest_name)
                character.xp += xp
        else:
            print('Passing event father')
            super().handle(character, event)


class QuestHunt(NullHandler):

    def handle(self, character, event):
        if event.kind == QUEST_HUNT:
            quest_name = 'Hunt for rats'
            xp = 300
            if quest_name not in (
                    character.passed_quests | character.taken_quests):
                print(f'Quest accepted: "{quest_name}"')
                character.taken_quests.add(quest_name)
            elif quest_name in character.taken_quests:
                print(f'Quest done: "{quest_name}"')
                character.passed_quests.add(quest_name)
                character.taken_quests.remove(quest_name)
                character.xp += xp
        else:
            print('Passing event father')
            super().handle(character, event)


class QuestCarry(NullHandler):

    def handle(self, character, event):
        if event.kind == QUEST_CARRY:
            quest_name = 'Carry resources'
            xp = 300
            if quest_name not in (
                    character.passed_quests | character.taken_quests):
                print(f'Quest accepted: "{quest_name}"')
                character.taken_quests.add(quest_name)
            elif quest_name in character.taken_quests:
                print(f'Quest done: "{quest_name}"')
                character.passed_quests.add(quest_name)
                character.taken_quests.remove(quest_name)
                character.xp += xp
        else:
            print('Passing event father')
            super().handle(character, event)


class QuestGiver:

    def __init__(self):
        self.handlers = QuestCarry(QuestHunt(QuestSpeak(NullHandler)))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, character):
        for event in self.events:
            self.handlers.handle(character, event)


if __name__ == '__main__':
    events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]
    quest_giver = QuestGiver()
    for quest in events:
        quest_giver.add_event(quest)

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
