import math
from abc import ABC, abstractclassmethod


class Base(ABC):

    def __init__(self, data, result):
        self.data = data
        self.result = result
        self._answer = [int(x >= 0.5) for x in self.data]

    def get_answer(self):
        return self._answer

    @abstractclassmethod
    def get_score(self):
        pass

    @abstractclassmethod
    def get_loss(self):
        pass


class A(Base):

    def get_score(self):
        return sum([int(x == y) for (x, y) in zip(self._answer, self.result)]) \
               / len(self._answer)

    def get_loss(self):
        return sum(
            [(x - y) * (x - y) for (x, y) in zip(self.data, self.result)])


class B(Base):

    def get_loss(self):
        return -sum([
            y * math.log(x) + (1 - y) * math.log(1 - x)
            for (x, y) in zip(self.data, self.result)
        ])

    def get_pre(self):
        res = [int(x == 1 and y == 1)
               for (x, y) in zip(self._answer, self.result)]
        return sum(res) / sum(self._answer)

    def get_rec(self):
        res = [int(x == 1 and y == 1)
               for (x, y) in zip(self._answer, self.result)]
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(A):

    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data, self.result)])


if __name__ == '__main__':
    pass
