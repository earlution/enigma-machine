import unittest
from source.reflector import *

# @TODO test various reversed rotor encodings
class TestReflectorReversedRotorEncodings(unittest.TestCase):
    def test_rotor_i_rev_a(self):
        self.assertEqual(True, False)  # add assertion here


class TestReflectorEncodings(unittest.TestCase):

    def test_reflector_a_encode_a(self):
        reflector = ReflectorA()
        result = reflector.encode('A')
        self.assertEqual('E', result)


if __name__ == '__main__':
    unittest.main()
