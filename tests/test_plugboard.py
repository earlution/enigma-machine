import unittest
from source.plugboard import PlugLead


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


class TestPlugLead(unittest.TestCase):
    def test_encode_big_ag_1(self):
        pluglead = PlugLead('AG')
        result = pluglead.encode('A')
        self.assertEqual('G', result)

    def test_encode_big_ag_2(self):
        pluglead = PlugLead('AG')
        result = pluglead.encode('D')
        self.assertEqual('D', result)

    def test_encode_big_da_1(self):
        pluglead = PlugLead('DA')
        result = pluglead.encode('A')
        self.assertEqual('D', result)

    def test_encode_big_da_2(self):
        pluglead = PlugLead('DA')
        result = pluglead.encode('D')
        self.assertEqual('A', result)

if __name__ == '__main__':
    unittest.main()
