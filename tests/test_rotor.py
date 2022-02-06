import unittest
from rotor import *


class TestRotors(unittest.TestCase):
    def test_rotor_i_a(self):
        test_rotor = Rotor('I')
        self.assertEqual(test_rotor.rotor['A'], 'E')

    def test_rotor_i_n(self):
        test_rotor = Rotor('I')
        self.assertEqual(test_rotor.rotor['N'], 'W')

    def test_rotor_i_z(self):
        test_rotor = Rotor('I')
        self.assertEqual(test_rotor.rotor['Z'], 'J')

    def test_rotor_ii_a(self):
        test_rotor = Rotor('II')
        self.assertEqual(test_rotor.rotor['A'], 'A')

    def test_rotor_ii_n(self):
        test_rotor = Rotor('II')
        self.assertEqual(test_rotor.rotor['N'], 'T')

    def test_rotor_ii_z(self):
        test_rotor = Rotor('II')
        self.assertEqual(test_rotor.rotor['Z'], 'E')


if __name__ == '__main__':
    unittest.main()
