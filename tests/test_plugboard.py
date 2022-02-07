import unittest

from plugboard import Plugboard


class TestPlugboardBaseEncoding(unittest.TestCase):
    def test_patch_big_a_b(self):
        test_plugboard = Plugboard()
        test_plugboard.patch('A', 'B')
        result = test_plugboard.mappings['A']
        self.assertEqual('B', result)


if __name__ == '__main__':
    unittest.main()
