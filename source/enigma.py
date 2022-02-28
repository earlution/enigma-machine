from keyboard import *
from plugboard import *
from rotors import *
from reflector import *


def rotate_letter(letter, rotation):
    """Rotates [uppercase] characters around the alphabet.  Works in both directions.

    :param letter: The letter to be rotations.
    :param rotation: The number of positions to rotate.
    :return: The rotations letter.
    """

    # invalid input
    if len(letter) != 1:
        return letter
    # letter is not in alphabet
    elif not letter.isalpha():
        return letter
    else:
        letter = letter.upper()
        ordv = ord(letter)
        ans = ((ordv - 65 + rotation) % 26) + 65
        return chr(ans)


class Enigma:
    def __init__(self):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard()
        self.rotors = Rotors()
        self.reflector = None
        # @TODO should have one abstract factory that has responsibility to create 'families' of objects
        self.rot_af = RotorAbstractFactory()
        self.ref_af = ReflectorAbstractFactory()

    @staticmethod
    def enalpharate_position(position):
        """Helper function to map position value to its equivalent letter in alphabet.

        :param position: The position value to enalpharate.
        :return: The enalpharated position.
        """
        import string
        positions = list(range(1, 27))
        letters = list(string.ascii_uppercase)
        enalpharations = dict(zip(positions, letters))
        return enalpharations[position]

    @staticmethod
    def enumerate_letter(letter):
        """Helper function to map letter to its equivalent position in alphabet.

        :param letter: The position value to enumerate.
        :return: The enumerated position.
        """
        import string
        letter = letter.upper()
        letters = list(string.ascii_uppercase)
        positions = list(range(1, 27))
        enumerations = dict(zip(letters, positions))
        return enumerations[letter]

    def add_reflector(self, reflector_to_add: Reflector):
        """Adds a reflector to this Enigma machine.

        :param reflector_to_add: The reflector to use.
        :type reflector_to_add: Reflector
        """
        self.reflector = reflector_to_add

    def encode(self, letter):
        """The main encode letter use case, synonymous with pressing a key on the Enigma keyboard.

        :param letter: The letter to encode
        :return: The encoded letter.
        """

        plugboard_enc = self.plugboard.encode(letter)
        # @TODO rotations related code smell
        rotors_enc = self.rotors.encode(plugboard_enc)
        reflector_enc = self.reflector.encode(rotors_enc)
        rotors_rev_enc = self.rotors.encode(reflector_enc, True)
        letter_enc = rotors_rev_enc

        return letter_enc


if __name__ == "__main__":
    # case 1
    enigma = Enigma()

    # create the desired rotors
    enigma.rot_af.config_factory(RotorIV)
    r1 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorV)
    r2 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorBeta)
    r3 = enigma.rot_af.create_rotor()

    # configure the ring settings
    r1.set_ring_setting(14)
    r2.set_ring_setting(9)
    r3.set_ring_setting(24)

    # configure the initial rotor positions
    r1.set_position(Enigma.enumerate_letter('A'))
    r2.set_position(Enigma.enumerate_letter('A'))
    r3.set_position(Enigma.enumerate_letter('A'))

    # add configured rotors to rotors sub-system
    enigma.rotors.add_rotor_to_rotors(r1)
    enigma.rotors.add_rotor_to_rotors(r2)
    enigma.rotors.add_rotor_to_rotors(r3)

    # make and add the reflector
    enigma.ref_af.config_factory(ReflectorB)
    reflector = enigma.ref_af.create_reflector()
    enigma.add_reflector(reflector)

    # perform encryption
    case1 = enigma.encode('H')






