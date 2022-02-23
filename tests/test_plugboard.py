import unittest
from source.plugboard import *


class TestPlugboardBaseEncoding(unittest.TestCase):
    def test_patch_big_a_b(self):
        plugboard = Plugboard()
        plugboard.add(PlugLead('AB'))
        result = plugboard.mappings['A']
        self.assertEqual('B', result)


class TestPlugboardPlugLeads(unittest.TestCase):
    def test_add_encode_provided_test_1(self):
        plugboard = Plugboard()
        plugboard.add(PlugLead("SZ"))
        plugboard.add(PlugLead("GT"))
        plugboard.add(PlugLead("DV"))
        plugboard.add(PlugLead("KU"))
        self.assertEqual('U', plugboard.encode("K"))

    def test_add_encode_provided_test_2(self):
        plugboard = Plugboard()
        plugboard.add(PlugLead("SZ"))
        plugboard.add(PlugLead("GT"))
        plugboard.add(PlugLead("DV"))
        plugboard.add(PlugLead("KU"))
        self.assertEqual('A', plugboard.encode("A"))

    def test_add_11th_pluglead(self):
        plugboard = Plugboard()
        plugboard.add(PlugLead('AB'))
        plugboard.add(PlugLead('CK'))
        plugboard.add(PlugLead('EF'))
        plugboard.add(PlugLead('GH'))
        plugboard.add(PlugLead('IJ'))
        plugboard.add(PlugLead('DL'))
        plugboard.add(PlugLead('MN'))
        plugboard.add(PlugLead('OP'))
        plugboard.add(PlugLead('QR'))
        plugboard.add(PlugLead('SU'))
        plugboard.add(PlugLead('XZ'))
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
