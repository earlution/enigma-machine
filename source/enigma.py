from keyboard import *
from plugboard import *
from reflector import *
from rotors import *


class Enigma:
    def __init__(self):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard()
        self.rotors = Rotors()
        self.reflector = Reflectors()


    def encode(self, letter):
        if letter.isalpha and (ord(letter.upper()) >= 65 and ord(letter.upper()) <= 90):
            letter = letter.upper()
            letter_pb = self.plugboard.encode(letter)
            letter_rotors = self.rotors.encode(letter_pb)
            letter_reflector = self.reflector.encode(letter_rotors)
            letter_rev_rotors = self.rotors.reverse_encode(letter_reflector)

            return letter_rev_rotors


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    enigma = Enigma()
    enigma.plugboard.add('a', 'f')
    encoded_letter = enigma.keyboard.press('a')
    print(f'Enigma encoded letter: {encoded_letter}')

    '''
    letter_pb = enigma.plugboard.mappings[letter]
    letter_r1 = enigma.rotors[1].encode(letter_pb)
    letter_r2 = enigma.rotors[2].encode(letter_r1)
    letter_r3 = enigma.rotors[3].encode(letter_r2)
    print(f'Enigma encoded letter: {letter_r3}')
    '''
