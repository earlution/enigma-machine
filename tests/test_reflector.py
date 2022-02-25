import unittest
from source.reflector import *

# @TODO test various reversed rotor encodings
class TestReflectorReversedRotorEncodings(unittest.TestCase):
    def test_rotor_i_rev_a(self):
        self.assertEqual(True, False)  # add assertion here


class TestReflectorEncodings(unittest.TestCase):

    # obviously this will work, this is here for potential of dynamic creation of polymorphic reflectors
    def test_reflector_default_encode_a(self):
        reflector = ReflectorA()
        result = reflector.encode('A')
        self.assertEqual('E', result)

    def test_reflector_a_encode_a(self):
        reflector = ReflectorA()
        result = reflector.encode('A')
        self.assertEqual('E', result)

    def test_reflector_a_encode_n(self):
        reflector = ReflectorA()
        result = reflector.encode('N')
        self.assertEqual('R', result)

    def test_reflector_a_encode_n(self):
        reflector = ReflectorA()
        result = reflector.encode('Z')
        self.assertEqual('D', result)

    def test_reflector_b_encode_a(self):
        reflector = ReflectorB()
        result = reflector.encode('A')
        self.assertEqual('Y', result)

    def test_reflector_b_encode_n(self):
        reflector = ReflectorB()
        result = reflector.encode('N')
        self.assertEqual('K', result)

    def test_reflector_b_encode_n(self):
        reflector = ReflectorB()
        result = reflector.encode('Z')
        self.assertEqual('T', result)

    def test_reflector_c_encode_a(self):
        reflector = ReflectorC()
        result = reflector.encode('A')
        self.assertEqual('F', result)

    def test_reflector_c_encode_n(self):
        reflector = ReflectorC()
        result = reflector.encode('N')
        self.assertEqual('W', result)

    def test_reflector_c_encode_n(self):
        reflector = ReflectorC()
        result = reflector.encode('Z')
        self.assertEqual('L', result)

    def test_reflector_bthin_encode_a(self):
        reflector = ReflectorBThin()
        result = reflector.encode('A')
        self.assertEqual('E', result)

    def test_reflector_bthin_encode_n(self):
        reflector = ReflectorBThin()
        result = reflector.encode('N')
        self.assertEqual('B', result)

    def test_reflector_bthin_encode_n(self):
        reflector = ReflectorBThin()
        result = reflector.encode('Z')
        self.assertEqual('S', result)

    def test_reflector_cthin_encode_a(self):
        reflector = ReflectorCThin()
        result = reflector.encode('A')
        self.assertEqual('R', result)

    def test_reflector_cthin_encode_n(self):
        reflector = ReflectorCThin()
        result = reflector.encode('N')
        self.assertEqual('F', result)

    def test_reflector_cthin_encode_n(self):
        reflector = ReflectorCThin()
        result = reflector.encode('Z')
        self.assertEqual('Q', result)

    def test_reflector_etw_encode_a(self):
        reflector = ReflectorETW()
        result = reflector.encode('A')
        self.assertEqual('A', result)

    def test_reflector_etw_encode_n(self):
        reflector = ReflectorETW()
        result = reflector.encode('N')
        self.assertEqual('N', result)

    def test_reflector_etw_encode_n(self):
        reflector = ReflectorETW()
        result = reflector.encode('Z')
        self.assertEqual('Z', result)



if __name__ == '__main__':
    unittest.main()
