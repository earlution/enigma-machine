import unittest
from source.reflector import *

# @TODO test various reversed rotor encodings
class TestReflectorReversedRotorEncodings(unittest.TestCase):
    def test_rotor_i_rev_a(self):
        self.assertEqual(True, False)  # add assertion here


class TestReflectorEncodings(unittest.TestCase):

    def test_reflector_a_encode_a(self):
        reflector = ReflectorA('A')
        result = reflector.encode('A')
        self.assertEqual('E', result)

    def test_reflector_b_encode_l(self):
        reflector = ReflectorB()
        result = reflector.encode('N')
        self.assertEqual('K', result)


if __name__ == '__main__':
    unittest.main()
