import unittest

from plugboard import Plugboard


class TestPlugboardBaseEncoding(unittest.TestCase):
    def test_patch_big_a_b(self):
        test_plugboard = Plugboard()
        test_plugboard.patch('A', 'B')
        result = test_plugboard.mappings['A']
        self.assertEqual('B', result)


class TestPlugboardPlugleads(unittest.TestCase):
    def test_add_11th_pluglead(self):
        test_plugboard = Plugboard()
        test_plugboard.patch('A', 'B')
        test_plugboard.patch('C', 'K')
        test_plugboard.patch('E', 'F')
        test_plugboard.patch('G', 'H')
        test_plugboard.patch('I', 'J')
        test_plugboard.patch('D', 'L')
        test_plugboard.patch('M', 'N')
        test_plugboard.patch('O', 'P')
        test_plugboard.patch('Q', 'R')
        test_plugboard.patch('S', 'U')
        test_plugboard.patch('X', 'Z')
        # @TODO do this test properly


if __name__ == '__main__':
    unittest.main()
