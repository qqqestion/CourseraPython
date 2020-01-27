import unittest


def fib(n):
    if n < 0 or not isinstance(n, int):
        raise ArithmeticError
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


class TestFibonacciNumbers(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def test_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib(n), fib_n)

    def test_positive(self):
        self.assertEqual(fib(10), 55)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -1)
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -10)

    def test_fractional(self):
        self.assertRaises(ArithmeticError, fib, 2.4)


def sort_algorithm(lst):
    pass


def is_not_in_descending_order(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True


class TestSort(unittest.TestCase):

    def setUp(self):
        self.cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(1, 10)), list(range(9, 0, -1)))

    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(1, 10)), list(range(9, 0, -1)))
        # for b in cases:
        for b in self.cases:
            with self.subTest(case=b):
                a = list(b)
                sort_algorithm(a)
                self.assertCountEqual(a, b)
                self.assertTrue(is_not_in_descending_order(a))


if __name__ == '__main__':
    unittest.main()
