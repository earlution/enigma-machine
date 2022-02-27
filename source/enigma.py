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

        self.raf = RotorAbstractFactory()


    def encode(self, letter):
        # @TODO we need a better place for this
        num_of_rotors = 0

        self.raf.config_factory(RotorI)
        r1 = self.raf.create_rotor()
        self.raf.config_factory(RotorII)
        r2 = self.raf.create_rotor()
        self.raf.config_factory(RotorIII)
        r3 = self.raf.create_rotor()
        self.rotors.add_rotor_to_rotors(r1)
        num_of_rotors += 1
        self.rotors.add_rotor_to_rotors(r2)
        num_of_rotors += 1
        self.rotors.add_rotor_to_rotors(r3)
        num_of_rotors += 1
        self.reflector = ReflectorB()

        rotations = [0 for _ in range(num_of_rotors)]

        plugboard_enc = self.plugboard.encode(letter)
        rotors_enc, rotations = self.rotors.encode(plugboard_enc, rotations)
        reflector_enc = self.reflector.encode(rotors_enc)
        rotors_rev_enc = self.rotors.encode(reflector_enc, True)
        letter_enc = rotors_rev_enc

        return letter_enc


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    enigma = Enigma()
    enigma.encode('A')



