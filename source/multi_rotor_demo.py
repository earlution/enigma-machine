from abc import ABC
from typing import Any
import string


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


class PlugLead:
    def __init__(self, patch):
        patch = patch.upper()
        self.mappings = dict()
        self.mappings = {patch[0]: patch[1], patch[1]: patch[0]}

    def encode(self, letter):
        if letter.upper() in self.mappings:
            return self.mappings[letter]
        else:
            return letter.upper()


class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = {k: v for k, v in zip(uppercase_letters_list, uppercase_letters_list)}
        self.patchings = dict()
        self.plugleads = list()
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0

    def add(self, pluglead: PlugLead):
        """Add one of ten available PlugLeads to the Plugboard.

        Patches two letters specified in the name parameter of the PlugLead.  E.g. the PlugLead argument 'AB' would
        patch the letters 'A' abd 'B', so that 'A' would be encoded to 'B' and 'B' would be encoded to 'A'.

        :param pluglead: A PlugLead object specifying the two letters for a bidirectional patch.
        :type pluglead: PlugLead
        """

        # edge case: attempt to make a patch that utilises an already patched letter
        for i in pluglead.mappings:
            for j in self.patchings:
                if i == j:
                    raise ValueError
        # edge case: attempt to add more than 10 PlugLeads
        if len(self.plugleads) == self.__max_num_of_plugleads:
            raise ValueError
        else:
            self.plugleads.append(pluglead)
            self.mappings.update(pluglead.mappings)
            self.patchings.update(pluglead.mappings)
            self.__num_of_plugleads += 1

    # @TODO imp. un_patch: delete from self.plugleads; reset self.mappings
    def un_patch(self, pluglead: PlugLead):
        if not isinstance(pluglead, PlugLead):
            pass
        elif pluglead not in self.plugleads:
            pass
        else:
            self.plugleads.remove(pluglead)

    def encode(self, letter):
        """Encodes param letter

        Encoding of the letter depends on the current state of the plugboard. I.e. what - if any - patches have beem
        made.

        :param letter: the letter to be encoded
        :return: the encoded letter
        """
        return self.mappings[letter]


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
        elif positions < 1:
            pass
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

    Chaudhary, M. 2021. Abstract Factory Method – Python Design Patterns [Online]. Uttar Pradesh: GeeksforGeeks.
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


class ReflectorSystem:
    """

    """

    # def __init__(self, reflectors_factory=None): # can't get factory pattern working... yet
    def __init__(self, reflector_name='A'):
        """reflector_factory is the abstract factory

        """

        ''' @FIXME can't get this working. for now use the [urgh] pattern adopted in Rotors
        self.reflector_factory = reflectors_factory
        '''
        self.reflector_name = None
        self.reflector_model = None

    def setup(self, reflector_name='A'):
        if type(reflector_name) == str:
            if reflector_name == 'A':
                self.reflector_name = 'A'
                self.reflector_model = ReflectorA()
            elif reflector_name == 'B':
                self.reflector_name = 'B'
                self.reflector_model = ReflectorB()

    def encode(self, letter):
        enc = self.reflector_model.encode(letter)
        print(f'Reflector {self.rotors[-1].__str__()} encoding: {letter}')  # for testing...
        return enc

    ''' part of an experiment to implement factory method design pattern
    def show_reflector(self):
        """ creates and shows reflectors using the abstract factory

        """

        reflector = self.reflector_factory()

        print(f'We have a reflector{reflector}')
        print('it has the following encodings pattern: ')
        print(f'{reflector.encodings}')
    '''


class Reflector(ABC):
    """

    """

    __encodings: list[Any] = list()

    def __init__(self):
        self._name = str
        self._encodings = None

    def __str__(self):
        return self._name

    def encode(self, letter):
        """Encodes a letter using the specific reflector schema in the subclass.

                :param letter: The letter to be encoded.
                :return: The encoded letter.
                """

        if ord(letter) < 65 or ord(letter) > 90:
            raise ValueError
        index_value = ord(letter) - ord('A')

        letter = self._encodings[index_value]
        print(f'Reflector {self.__str__()} encoding: {letter}')  # for testing...

        return letter


class ReflectorA(Reflector):
    """

    """

    __encodings = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C',
                   'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO trying to be polymorphic, figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)

        super().__init__()
        self._name = 'A'
        super().__str__()
        self._encodings = ReflectorA.__encodings.copy()


class ReflectorB(Reflector):
    """

    """

    __encodings = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O',
                   'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)

        super().__init__()
        self._name = 'B'
        super().__str__()
        self._encodings = ReflectorB.__encodings.copy()


class ReflectorC(Reflector):
    """

    """

    __encodings = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X',
                   'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)

        super().__init__()
        self._name = 'C'
        super().__str__()
        self._encodings = ReflectorC.__encodings.copy()


class ReflectorBThin(Reflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P',
                   'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)

        super().__init__()
        self._name = 'B Thin'
        super().__str__()
        self._encodings = ReflectorBThin.__encodings.copy()


class ReflectorCThin(Reflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L',
                   'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)

        super().__init__()
        self._name = 'C Thin'
        super().__str__()
        self._encodings = ReflectorCThin.__encodings.copy()


class ReflectorETW(Reflector):
    """An Enigma reflector.

    Date introduced:
    Model name and number: Enigma I
    """

    __encodings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)
        super().__init__()
        self._encodings = ReflectorETW.__encodings.copy()


def reflector_factory(name='A'):
    """Factory method to create a reflector of desired type.

    Attempt to implement factory method pattern.

    Intention is to enable creation of whichever reflector, from another object without having to directly create
    instance from class.

    :param name: The name of the intended reflector
    :return: The specified reflector
    """

    reflectors = {'A': ReflectorA,
                  'B': ReflectorB,
                  'C': ReflectorC,
                  'B Thin': ReflectorBThin,
                  'C Thin': ReflectorCThin}

    if name not in reflectors:
        return reflectors['A']()
    else:
        return reflectors[name]()


class ReflectorAbstractFactory:
    """Reflector abstract factory - an implementation of the abstract factory design pattern.

    To enable dynamic creation of whatever flavor of Reflector, so that we can have Enigma machines with however
    many reflectors.

    Abstract factory pattern implementation from:

    Chaudhary, M. 2021. Abstract Factory Method – Python Design Patterns [Online]. Uttar Pradesh: GeeksforGeeks.
     Available from: https://www.geeksforgeeks.org/abstract-factory-method-python-design-patterns/
     [Accessed Wed 23 Feb 2022].
    """

    def __init__(self, reflectors_factory=None):
        """reflectors_factory is the abstract factory

        :param reflectors_factory: The Reflector type with which to configure the factory.
        """

        self.reflector_factory = reflectors_factory

    def config_factory(self, reflectors_factory: Reflector):
        """To enable the factory to be configured to create various specialised Rotor

         - MIRRORS __init__ behaviour (but signature is different) - code smell?

        :param reflectors_factory: The Reflector type with which to configure the factory.
        """

        self.reflector_factory = reflectors_factory

    def create_reflector(self) -> Reflector:
        """Creates a specialised reflector (of type Reflector) polymorphically using the abstract factory.

        Flavour of Reflector is dependent on the current factory configuration.

        :return: The created Reflector.
        :rtype: Reflector
        """

        created_reflector = self.reflector_factory()
        return created_reflector


class Keyboard:
    def __init__(self):
        pass

    def press(self, letter=None):
        if type(letter) != str or (ord(letter.upper()) < 65 or (ord(letter.upper()) > 90)):
            letter = input('Type a letter: ').upper()[0]
            if type(letter) != str or (ord(letter.upper()) < 65 or (ord(letter.upper()) > 90)):
                return ''
        else:
            return letter.upper()


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
    enigma.rot_af.config_factory(RotorI)
    r1 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorII)
    r2 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorIII)
    r3 = enigma.rot_af.create_rotor()

    # configure the ring settings
    r1.set_ring_setting(1)
    r2.set_ring_setting(1)
    r3.set_ring_setting(2)

    # configure the initial rotor positions
    r1.set_position(Enigma.enumerate_letter('A'))
    r2.set_position(Enigma.enumerate_letter('A'))
    r3.set_position(Enigma.enumerate_letter('Z'))

    # add configured rotors to rotors sub-system
    enigma.rotors.add_rotor_to_rotors(r1)
    enigma.rotors.add_rotor_to_rotors(r2)
    enigma.rotors.add_rotor_to_rotors(r3)

    # make and add the reflector
    enigma.ref_af.config_factory(ReflectorB)
    reflector = enigma.ref_af.create_reflector()
    enigma.add_reflector(reflector)

    # perform encryption
    case1 = enigma.encode('A')

    # case 2
    enigma = Enigma()

    # create the desired rotors
    enigma.rot_af.config_factory(RotorI)
    r1 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorII)
    r2 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorIII)
    r3 = enigma.rot_af.create_rotor()

    # configure the ring settings
    r1.set_ring_setting(1)
    r2.set_ring_setting(1)
    r3.set_ring_setting(2)

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
    case2 = enigma.encode('A')

    # case 3
    enigma = Enigma()

    # create the desired rotors
    enigma.rot_af.config_factory(RotorI)
    r1 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorII)
    r2 = enigma.rot_af.create_rotor()
    enigma.rot_af.config_factory(RotorIII)
    r3 = enigma.rot_af.create_rotor()

    # configure the ring settings
    r1.set_ring_setting(1)
    r2.set_ring_setting(1)
    r3.set_ring_setting(2)

    # configure the initial rotor positions
    r1.set_position(Enigma.enumerate_letter('Q'))
    r2.set_position(Enigma.enumerate_letter('E'))
    r3.set_position(Enigma.enumerate_letter('V'))

    # add configured rotors to rotors sub-system
    enigma.rotors.add_rotor_to_rotors(r1)
    enigma.rotors.add_rotor_to_rotors(r2)
    enigma.rotors.add_rotor_to_rotors(r3)

    # make and add the reflector
    enigma.ref_af.config_factory(ReflectorB)
    reflector = enigma.ref_af.create_reflector()
    enigma.add_reflector(reflector)

    # perform encryption
    case3 = enigma.encode('A')

