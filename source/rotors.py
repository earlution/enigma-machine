import string


class Rotors:
    """

    """

    def __init__(self, ):
        self.rotors = list()
        self.num_of_rotors = 0
        # @TODO need to figure out a goo place for .rotations ...
        '''
        # values to track if a rotor has rotated, so that input value to next rotor can be adjusted accordingly
        self.rotations = [0 for _ in range(self.num_of_rotors)]
        '''
        self.rotations = list()

    def setup(self, *varargs):
        for rotor_class in varargs:
            if type(rotor_class) != Rotor:
                # @TODO what to do here if arg is invalid...
                pass
            else:
                raf = RotorAbstractFactory(rotor_class)
                # self.rotors.append(raf.create_rotor())
                return raf.create_rotor()

    # @TODO this is a temp helper method to get my head round the abstract factory process...
    def add_rotor_to_rotors(self, new_rotor):
        self.rotors.append(new_rotor)
        self.num_of_rotors += 1
        self.rotors[self.num_of_rotors - 1].set_rotor_number(self.num_of_rotors)

    def get_num_of_rotors(self):
        return self.num_of_rotors

    def get_rotor_name(self, rotor_number):
        # @TODO get name of _encodings from intended list of Rotors, via param rotor_number
        pass

    def encode(self, letter, rotations, reverse=False):
        """Encodes an inputted letter.

        - Uses the specific Enigma _encodings map to encode a letter.
        - Checks if turnover position has been reached, if so triggers rotation of next _encodings.

        :param letter: The letter to encode.
        :param reverse: True for standard encoding (default), False for reverse encoding.
        :return: The encoded letter
        """

        uc = list(string.ascii_uppercase)
        letter = letter.upper()
        rotor_indexes = self.num_of_rotors - 1
        curr_rotor_index = rotor_indexes
        self.rotations = rotations
        turnover = False

        if reverse:
            for rotor in self.rotors:
                letter = rotor.encode(letter, True)
                print(f'Reflected rotor {rotor.rotor_number} ({rotor.__str__()}) encoding: {letter}')  # for testing...

                # adjust next input if rotation just occurred
                # @TODO figure out why self.rotations values are all 0
                if self.rotations[curr_rotor_index] > 0:
                    letter = self.rotate_letter(letter, -self.rotations[curr_rotor_index])
                    print(f'Rotor {rotor.rotor_number} rotations, so input to next is: {letter}')  # for testing...

                # bookkeeping for this rotor
                curr_rotor_index -= 1
        else:
            # rotate the right-most rotor
            self.rotors[rotor_indexes].rotate()
            self.rotations[curr_rotor_index] += 1

            # encode letter by right-most rotor
            letter = self.rotors[curr_rotor_index].encode(letter)
            print(f'Rotor {self.rotors[-1].rotor_number} ({self.rotors[-1].__str__()}) encoding: {letter}')  # for testing...

            # check if turnover position reached
            if letter == self.rotors[rotor_indexes].turnover:
                turnover = True

            # adjust next input for rotation relative to initial setting
            if self.rotations[curr_rotor_index] > 0:
                letter = self.rotate_letter(letter, -self.rotations[curr_rotor_index])
                print(f'Rotor {self.rotors[-1].rotor_number} rotations, so input to next is: {letter}')  # for testing...

            curr_rotor_index -= 1

            ''' previous approach to turnover rotation, left to demonstrate enumeration knowledge
            for rotor in reversed(self.rotors[:-1]):
                # enumerating rotor.turnover str, so can be compared with rotor.position int
                if rotor.position == [i for i, letter in enumerate(uc, 1) if letter == rotor.turnover][0]:
                    rotor.rotate()
            '''
            for rotor in reversed(self.rotors[:curr_rotor_index + 1]):
                if turnover:
                    self.rotors[curr_rotor_index].rotate
                letter = rotor.encode(letter)
                print(f'Rotor {rotor.rotor_number} ({rotor.__str__()}) encoding: {letter}')  # for testing...

                # adjust next input by any rotation occurred
                if self.rotations[curr_rotor_index] > 0:
                    letter = self.rotate_letter(letter, -self.rotations[curr_rotor_index])
                    print(f'Rotor {rotor.rotor_number} rotations so input to next should be: {letter}')  # for testing...

        return letter, rotations

    def rotate_letter(self, letter, rotation):
        """Rotates [uppercase] characters around the alphabet.  Works in both directions.

        :param letter: The letter to be rotations.
        :param rotation: The number of positions to rotate.
        :return: The rotations letter.
        """

        # invalid input
        if len(letter) != 1:
            return -1
        # letter is not in alphabet
        elif letter.isalpha() == False:
            return letter
        else:
            letter = letter.upper()
            new = ord(letter) + rotation
            # makes sure the value does not overflow.
            if new > ord('Z'):
                new = new - ord('Z') + ord('A') - 1
            elif new < ord('A'):
                new = new + ord('Z') - ord('A') + 1
            return chr(new)


class Rotor:
    """Superclass implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].
    """

    # @TODO delete this - when confident
    ''' hopefully we won't need this AWFUL mess!
    # @TODO write tests for reversed _encodings encodings
    __rotor_i = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    __rotor_i_rev = ['U', 'W', 'Y', 'G', 'A', 'D', 'F', 'P', 'V', 'Z', 'B', 'E', 'C',
                     'K', 'M', 'T', 'H', 'X', 'S', 'L', 'R', 'I', 'N', 'Q', 'O', 'J']
    __rotor_ii = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                  'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    __rotor_ii_rev = ['A', 'J', 'P', 'C', 'Z', 'W', 'R', 'L', 'F', 'B', 'D', 'K', 'O',
                      'T', 'Y', 'U', 'Q', 'G', 'E', 'N', 'H', 'X', 'M', 'I', 'V', 'S']
    __rotor_iii = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                   'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    __rotor_iii_rev = ['T', 'A', 'G', 'B', 'P', 'C', 'S', 'D', 'Q', 'E', 'U', 'F', 'V',
                       'N', 'Z', 'H', 'Y', 'I', 'X', 'J', 'W', 'L', 'R', 'K', 'O', 'M']
    __rotor_iv = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                  'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
    __rotor_iv_rev = ['H', 'Z', 'W', 'V', 'A', 'R', 'T', 'N', 'L', 'G', 'U', 'P', 'X',
                      'Q', 'C', 'E', 'J', 'M', 'B', 'S', 'K', 'D', 'Y', 'O', 'I', 'F']
    __rotor_v = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
    __rotor_v_rev = ['Q', 'C', 'Y', 'L', 'X', 'W', 'E', 'N', 'F', 'T', 'Z', 'O', 'S',
                     'M', 'V', 'J', 'U', 'D', 'K', 'G', 'I', 'A', 'R', 'P', 'H', 'B']
    __rotor_vi = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N',
                  'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']
    __rotor_vi_rev = ['S', 'K', 'X', 'Q', 'L', 'H', 'C', 'N', 'W', 'A', 'R', 'V', 'G',
                      'M', 'E', 'B', 'J', 'P', 'T', 'Y', 'F', 'D', 'Z', 'U', 'I', 'O']
    __rotor_vii = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B',
                   'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']
    __rotor_vii_rev = ['Q', 'M', 'G', 'Y', 'V', 'P', 'E', 'D', 'R', 'C', 'W', 'T', 'I',
                       'A', 'N', 'U', 'X', 'F', 'K', 'Z', 'O', 'S', 'L', 'H', 'J', 'B']
    __rotor_viii = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P',
                    'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']
    __rotor_viii_rev = ['Q', 'J', 'I', 'N', 'S', 'A', 'Y', 'D', 'V', 'K', 'B', 'F', 'R',
                        'U', 'H', 'M', 'C', 'P', 'L', 'E', 'W', 'Z', 'T', 'G', 'X', 'O']
    __rotor_i_turnover = ['R']
    __rotor_ii_turnover = ['F']
    __rotor_iii_turnover = ['W']
    __rotor_iv_turnover = ['K']
    __rotor_v_turnover = ['A']
    __rotor_vi_turnover = ['A', 'N']
    __rotor_vii_turnover = ['A', 'N']
    __rotor_viii_turnover = ['A', 'N']
    '''

    def __init__(self, ring_setting=1, position=1):
        """Rotor superclass constructor.

        :param ring_setting: The intended ring setting.
        :param position: The initial rotor position.
        """

        # @TODO delete this - when confident
        '''
        # if invalid, default to 'I'
        if name.upper() not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']:
            name = 'I'
        # if invalid, default to 1
        if (ring_setting < 1 or ring_setting > 26) or (not isinstance(ring_setting, int)):
            ring_position = 1
        self.name = name
        '''
        # will be overridden in subclasses
        # self.name = None
        self.rotor_number = int()
        self.ring_setting = ring_setting
        self.position = position
        self.rotation = 0
        self._encodings = list()
        self._encodings_rev = list()
        # would be logically easier to implement as int not str, but more abstract from Enigma construction.
        # A solution to this problem, is to enumerate self.turnover when required.
        # However, approach adds an order of time complexity, per rotor, to the Rotors.encode() algorithm.'''
        self.turnover = str

        # @TODO delete this - when confident
        ''' if this works then w00t!!!
        # @TODO this is HORRIFIC! need to create indiv. Rotor subclasses polymorphiclly
        if self.name.upper() == 'I':
            self._encodings = Rotor.__rotor_i.copy()
            self._encodings_rev = Rotor.__rotor_i_rev.copy()
            self.turnover = Rotor.__rotor_i_turnover.copy()
        elif self.name.upper() == 'II':
            self._encodings = Rotor.__rotor_ii.copy()
            self._encodings_rev = Rotor.__rotor_ii_rev.copy()
            self.turnover = Rotor.__rotor_ii_turnover.copy()
        elif self.name.upper() == 'III':
            self._encodings = Rotor.__rotor_iii.copy()
            self._encodings_rev = Rotor.__rotor_iii_rev.copy()
            self.turnover = Rotor.__rotor_iii_turnover.copy()
        elif self.name.upper() == 'IV':
            self._encodings = Rotor.__rotor_iv.copy()
            self._encodings_rev = Rotor.__rotor_iv_rev.copy()
            self.turnover = Rotor.__rotor_iv_turnover.copy()
        elif self.name.upper() == 'V':
            self._encodings = Rotor.__rotor_v.copy()
            self._encodings_rev = Rotor.__rotor_v_rev.copy()
            self.turnover = Rotor.__rotor_v_turnover.copy()
        elif self.name.upper() == 'VI':
            self._encodings = Rotor.__rotor_vi.copy()
            self._encodings_rev = Rotor.__rotor_vi_rev.copy()
            self.turnover = Rotor.__rotor_vi_turnover.copy()
        elif self.name.upper() == 'VII':
            self._encodings = Rotor.__rotor_vii.copy()
            self._encodings_rev = Rotor.__rotor_vii_rev.copy()
            self.turnover = Rotor.__rotor_vii_turnover.copy()
        elif self.name.upper() == 'VIII':
            self._encodings = Rotor.__rotor_viii.copy()
            self._encodings_rev = Rotor.__rotor_viii_rev.copy()
            self.turnover = Rotor.__rotor_viii_turnover.copy()
        '''

    def __str__(self):
        return self._name

    @staticmethod
    def get_reverse_encodings(encodings):
        """Helper function to generate the reverse _encodings encodings, as experienced by signal post-reflector.

        :param encodings: The standard _encodings encodes from which to get the reverse encodings.
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

    def __advance_position(self):
        """Increments the position value of this rotor by 1, until position is 26.  After which the value cycles back
        round to 1.

        """

        self.position += 1
        self.position = self.position % 26

    def set_rotor_number(self, rotor_num):
        """Sets the - from left to right - position in the rotor sub-system this rotor will occupy.

        I.e. From left to right, which position in the rotor system this rotor occupies.

        :param rotor_num: The position in the rotor sub-system.
        """

        self.rotor_number = rotor_num

    def rotate(self, positions=1):
        """Rotates the _encodings by param positions places.

        :param positions: The number of positions to rotate the _encodings by - default is 1.
        """

        if not isinstance(positions, int):
            positions = 1
        elif positions < 1 or positions > 26:
            positions = 1

        self.__advance_position()
        ''' this imp. goes the wong way - i.e. backwards
        self._encodings = (self._encodings[len(self._encodings) - 1:len(self._encodings)] 
                           + self._encodings[0:len(self._encodings) - 1])
        '''
        self._encodings = self._encodings[positions:] + self._encodings[0:positions]

    def get_name(self):
        """Gets the name of this _encodings.

        :return: The name of this _encodings.
        :rtype: str
        """

        return self._name

    def get_position(self):
        """Gets the current position value of this _encodings.

        :return: The current position of this _encodings.
        :rtype: str
        """

        return self.position

    def set_position(self, position):
        """Sets the position for this _encodings.

        :param position: The intended position.
        """

        if position < 1 or position > 26:
            pass
        else:
            self.position = position
            self._encodings = self._encodings[position - 1:] + self._encodings[0:position - 1]

    def get_ring_setting(self):
        """Gets the current ring position.

        :return: The current ring position.
        """

        return self.ring_setting

    def set_ring_position(self, ring_setting):
        """Sets the ring position.

        :param ring_setting: The intended ring setting for this _encodings relative to 'A' MOD 26.
        """

        self.rotate(ring_setting)

    def encode(self, letter, reverse=False):
        letter = letter.upper()
        if ord(letter) < 65 or ord(letter) > 90:
            return ''
        else:
            if not reverse:
                self.__advance_position()
                relative_letter_value = ord(letter) - ord('A')

                return self._encodings[relative_letter_value]
            else:
                relative_letter_value = ord(letter) - ord('A')

                return self._encodings_rev[relative_letter_value]


class RotorI(Rotor):
    """Specialised Rotor; _encodings I.

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
        self._encodings = RotorI.__encodings.copy()
        self._encodings_rev = RotorI.__encodings_rev.copy()
        self.turnover = RotorI.__turnover


class RotorII(Rotor):
    """Specialised Rotor; _encodings II.

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
        self._encodings = RotorII.__encodings.copy()
        self._encodings_rev = RotorII.__encodings_rev.copy()
        self.turnover = RotorII.__turnover


class RotorIII(Rotor):
    """Specialised Rotor; _encodings III.

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
        self._encodings = RotorIII.__encodings.copy()
        self._encodings_rev = RotorIII.__encodings_rev.copy()
        self.turnover = RotorIII.__turnover


class RotorIV(Rotor):
    """Specialised Rotor; _encodings IV.

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
        self._encodings = RotorIV.__encodings.copy()
        self._encodings_rev = RotorIV.__encodings_rev.copy()
        self.turnover = RotorIV.__turnover


class RotorV(Rotor):
    """Specialised Rotor; _encodings V.

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
        self._encodings = RotorV.__encodings.copy()
        self._encodings_rev = RotorV.__encodings_rev.copy()
        self.turnover = RotorV.__turnover


class RotorVI(Rotor):
    """Specialised Rotor; _encodings VI.

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
        self._encodings = RotorVI.__encodings.copy()
        self._encodings_rev = RotorVI.__encodings_rev.copy()
        self.turnover = RotorVI.__turnover


class RotorVII(Rotor):
    """Specialised Rotor; _encodings VII.

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
        self._encodings = RotorVII.__encodings.copy()
        self._encodings_rev = RotorVII.__encodings_rev.copy()
        self.turnover = RotorVII.__turnover


class RotorVIII(Rotor):
    """Specialised Rotor; _encodings VIII.

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
        self._encodings = RotorVIII.__encodings.copy()
        self._encodings_rev = RotorVIII.__encodings_rev.copy()
        self.turnover = RotorVIII.__turnover


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
        """"rotors_factory is the abstract factory

        :param rotors_factory:
        """

        self.rotor_factory = rotors_factory

    def config_factory(self, rotors_factory: Rotor):
        """To enable the factory to be configured to create various specialised Rotor

         - MIRRORS __init__ behaviour - code smell?

        :param rotors_factory: The Rotor type with which to configure the factory.
        """

        self.rotor_factory = rotors_factory

    def create_rotor(self) -> Rotor:
        """Creates a rotor using abstract factory.

        Flavour of Rotor is dependent on the current factory configuration.

        :return: The created Rotor.
        :rtype: Rotor
        """

        created_rotor = self.rotor_factory()
        return created_rotor


if __name__ == "__main__":
    pass
