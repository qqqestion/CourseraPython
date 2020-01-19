import json
import unittest
from unittest.mock import patch
from week04.asteroid import Asteroid


class TestPython(unittest.TestCase):

    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))
        print('test_float_to_int_coercion is correct')

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))
        print('test_get_empty_dict is correct')

    def test_trueness(self):
        self.assertTrue(bool(10))
        print('test_trueness is correct')

    def test_integer_division(self):
        self.assertIs(10 / 5, 2)




class TestAsteroid(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.asteroid = Asteroid(2099942)

    def setUp(self):
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        with open('../files/apophis.txt') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        self.assertEqual(
            self.asteroid.name, '99942 Apophis (2004 MN4)'
        )
        print('test_name is correct')

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)
        print('test_diameter is correct')


# def main():
#     a = TestPython()
#     a.test_float_to_int_coercion()
#     a.test_get_empty_dict()
#     a.test_trueness()
#     # a.test_integer_division() # causes error
#
#     apophis = Asteroid(2099942)
#     print(f'Name: {apophis.name}')
#     print(f'Diameter: {apophis.diameter}')
#
#     tests = TestAsteroid()
#     tests.test_name()
#     tests.test_diameter()
#
#
# if __name__ == '__main__':
#     main()
