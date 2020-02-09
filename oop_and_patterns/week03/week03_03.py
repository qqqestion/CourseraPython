from abc import ABC, abstractmethod


class ObservableEngine(Engine):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self, achievements=None):
        self.achievements = achievements or set()  # save only title

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):

    def __init__(self, achievements=None):
        self.achievements = achievements or list()  # save whole dict

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)
