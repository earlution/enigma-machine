class Rotors:
    """

    """
    # @TODO imp. with *varargs
    def __init__(self, rotor_1_name='I', rotor_2_name="II", rotor_3_name="III"):
        if type(rotor_1_name) == str and type(rotor_2_name) == str and type(rotor_3_name) == str:
            self.rotor_1 = Rotor(rotor_1_name)
            self.rotor_1_name = rotor_1_name
            self.rotor_2 = Rotor(rotor_2_name)
            self.rotor_2_name = rotor_2_name
            self.rotor_3 = Rotor(rotor_3_name)
            self.rotor_3_name = rotor_3_name
            # @ bad design, what if we want a 4 or 5 rotor Enigma?
        else:
            # @TODO this is temporary
            self.rotor_1_name = input('Which rotor do you want in position 1 (I, II, III, IV, or V): ')
            self.rotor_1 = Rotor(self.rotor_1_name)
            self.rotor_2_name = input('Which rotor do you want in position 2 (I, II, III, IV, or V): ')
            self.rotor_2 = Rotor(self.rotor_2_name)
            self.rotor_3_name = input('Which rotor do you want in position 3 (I, II, III, IV, or V): ')
            self.rotor_2 = Rotor(self.rotor_2_name)

    def encode(self, letter):
        """Encodes an inputted letter.

        - Uses the specific Enigma rotor map to encode a letter.
        - Checks if turnover position has been reached, if so triggers rotation of next rotor.

        :param letter: The letter to encode.
        :return: The encoded letter
        """

        letter = letter.upper()
        self.rotor_3.rotate()
        if self.rotor_3.position == self.rotor_3.turnover:
            self.rotor_2.rotate()
            if self.rotor_2.position == self.rotor_2.turnover:
                self.rotor_1.rotate()
        letter = self.rotor_3.encode(letter)
        letter = self.rotor_2.encode(letter)
        letter = self.rotor_1.encode(letter)

        return letter

    def reverse_encode(self, letter):
        letter = letter.upper()
        letter = self.rotor_1.encode(letter)

    def turnover(self):
        raise NotImplementedError


class Rotor:
    """Implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].

    :param name:
    Name of the intended Enigma rotor, must be in ['I', 'II', 'III', 'IV', 'V'].
    """

    # @TODO write tests for reversed rotor encodings
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


    def __init__(self, name, position=1):
        # if invalid, default to 'I'
        if name.upper() not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']:
            name = 'I'
        # if invalid, default to 1
        if (position < 1 or position > 26) or (not isinstance(position, int)):
            position = 1
        self.name = name
        self.position = position
        self.rotor = list()
        self.rotor_rev = list()

        # @TODO this is HORRIFIC! need to create indiv. Rotor subclasses polymorphiclly
        if self.name.upper() == 'I':
            self.rotor = Rotor.__rotor_i.copy()
            self.rotor_rev = Rotor.__rotor_i_rev.copy()
            self.turnover = Rotor.__rotor_i_turnover.copy()
        elif self.name.upper() == 'II':
            self.rotor = Rotor.__rotor_ii.copy()
            self.rotor_rev = Rotor.__rotor_ii_rev.copy()
            self.turnover = Rotor.__rotor_ii_turnover.copy()
        elif self.name.upper() == 'III':
            self.rotor = Rotor.__rotor_iii.copy()
            self.rotor_rev = Rotor.__rotor_iii_rev.copy()
            self.turnover = Rotor.__rotor_iii_turnover.copy()
        elif self.name.upper() == 'IV':
            self.rotor = Rotor.__rotor_iv.copy()
            self.rotor_rev = Rotor.__rotor_iv_rev.copy()
            self.turnover = Rotor.__rotor_iv_turnover.copy()
        elif self.name.upper() == 'V':
            self.rotor = Rotor.__rotor_v.copy()
            self.rotor_rev = Rotor.__rotor_v_rev.copy()
            self.turnover = Rotor.__rotor_v_turnover.copy()
        elif self.name.upper() == 'VI':
            self.rotor = Rotor.__rotor_vi.copy()
            self.rotor_rev = Rotor.__rotor_vi_rev.copy()
            self.turnover = Rotor.__rotor_vi_turnover.copy()
        elif self.name.upper() == 'VII':
            self.rotor = Rotor.__rotor_vii.copy()
            self.rotor_rev = Rotor.__rotor_vii_rev.copy()
            self.turnover = Rotor.__rotor_vii_turnover.copy()
        elif self.name.upper() == 'VIII':
            self.rotor = Rotor.__rotor_viii.copy()
            self.rotor_rev = Rotor.__rotor_viii_rev.copy()
            self.turnover = Rotor.__rotor_viii_turnover.copy()


    def get_rev_encodings(self, std_encodings):
        import string
        import operator
        uc = list(string.ascii_uppercase)
        dict_to_swap = dict(zip(uc, std_encodings))
        rev_key_value = {value: key for (key, value) in dict_to_swap.items()}
        sorted_dict = dict(sorted(rev_key_value.items(), key=operator.itemgetter(0)))
        # get list of values
        dict_values = sorted_dict.values()
        rev_encodings = list(dict_values)
        return rev_encodings


    def __set_rotation(self, position):
        """Sets the rotation for this rotor.

        :param position: The intended position for this rotor relative to 'A' MOD 26.
        """

        raise NotImplementedError


    def __rotate(self):
        """Rotates the rotor by one place.

        """

        self.__advance_position()
        ''' pretty sure this imp. goes the wong way - i.e. backwards
        self.rotor = (self.rotor[len(self.rotor) - 1:len(self.rotor)] + self.rotor[0:len(self.rotor) - 1])
        '''
        self.rotor = self.rotor[1:] + self.rotor[0:1]


    def __advance_position(self):
        """Increments the position value of this rotor by 1, until position is 26.  After which the value cycles back
        round to 1.

        """

        self.position += 1
        self.position = self.position % 26


    def get_name(self):
        """Gets the name of this rotor.

        :return: The name of this rotor.
        :rtype: str
        """

        return self.name


    def get_position(self):
        """Gets the current position value of this rotor.

        :return: The position of this rotor.
        :rtype: str
        """

        return self.position


    def set_position(self, position):
        """Sets the position value for this rotor.

        :param position: The intended position.
        :raises ValueError: If param position is less than 1 or is greater than 26.
        """

        if position < 1 or position > 26:
            raise ValueError
        else:
            self.position = position


    def encode(self, letter, reverse=False):
        letter = letter.upper()
        if ord(letter) < 65 or ord(letter) > 90:
            return ''
        else:
            if not reverse:
                self.__rotate()
                relative_letter_value = ord(letter) - ord('A')

                return self.rotor[relative_letter_value]
            else:
                relative_letter_value = ord(letter) - ord('A')

                return self.rotor_rev[relative_letter_value]


    def rotate(self):
        pass


class RotorI(Rotor):
    """

    """

    __rotor_i = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']


if __name__ == "__main__":
    rotor = Rotor('VIII')
    std_encodings = rotor.rotor
    rev_encodings = rotor.get_rev_encodings(std_encodings)
    print(rev_encodings)