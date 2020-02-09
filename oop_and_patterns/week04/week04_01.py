class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    type_id = 0

    def __init__(self, type_):
        self.type = type_


class EventSet:
    type_id = 1

    def __init__(self, value):
        self.value = value


class NullHandler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor is not None:
            if event.type_id == 0:
                res = self.successor.handle(obj, event)
                return res
            else:
                self.successor.handle(obj, event)


class IntHandler(NullHandler):

    def handle(self, obj, event):
        if event.type_id == 0:
            if event.type == int:
                return obj.integer_field
            else:
                # print('Passing int get event')
                return super().handle(obj, event)
        elif event.type_id == 1:
            if isinstance(event.value, int):
                obj.integer_field = event.value
            else:
                # print('Passing int set event')
                super().handle(obj, event)


class FloatHandler(NullHandler):

    def handle(self, obj, event):
        if event.type_id == 0:
            if event.type == float:
                return obj.float_field
            else:
                # print('Passing float get event')
                return super().handle(obj, event)
        elif event.type_id == 1:
            if isinstance(event.value, float):
                obj.float_field = event.value
            else:
                # print('Passing float set event')
                super().handle(obj, event)


class StrHandler(NullHandler):

    def handle(self, obj, event):
        if event.type_id == 0:
            if event.type == str:
                return obj.string_field
            else:
                # print('Passing str get event')
                return super().handle(obj, event)
        elif event.type_id == 1:
            if isinstance(event.value, str):
                obj.string_field = event.value
            else:
                # print('Passing str set event')
                super().handle(obj, event)


if __name__ == '__main__':
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))
    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
    'new text'
