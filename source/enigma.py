from keyboard import Keyboard
from plugboard import *
from rotor import Rotor


class Enigma:
    def __init__(self):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard()
        self.__rotor_1_name = input('Which rotor do you want in position 1 (I, II, III, IV, or V): ')
        self.__rotor_2_name = input('Which rotor do you want in position 2 (I, II, III, IV, or V): ')
        self.__rotor_3_name = input('Which rotor do you want in position 3 (I, II, III, IV, or V): ')
        self.__rotor_1 = Rotor(self.__rotor_1_name)
        self.__rotor_2 = Rotor(self.__rotor_2_name)
        self.__rotor_3 = Rotor(self.__rotor_3_name)
        self.rotors = dict()
        self.rotors[1] = self.__rotor_1
        self.rotors[2] = self.__rotor_2
        self.rotors[3] = self.__rotor_3

    def query_rotors(self):
        print(f'Rotor 1 is {self.rotors[1]}')
        print(f'Rotor 2 is {self.rotors[2]}')
        print(f'Rotor 2 is {self.rotors[3]}')


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    enigma = Enigma()
    enigma.plugboard.patch('a', 'f')
    letter = enigma.keyboard.press()
    letter_pb = enigma.plugboard.mappings[letter]
    letter_r1 = enigma.rotors[1].encode(letter_pb)
    letter_r2 = enigma.rotors[2].encode(letter_r1)
    letter_r3 = enigma.rotors[3].encode(letter_r2)
    print(f'Enigma encoded letter: {letter_r3}')
