import unittest
from enigma import Enigma
from rotors import *


class TestEnigma(unittest.TestCase):
    def test_vanilla_press_big_a_stages(self):
        letter = 'A'
        enigma = Enigma()
        pb_result = enigma.plugboard.encode(letter)
        r1_result = enigma.rotors.rotor_1.encode(pb_result)
        r2_result = enigma.rotors.rotor_2.encode(r1_result)
        r3_result = enigma.rotors.rotor_3.encode(r2_result)
        self.assertEqual('A', pb_result)
        self.assertEqual('E', r1_result)
        self.assertEqual('S', r2_result)
        self.assertEqual('G', r3_result)

    def test_vanilla_press_big_a(self):
        letter = 'A'
        enigma = Enigma()
        result = enigma.press_key(letter)
        self.assertEqual('A', result)


class TestRotorsInHashtable(unittest.TestCase):
    def test_rotor_i_a(self):
        test_rotor = Rotor('I')
        self.assertEqual('E', test_rotor.rotor['A'])

    def test_rotor_i_a_little(self):
        test_rotor = Rotor('I')
        self.assertEqual('E', test_rotor.rotor['a'])

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

    def test_rotor_1_name_error(self):
        try:
            test_rotor = Rotor('1')
        except:
            NameError


class TestRotorEncode(unittest.TestCase):
    def test_rotor_i_encode_a_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('A')
        self.assertEqual('E', result)

    def test_rotor_i_encode_a_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('a')
        self.assertEqual('E', result)

    def test_rotor_i_encode_n_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('N')
        self.assertEqual('W', result)

    def test_rotor_i_encode_n_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('n')
        self.assertEqual('W', result)

    def test_rotor_i_encode_z_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('Z')
        self.assertEqual('J', result)

    def test_rotor_i_encode_z_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('z')
        self.assertEqual('J', result)

    def test_rotor_ii_encode_a_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('A')
        self.assertEqual('A', result)

    def test_rotor_ii_encode_a_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('a')
        self.assertEqual('A', result)

    def test_rotor_ii_encode_n_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('N')
        self.assertEqual('T', result)

    def test_rotor_ii_encode_n_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('n')
        self.assertEqual('T', result)

    def test_rotor_ii_encode_z_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('Z')
        self.assertEqual('E', result)

    def test_rotor_ii_encode_z_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('z')
        self.assertEqual('E', result)

    # @TODO add test for rotors III and IV

    def test_rotor_v_encode_a_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('A')
        self.assertEqual('V', result)

    def test_rotor_v_encode_a_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('a')
        self.assertEqual('V', result)

    def test_rotor_v_encode_n_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('N')
        self.assertEqual('H', result)

    def test_rotor_v_encode_n_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('n')
        self.assertEqual('H', result)

    def test_rotor_v_encode_z_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('Z')
        self.assertEqual('K', result)

    def test_rotor_v_encode_z_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('z')
        self.assertEqual('K', result)


class TestRotorRotate(unittest.TestCase):
    def test_rotor_i_a_from_pos_a(self):
        test_rotor = Rotor('I', 1)
        test_rotor.rotate()
        result = test_rotor.encode('A')
        self.assertEqual('J', result)
        self.assertEqual(2, test_rotor.position)


if __name__ == '__main__':
    unittest.main()
