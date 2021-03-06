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
        result = enigma.encode(letter)
        self.assertEqual('A', result)


class TestRotorListValue(unittest.TestCase):
    def test_rotor_i_a(self):
        test_rotor = Rotor('I')
        self.assertEqual('E', test_rotor.encodings[0])

    def test_rotor_i_n(self):
        test_rotor = Rotor('I')
        self.assertEqual('W', test_rotor.encodings[13])

    def test_rotor_i_z(self):
        test_rotor = Rotor('I')
        self.assertEqual('J', test_rotor.encodings[25])

    def test_rotor_ii_a(self):
        test_rotor = Rotor('II')
        self.assertEqual('A', test_rotor.encodings[0])

    def test_rotor_ii_n(self):
        test_rotor = Rotor('II')
        self.assertEqual('T', test_rotor.encodings[13])

    def test_rotor_ii_z(self):
        test_rotor = Rotor('II')
        self.assertEqual('E', test_rotor.encodings[25])

    def test_rotor_iii_a(self):
        test_rotor = Rotor('III')
        self.assertEqual('B', test_rotor.encodings[0])

    def test_rotor_iii_n(self):
        test_rotor = Rotor('III')
        self.assertEqual('N', test_rotor.encodings[13])

    def test_rotor_iii_z(self):
        test_rotor = Rotor('III')
        self.assertEqual('O', test_rotor.encodings[25])

    def test_rotor_iv_a(self):
        test_rotor = Rotor('IV')
        self.assertEqual('E', test_rotor.encodings[0])

    def test_rotor_iv_n(self):
        test_rotor = Rotor('IV')
        self.assertEqual('H', test_rotor.encodings[13])

    def test_rotor_iv_z(self):
        test_rotor = Rotor('IV')
        self.assertEqual('B', test_rotor.encodings[25])

    def test_rotor_v_a(self):
        test_rotor = Rotor('V')
        self.assertEqual('V', test_rotor.encodings[0])

    def test_rotor_v_b(self):
        test_rotor = Rotor('V')
        self.assertEqual('Z', test_rotor.encodings[1])

    def test_rotor_v_c(self):
        test_rotor = Rotor('V')
        self.assertEqual('B', test_rotor.encodings[2])

    def test_rotor_v_d(self):
        test_rotor = Rotor('V')
        self.assertEqual('R', test_rotor.encodings[3])

    def test_rotor_v_f(self):
        test_rotor = Rotor('V')
        self.assertEqual('I', test_rotor.encodings[5])

    def test_rotor_v_n(self):
        test_rotor = Rotor('V')
        self.assertEqual('H', test_rotor.encodings[13])

    def test_rotor_v_y(self):
        test_rotor = Rotor('V')
        self.assertEqual('C', test_rotor.encodings[24])

    def test_rotor_v_z(self):
        test_rotor = Rotor('V')
        self.assertEqual('K', test_rotor.encodings[25])

    def test_rotor_1_name_error(self):
        try:
            test_rotor = Rotor('1')
        except:
            NameError


class TestRotorEncode(unittest.TestCase):
    def test_rotor_i_encode_a_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('A')
        self.assertEqual('K', result)

    def test_rotor_i_encode_a_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('a')
        self.assertEqual('K', result)

    def test_rotor_i_encode_n_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('N')
        self.assertEqual('Y', result)

    def test_rotor_i_encode_n_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('n')
        self.assertEqual('Y', result)

    def test_rotor_i_encode_z_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('Z')
        self.assertEqual('E', result)

    def test_rotor_i_encode_z_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('z')
        self.assertEqual('E', result)

    def test_rotor_ii_encode_a_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('A')
        self.assertEqual('J', result)

    def test_rotor_ii_encode_a_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('a')
        self.assertEqual('J', result)

    def test_rotor_ii_encode_n_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('N')
        self.assertEqual('M', result)

    def test_rotor_ii_encode_n_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('n')
        self.assertEqual('M', result)

    def test_rotor_ii_encode_z_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('Z')
        self.assertEqual('A', result)

    def test_rotor_ii_encode_z_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('z')
        self.assertEqual('A', result)

    def test_rotor_iii_encode_a_big(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('A')
        self.assertEqual('D', result)

    def test_rotor_iii_encode_a_little(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('a')
        self.assertEqual('D', result)

    def test_rotor_iii_encode_n(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('N')
        self.assertEqual('Y', result)

    def test_rotor_iii_encode_z(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('Z')
        self.assertEqual('B', result)

    def test_rotor_iv_encode_a_big(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('A')
        self.assertEqual('S', result)

    def test_rotor_iv_encode_n(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('N')
        self.assertEqual('X', result)

    def test_rotor_iv_encode_z(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('Z')
        self.assertEqual('E', result)

    def test_rotor_v_encode_a_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('A')
        self.assertEqual('Z', result)

    def test_rotor_v_encode_a_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('a')
        self.assertEqual('Z', result)

    def test_rotor_v_encode_n_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('N')
        self.assertEqual('L', result)

    def test_rotor_v_encode_n_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('n')
        self.assertEqual('L', result)

    def test_rotor_v_encode_z_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('Z')
        self.assertEqual('V', result)

    def test_rotor_v_encode_z_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('z')
        self.assertEqual('V', result)

class TestRotorRevEncode(unittest.TestCase):
    def test_rotor_i_encode_a_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('A', True)
        self.assertEqual('U', result)

    def test_rotor_i_encode_a_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('a', True)
        self.assertEqual('U', result)

    def test_rotor_i_encode_n_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('N', True)
        self.assertEqual('K', result)

    def test_rotor_i_encode_n_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('n', True)
        self.assertEqual('K', result)

    def test_rotor_i_encode_z_big(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('Z', True)
        self.assertEqual('J', result)

    def test_rotor_i_encode_z_little(self):
        test_rotor = Rotor('I')
        result = test_rotor.encode('z', True)
        self.assertEqual('J', result)

    def test_rotor_ii_encode_a_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('A', True)
        self.assertEqual('A', result)

    def test_rotor_ii_encode_a_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('a', True)
        self.assertEqual('A', result)

    def test_rotor_ii_encode_n_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('N', True)
        self.assertEqual('T', result)

    def test_rotor_ii_encode_n_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('n', True)
        self.assertEqual('T', result)

    def test_rotor_ii_encode_z_big(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('Z', True)
        self.assertEqual('S', result)

    def test_rotor_ii_encode_z_little(self):
        test_rotor = Rotor('II')
        result = test_rotor.encode('z', True)
        self.assertEqual('S', result)

    def test_rotor_iii_encode_a_big(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('A', True)
        self.assertEqual('T', result)

    def test_rotor_iii_encode_a_little(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('a', True)
        self.assertEqual('T', result)

    def test_rotor_iii_encode_n(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('N', True)
        self.assertEqual('N', result)

    def test_rotor_iii_encode_z(self):
        test_rotor = Rotor('III')
        result = test_rotor.encode('Z', True)
        self.assertEqual('M', result)

    def test_rotor_iv_encode_a_big(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('A', True)
        self.assertEqual('H', result)

    def test_rotor_iv_encode_n(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('N', True)
        self.assertEqual('Q', result)

    def test_rotor_iv_encode_z(self):
        test_rotor = Rotor('IV')
        result = test_rotor.encode('Z', True)
        self.assertEqual('F', result)

    def test_rotor_v_encode_a_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('A', True)
        self.assertEqual('Q', result)

    def test_rotor_v_encode_a_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('a', True)
        self.assertEqual('Q', result)

    def test_rotor_v_encode_n_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('N', True)
        self.assertEqual('M', result)

    def test_rotor_v_encode_n_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('n', True)
        self.assertEqual('M', result)

    def test_rotor_v_encode_z_big(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('Z', True)
        self.assertEqual('B', result)

    def test_rotor_v_encode_z_little(self):
        test_rotor = Rotor('V')
        result = test_rotor.encode('z', True)
        self.assertEqual('B', result)


class TestRotorRotate(unittest.TestCase):
    def test_rotor_i_a_from_pos_a(self):
        test_rotor = Rotor('I', 1)
        result = test_rotor.encode('A')
        self.assertEqual('K', result)
        self.assertEqual(2, test_rotor.ring_position)


class TestRotorRing(unittest.TestCase):
    def test_rotor_i_set_ring_position_2(self):
        test_rotor = Rotor('I')
        test_rotor.set_ring_setting(2)
        ring_pos_result = test_rotor.get_ring_setting()
        encode_result = test_rotor.encode('A')
        self.assertEqual(2, ring_pos_result)
        self.assertEqual('M', encode_result)


class TestRotorsAbstractFactory(unittest.TestCase):

    def test_is_a_rotor(self):
        rotors = Rotors()
        rotor = rotors.setup(RotorII)
        self.assertEqual(True, isinstance(rotor, Rotor))
        print(type(rotor))

if __name__ == '__main__':
    unittest.main()
