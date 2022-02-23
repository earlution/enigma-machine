from keyboard import Keyboard
from plugboard import *
from rotors import *


class Enigma:
    def __init__(self):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard()
        self.rotors = Rotors()

    def query_rotors(self):
        print(f'Rotor 1 is {self.rotors[1]}')
        print(f'Rotor 2 is {self.rotors[2]}')
        print(f'Rotor 2 is {self.rotors[3]}')

    def press_key(self, letter):
        try:
            letter.isalpha()
            letter_pb = self.plugboard.encode(letter)
            letter_rotors = self.rotors.encode(letter_pb)
            # functional placeholder in place of reflector system
            letter_enc = letter_rotors
            return letter_enc
        except:
            pass


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    enigma = Enigma()
    enigma.plugboard.patch('a', 'f')
    encoded_letter = enigma.keyboard.press('a')
    print(f'Enigma encoded letter: {encoded_letter}')

    '''
    letter_pb = enigma.plugboard.mappings[letter]
    letter_r1 = enigma.rotors[1].encode(letter_pb)
    letter_r2 = enigma.rotors[2].encode(letter_r1)
    letter_r3 = enigma.rotors[3].encode(letter_r2)
    print(f'Enigma encoded letter: {letter_r3}')
    '''
