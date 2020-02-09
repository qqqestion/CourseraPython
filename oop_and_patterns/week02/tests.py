import unittest
from oop_and_patterns.week02.week02_01 import A, B, C, Base
# from week02_01 import A, B, C
import oop_and_patterns.week02.expected as ex


class BaseTest(unittest.TestCase):

    def test_with_one(self):
        data = [1, .5, .4, .1, .7, .9]
        result = [1, .1, .7, .2, .4, .9, .5, .1]
        a = A(data, result)
        b = B(data, result)
        c = C(data, result)

        exa = ex.A(data, result)
        exb = ex.B(data, result)
        exc = ex.C(data, result)

        for mine, expected in zip([a, b, c], [exa, exb, exc]):
            with self.subTest(x=(mine, expected)):
                self.assertEqual(mine.get_answer(), expected.get_answer())
                self.assertEqual(mine.get_score(), expected.get_score())

    def test_without_one(self):
        data = [.1, .5, .4, .1, .7, .9]
        result = [.1, .1, .7, .2, .4, .9, .5, .1]
        a = A(data, result)
        b = B(data, result)
        c = C(data, result)

        exa = ex.A(data, result)
        exb = ex.B(data, result)
        exc = ex.C(data, result)

        for mine, expected in zip([a, b, c], [exa, exb, exc]):
            with self.subTest(x=(mine, expected)):
                self.assertEqual(mine.get_loss(), expected.get_loss())
