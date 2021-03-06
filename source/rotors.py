from enigma import *
from enigma import Enigma


class Rotors:
    """

    """

    def __init__(self, ):
        self.rotors = list()
        self.num_of_rotors = 0

    def add_rotor_to_rotors(self, new_rotor):
        self.rotors.append(new_rotor)
        self.num_of_rotors += 1
        self.rotors[self.num_of_rotors - 1].set_rotor_number(self.num_of_rotors)

    def get_num_of_rotors(self):
        return self.num_of_rotors

    def get_rotor_name(self, rotor_number):
        # @TODO get name of encodings from intended list of Rotors, via param rotor_number
        pass

    def encode(self, letter, reverse=False):
        """Encodes an inputted letter.

        - Uses the specific Enigma encodings map to encode a letter.
        - Checks if turnover position has been reached, if so triggers rotation of next encodings.

        :param letter: The letter to encode.
        :param reverse: True for standard encoding (default), False for reverse encoding.
        :return: The encoded letter
        """

        letter = letter.upper()

        if not reverse:
            # rotate the right-most rotor
            self.rotors[2].rotate()

            # check for rotor 2 turnover
            r2_position_letter = Enigma.enalpharate_position(self.rotors[2].position)
            if r2_position_letter in self.rotors[2].turnover:
                self.rotors[1].rotate()

            # check for rotor 1 turnover
            r1_position_letter = Enigma.enalpharate_position(self.rotors[1].position)
            if r1_position_letter in self.rotors[1].turnover:
                self.rotors[0].rotate()

            # encode letter by rotor 3
            letter = self.rotors[2].encode(letter)
            print(f'Rotor {self.rotors[-1].rotor_number} ({self.rotors[2].__str__()}) encoded: {letter}')

            # adjust next input by rotation, relative to initial setting
            if self.rotors[2].position != 1:
                rotation = 27 - self.rotors[2].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[2].rotor_number} rotated, so input to next is: {letter}')

            # encode letter by rotor 2
            letter = self.rotors[1].encode(letter)
            print(f'Rotor {self.rotors[1].rotor_number} ({self.rotors[1].__str__()}) encoded: {letter}')

            # adjust next input by rotation, relative to initial setting
            if self.rotors[1].position != 1:
                rotation = 27 - self.rotors[1].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[1].rotor_number} rotated, so input to next is: {letter}')

            # encode letter by rotor 1
            letter = self.rotors[0].encode(letter)
            print(f'Rotor {self.rotors[0].rotor_number} ({self.rotors[0].__str__()}) encoded: {letter}')

            # adjust next input by rotation, relative to initial setting
            if self.rotors[0].position != 1:
                rotation = 27 - self.rotors[0].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[0].rotor_number} rotated, so input to next is: {letter}')


        else:
            # encode letter by rotor 1
            letter = self.rotors[0].encode(letter, True)
            print(f'Rotor {self.rotors[0].rotor_number} ({self.rotors[0].__str__()}) encoded: {letter}')

            if self.rotors[0].position != 1:
                rotation = 27 - self.rotors[0].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[0].rotor_number} rotated, so input to next is: {letter}')

            # encode letter by rotor 2
            letter = self.rotors[1].encode(letter, True)
            print(f'Rotor {self.rotors[1].rotor_number} ({self.rotors[1].__str__()}) encoded: {letter}')

            # adjust next input by rotation, relative to initial setting
            if self.rotors[1].position != 1:
                rotation = 27 - self.rotors[1].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[1].rotor_number} rotated, so input to next is: {letter}')

            # encode letter by rotor 3
            letter = self.rotors[2].encode(letter, True)
            print(f'Rotor {self.rotors[-1].rotor_number} ({self.rotors[2].__str__()}) encoded: {letter}')

            # adjust next input by rotation, relative to initial setting
            if self.rotors[2].position != 1:
                rotation = 27 - self.rotors[2].position
                letter = rotate_letter(letter, rotation)
                print(f'Rotor {self.rotors[2].rotor_number} rotated, so output is: {letter}')

        return letter

    @staticmethod
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


class Rotor:
    """Superclass implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].
    """

    def __init__(self, ring_setting=1, position=1):
        """Rotor superclass constructor.

        :param ring_setting: The intended ring setting.
        :param position: The initial rotor position.
        """

        # will be overridden in subclasses
        # self.name = None
        # @TODO this is not working, the individual rotors do not have correct name
        self.rotor_number = int()
        self.ring_setting = ring_setting
        self.position = position
        self.encodings = list()
        self.encodings_rev = list()
        # would be logically easier to implement as int not str, but more abstract from Enigma construction.
        # A solution to this problem, is to enumerate self.turnover when required.
        # However, approach adds an order of time complexity, per rotor, to the Rotors.encode() algorithm.'''

        self.input_offset = 0
        self.output_offset = 0

    def __str__(self):
        return self._name

    @staticmethod
    def get_reverse_encodings(encodings):
        """Helper function to generate the reverse encodings, as experienced by signal post-reflector.

        :param encodings: The standard encodings encodes from which to get the reverse encodings.
        :return: The reverse encodings.
        """

        import string
        import operator
        uc = list(string.ascii_uppercase)
        dict_to_swap = dict(zip(uc, encodings))
        rev_key_value = {value: key for (key, value) in dict_to_swap.items()}
        sorted_dict = dict(sorted(rev_key_value.items(), key=operator.itemgetter(0)))
        # get list of values
        dict_values = sorted_dict.values()
        reverse_encodings = list(dict_values)
        return reverse_encodings

    def set_rotor_number(self, rotor_num):
        """Sets the - from left to right - position in the rotor sub-system this rotor will occupy.

        I.e. From left to right, which position in the rotor system this rotor occupies.

        :param rotor_num: The position in the rotor sub-system.
        """

        self.rotor_number = rotor_num

    def rotate(self, positions=1):
        """Rotates the position of this rotor by param positions places.

        :param positions: The number of positions to rotate the position by - default is 1.
        """

        # edge case: invalid type, do not rotate
        if not isinstance(positions, int):
            pass
        # edge case: invalid value, do not rotate
        # elif positions < 1:
        #     pass
        else:
            self.encodings = self.encodings[positions:] + self.encodings[0:positions]
            self.encodings_rev = self.encodings_rev[positions:] + self.encodings_rev[0:positions]
            self.position = (self.position + positions) % 26

    def get_name(self):
        """Gets the name of this rotor.

        :return: The name of this rotor.
        :rtype: str
        """

        return self._name

    def get_position(self):
        """Gets the current position value of this rotor.

        :return: The current position of this rotor.
        :rtype: str
        """

        return self.position

    def set_position(self, position):
        """Sets the rotational position for this rotor.

        :param position: The intended position.
        """

        # edge case: invalid type, do nothing
        if not isinstance(position, int):
            pass
        # edge case: invalid value, do nothing
        elif position < 1 or position > 26:
            pass
        # edge case: position == 1, no need to rotate
        elif position == 1:
            self.position = position
        else:
            self.position = position
            self.encodings = self.encodings[position - 1:] + self.encodings[0:position - 1]
            self.encodings_rev = self.encodings_rev[position - 1:] + self.encodings_rev[0:position - 1]

    def get_ring_setting(self):
        """Gets the current ring position.

        :return: The current ring position.
        """

        return self.ring_setting

    def set_ring_setting(self, ring_setting):
        """Sets the ring position.

        :param ring_setting: The intended ring setting for this encodings relative to 'A' MOD 26.
        """

        self.ring_setting = ring_setting
        # ring_setting of 1 means no adjustment...
        if ring_setting == 1:
            pass
        else:
            # ...therefore the actual adjustment needs to be reduced by 1
            self.rotate(-ring_setting)
            print()

    def encode(self, letter, reverse=False):
        """Encodes a letter based upon this rotor's mappings.

        :param letter: The letter to be encoded.
        :param reverse: Perform a reverse encoding post-reflector.
        :return: The encoded letter.
        """

        letter = letter.upper()
        if ord(letter) < 65 or ord(letter) > 90:
            return ''
        else:
            if not reverse:
                relative_letter_value = ord(letter) - ord('A')
                return self.encodings[relative_letter_value]
            else:
                relative_letter_value = ord(letter) - ord('A')
                return self.encodings_rev[relative_letter_value]


class RotorI(Rotor):
    """Specialised Rotor; model I.

    """

    __encodings = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                   'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    __encodings_rev = ['U', 'W', 'Y', 'G', 'A', 'D', 'F', 'P', 'V', 'Z', 'B', 'E', 'C',
                       'K', 'M', 'T', 'H', 'X', 'S', 'L', 'R', 'I', 'N', 'Q', 'O', 'J']
    __turnover = ['R']

    def __init__(self):
        super().__init__()
        self._name = 'I'
        super().__str__()
        self.encodings = RotorI.__encodings.copy()
        self.encodings_rev = RotorI.__encodings_rev.copy()
        self.turnover = RotorI.__turnover


class RotorII(Rotor):
    """Specialised Rotor; model II.

    """

    __encodings = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                   'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    __encodings_rev = ['A', 'J', 'P', 'C', 'Z', 'W', 'R', 'L', 'F', 'B', 'D', 'K', 'O',
                       'T', 'Y', 'U', 'Q', 'G', 'E', 'N', 'H', 'X', 'M', 'I', 'V', 'S']
    __turnover = ['F']

    def __init__(self):
        super().__init__()
        self._name = 'II'
        super().__str__()
        self.encodings = RotorII.__encodings.copy()
        self.encodings_rev = RotorII.__encodings_rev.copy()
        self.turnover = RotorII.__turnover


class RotorIII(Rotor):
    """Specialised Rotor; model III.

    """

    __encodings = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                   'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    __encodings_rev = ['T', 'A', 'G', 'B', 'P', 'C', 'S', 'D', 'Q', 'E', 'U', 'F', 'V',
                       'N', 'Z', 'H', 'Y', 'I', 'X', 'J', 'W', 'L', 'R', 'K', 'O', 'M']
    __turnover = ['W']

    def __init__(self):
        super().__init__()
        self._name = 'III'
        super().__str__()
        self.encodings = RotorIII.__encodings.copy()
        self.encodings_rev = RotorIII.__encodings_rev.copy()
        self.turnover = RotorIII.__turnover


class RotorIV(Rotor):
    """Specialised Rotor; model IV.

    """

    __encodings = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                   'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
    __encodings_rev = ['H', 'Z', 'W', 'V', 'A', 'R', 'T', 'N', 'L', 'G', 'U', 'P', 'X',
                       'Q', 'C', 'E', 'J', 'M', 'B', 'S', 'K', 'D', 'Y', 'O', 'I', 'F']
    __turnover = ['K']

    def __init__(self):
        super().__init__()
        self._name = 'IV'
        super().__str__()
        self.encodings = RotorIV.__encodings.copy()
        self.encodings_rev = RotorIV.__encodings_rev.copy()
        self.turnover = RotorIV.__turnover


class RotorV(Rotor):
    """Specialised Rotor; model V.

    """

    __encodings = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                   'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
    __encodings_rev = ['Q', 'C', 'Y', 'L', 'X', 'W', 'E', 'N', 'F', 'T', 'Z', 'O', 'S',
                       'M', 'V', 'J', 'U', 'D', 'K', 'G', 'I', 'A', 'R', 'P', 'H', 'B']
    __turnover = ['A']

    def __init__(self):
        super().__init__()
        self._name = 'I'
        super().__str__()
        self.encodings = RotorV.__encodings.copy()
        self.encodings_rev = RotorV.__encodings_rev.copy()
        self.turnover = RotorV.__turnover


class RotorVI(Rotor):
    """Specialised Rotor; model VI.

    """

    __encodings = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N',
                   'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']
    __encodings_rev = ['S', 'K', 'X', 'Q', 'L', 'H', 'C', 'N', 'W', 'A', 'R', 'V', 'G',
                       'M', 'E', 'B', 'J', 'P', 'T', 'Y', 'F', 'D', 'Z', 'U', 'I', 'O']
    __turnover = ['A', 'N']

    def __init__(self):
        super().__init__()
        self._name = 'VI'
        super().__str__()
        self.encodings = RotorVI.__encodings.copy()
        self.encodings_rev = RotorVI.__encodings_rev.copy()
        self.turnover = RotorVI.__turnover


class RotorVII(Rotor):
    """Specialised Rotor; model VII.

    """

    __encodings = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B',
                   'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']
    __encodings_rev = ['Q', 'M', 'G', 'Y', 'V', 'P', 'E', 'D', 'R', 'C', 'W', 'T', 'I',
                       'A', 'N', 'U', 'X', 'F', 'K', 'Z', 'O', 'S', 'L', 'H', 'J', 'B']
    __turnover = ['A', 'N']

    def __init__(self):
        super().__init__()
        self._name = 'VII'
        super().__str__()
        self.encodings = RotorVII.__encodings.copy()
        self.encodings_rev = RotorVII.__encodings_rev.copy()
        self.turnover = RotorVII.__turnover


class RotorVIII(Rotor):
    """Specialised Rotor; model VIII.

    """

    __encodings = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P',
                   'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']
    __encodings_rev = ['Q', 'J', 'I', 'N', 'S', 'A', 'Y', 'D', 'V', 'K', 'B', 'F', 'R',
                       'U', 'H', 'M', 'C', 'P', 'L', 'E', 'W', 'Z', 'T', 'G', 'X', 'O']
    __turnover = ['A', 'N']

    def __init__(self):
        super().__init__()
        self._name = 'VIII'
        super().__str__()
        self.encodings = RotorVIII.__encodings.copy()
        self.encodings_rev = RotorVIII.__encodings_rev.copy()
        self.turnover = RotorVIII.__turnover


class RotorBeta(Rotor):
    """Specialised Rotor; model Beta.

    """

    __encodings = ['L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q',
                   'M', 'D', 'R', 'T', 'A', 'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S']
    __encodings_rev = ['R', 'L', 'F', 'O', 'B', 'V', 'U', 'X', 'H', 'D', 'S', 'A', 'N',
                       'G', 'Y', 'K', 'M', 'P', 'Z', 'Q', 'W', 'E', 'J', 'I', 'C', 'T']
    __turnover = []

    def __init__(self):
        super().__init__()
        self._name = 'Beta'
        super().__str__()
        self.encodings = RotorBeta.__encodings.copy()
        self.encodings_rev = RotorBeta.__encodings_rev.copy()
        self.turnover = RotorBeta.__turnover


class RotorGamma(Rotor):
    """Specialised Rotor; model Gamma.

    """

    __encodings = ['F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T',
                   'I', 'Y', 'C', 'W', 'L', 'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D']
    __encodings_rev = ['E', 'L', 'P', 'Z', 'H', 'A', 'X', 'J', 'N', 'Y', 'D', 'R', 'K',
                       'F', 'C', 'T', 'S', 'I', 'B', 'M', 'G', 'W', 'Q', 'V', 'O', 'U']
    __turnover = []

    def __init__(self):
        super().__init__()
        self._name = 'Gamma'
        super().__str__()
        self.encodings = RotorGamma.__encodings.copy()
        self.encodings_rev = RotorGamma.__encodings_rev.copy()
        self.turnover = RotorGamma.__turnover


class RotorAbstractFactory:
    """Rotor abstract factory - an implementation of the abstract factory design pattern.

    To enable dynamic creation of whatever flavor of Rotor, so that we can have Enigma machines with however many
    rotors.

    Abstract factory pattern implementation from:

    Chaudhary, M. 2021. Abstract Factory Method ??? Python Design Patterns [Online]. Uttar Pradesh: GeeksforGeeks.
     Available from: https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/
     [Accessed Wed 23 Feb 2022].
    """

    def __init__(self, rotors_factory=None):
        """rotors_factory is the abstract factory

        :param rotors_factory: The Rotor type with which to configure the factory.
        """

        self.rotor_factory = rotors_factory

    def config_factory(self, rotors_factory: Rotor):
        """To enable the factory to be configured to create various specialised Rotor

         - MIRRORS __init__ behaviour (but signature is different) - code smell?

        :param rotors_factory: The Rotor type with which to configure the factory.
        """

        self.rotor_factory = rotors_factory

    def create_rotor(self) -> Rotor:
        """Creates a specialised rotor (of type Rotor) polymorphically using the abstract factory.

        Flavour of Rotor is dependent on the current factory configuration.

        :return: The created Rotor.
        :rtype: Rotor
        """

        created_rotor = self.rotor_factory()
        return created_rotor


if __name__ == "__main__":
    # create the rotor abstract factory
    r_af = RotorAbstractFactory()
    # configure the abstract factory for specialised Rotor of type RotorI
    r_af.config_factory(RotorI)
    # create the desired Rotor subclass
    rotor = r_af.create_rotor()

    assert(rotor.encode('A') == 'E')
    assert (rotor.encode('A', True) == 'U')
