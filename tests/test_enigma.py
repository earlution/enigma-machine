import unittest
from enigma import Enigma


class TestEnigma(unittest.TestCase):
    def test_enigma_jupyter_nb_case(self):
        enigma = Enigma()
        enigma.rotors.setup_rotors('I', 'II', 'III')
        enigma.rotors.rotor_3.set_position(26)
        enigma.reflector.setup('B')
        input = 'A'
        post_rotors = enigma.rotors.encode(input)
        post_reflector = enigma.reflector.encode(post_rotors)
        post_rotors_rev = enigma.rotors.encode(post_reflector, True)
        print(post_rotors_rev)



if __name__ == '__main__':
    unittest.main()
