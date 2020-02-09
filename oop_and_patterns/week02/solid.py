"""
SOLID principles
. single responsibility principle: class should have only one job. So if a class
  has more that one responsibility, it becomes coupled. A change to one
  responsibility results to modification of the other responsibility.
. open-closed principle: software entities (classes, modules, functions) should
  be open for extension, not modification.
. Liskov substitution principle: functions that required base class have to
  use subclasses without even noticing. This means that clients are completely
  isolated and unaware of changes in the class hierarchy.
. interface segregation principle: make fine grained interfaces that are client
  specific Clients should not be forced to depend upon interfaces that they do
  not use. This principle deals with the disadvantages of implementing big
  interfaces.
. dependency inversion principle: dependency should be on abstractions not
  concretions. High-level modules should not depend upon low-level modules.
  Both low and high level classes should depend on the same abstractions.
  Abstractions should not depend on details. Details should depend upon
  abstractions.
"""

""" PRINCIPLE 1 """


# incorrect
class EventHandler:

    def handle_event1(self, event):
        # first event processing
        pass

    def handle_event2(self, event):
        # second event processing
        pass

    def handle_event3(self, event):
        # third event processing
        pass

    def database_logger(self, event):
        # method for writing log to the database
        pass


# correct
class EventHandler:

    def handle_event1(self, event):
        # first event processing
        pass

    def handle_event2(self, event):
        # second event processing
        pass

    def handle_event3(self, event):
        # third event processing
        pass


class DatabaseLogger:

    def database_logger(self, event):
        # method for writing log to the database
        pass


""" PRINCIPLE 2 """


# incorrect
class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4


# correct
class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):

    def give_discount(self):
        return super().give_discount() * 0.2


""" PRINCIPLE 3 """


# incorrect
class Parent:

    def __init(self, value):
        self.value = value

    def do_something(self):
        print('Function was called')


class Child(Parent):

    def do_something(self):
        super().do_something()
        self.value = 0


def function(obj: Parent):
    obj.do_something()
    if obj.value > 0:
        print('All correct')
    else:
        print('SOMETHING IS GOING WRONG!')


parent = Parent(5)
function(parent)
print()

# incorrect behavior
child = Child(5)
function(child)
print()

""" PRINCIPLE 4 """

import math


# incorrect


class AllScoresCalculator:

    def calculate_accuracy(self, y_true, y_pred):
        return sum(int(x == y) for x, y in zip(y_true, y_pred)) / len(y_true)

    def log_loss(self, y_true, y_pred):
        return sum(
            (x * math.log(y) + (1 - x) * math.log(1 - y))
            for x, y in zip(y_true, y_pred)
        ) / len(y_true)


# correct
class CalculateLosses:
    def log_loss(self, y_true, y_pred):
        return sum(
            (x * math.log(y) + (1 - x) * math.log(1 - y))
            for x, y in zip(y_true, y_pred)
        ) / len(y_true)


class CalculateMetrics:
    def calculate_accuracy(self, y_true, y_pred):
        return sum(int(x == y) for x, y in zip(y_true, y_pred)) / len(y_true)


""" PRINCIPLE 5 """


class AuthenticationForUser:

    def __init(self, connector):
        self.connection = connector.connect()

    def authenticate(self, credentials):
        pass

    def is_authenticated(self):
        pass

    def last_login(self):
        pass


class AnonymousAuth(AuthenticationForUser):
    pass


class GithubAuth(AuthenticationForUser):

    def last_login(self):
        pass


class FacebookAuth(AuthenticationForUser):
    pass


class Permissions:

    def __init__(self, auth: AuthenticationForUser):
        self.auth = auth

    def has_permissions(self):
        pass


class IsLoggedInPermissions(Permissions):

    def last_login(self):
        return self.auth.last_login()
    