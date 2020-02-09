import math


class Base:

    pass


class A:
    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
            / len(ans)

    def get_loss(self):
        return sum(
            [(x - y) * (x - y) for (x, y) in zip(self.data, self.result)])


class B:
    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_loss(self):
        return -sum([
            y * math.log(x) + (1 - y) * math.log(1 - x)
            for (x, y) in zip(self.data, self.result)
        ])

    def get_pre(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(ans)

    def get_rec(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans, self.result)]
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C:
    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
            / len(ans)

    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data, self.result)])


def test(classA, classB, classC):
    a = A([1, .5, .4, .1, .7, .9], [1, .1, .7, .2, .4, .9, .5, .1])
    b = B([1, .5, .4, .1, .7, .9], [1, .1, .7, .2, .4, .9, .5, .1])
    c = C([1, .5, .4, .1, .7, .9], [1, .1, .7, .2, .4, .9, .5, .1])
    print(a.get_score())
    print(b.get_score())
    print(c.get_score())


if __name__ == '__main__':
    test()
