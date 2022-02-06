import unittest
from rotor import *


class TestRotors(unittest.TestCase):
    def test_rotor_i_a(self):
        test_rotor = Rotor('I')
        self.assertEqual('E', test_rotor.rotor['A'])

    def test_rotor_i_n(self):
        test_rotor = Rotor('I')
        self.assertEqual('W', test_rotor.rotor['N'])

    def test_rotor_i_z(self):
        test_rotor = Rotor('I')
        self.assertEqual('J', test_rotor.rotor['Z'])

    def test_rotor_ii_a(self):
        test_rotor = Rotor('II')
        self.assertEqual('A', test_rotor.rotor['A'])

    def test_rotor_ii_n(self):
        test_rotor = Rotor('II')
        self.assertEqual('T', test_rotor.rotor['N'])

    def test_rotor_ii_z(self):
        test_rotor = Rotor('II')
        self.assertEqual('E', test_rotor.rotor['Z'])

    def test_rotor_iii_a(self):
        test_rotor = Rotor('III')
        self.assertEqual('B', test_rotor.rotor['A'])

    def test_rotor_iii_n(self):
        test_rotor = Rotor('III')
        self.assertEqual('N', test_rotor.rotor['N'])

    def test_rotor_iii_z(self):
        test_rotor = Rotor('III')
        self.assertEqual('O', test_rotor.rotor['Z'])

    def test_rotor_iv_a(self):
        test_rotor = Rotor('IV')
        self.assertEqual('E', test_rotor.rotor['A'])

    def test_rotor_iv_n(self):
        test_rotor = Rotor('IV')
        self.assertEqual('H', test_rotor.rotor['N'])

    def test_rotor_iv_z(self):
        test_rotor = Rotor('IV')
        self.assertEqual('B', test_rotor.rotor['Z'])

    def test_rotor_v_a(self):
        test_rotor = Rotor('V')
        self.assertEqual('V', test_rotor.rotor['A'])

    def test_rotor_v_b(self):
        test_rotor = Rotor('V')
        self.assertEqual('Z', test_rotor.rotor['B'])

    def test_rotor_v_c(self):
        test_rotor = Rotor('V')
        self.assertEqual('B', test_rotor.rotor['C'])

    def test_rotor_v_d(self):
        test_rotor = Rotor('V')
        self.assertEqual('R', test_rotor.rotor['D'])

    def test_rotor_v_f(self):
        test_rotor = Rotor('V')
        self.assertEqual('I', test_rotor.rotor['F'])

    def test_rotor_v_n(self):
        test_rotor = Rotor('V')
        self.assertEqual('H', test_rotor.rotor['N'])

    def test_rotor_v_y(self):
        test_rotor = Rotor('V')
        self.assertEqual('C', test_rotor.rotor['Y'])

    def test_rotor_v_z(self):
        test_rotor = Rotor('V')
        self.assertEqual('K', test_rotor.rotor['Z'])
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
