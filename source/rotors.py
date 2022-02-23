from string import ascii_uppercase


class Rotors:
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

    __rotor_i = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    __rotor_ii = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                  'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    __rotor_iii = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                   'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    __rotor_iv = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                  'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
    __rotor_v = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
    __rotor_i_turnover = 'R'
    __rotor_ii_turnover = 'F'
    __rotor_iii_turnover = 'W'
    __rotor_iv_turnover = 'K'
    __rotor_v_turnover = 'A'

    def __init__(self, name, position=1):
        if name.upper() not in ['I', 'II', 'III', 'IV', 'V']:
            raise NameError
        if position < 1 or position > 26:
            raise ValueError
        self.name = name
        self.position = position
        self.rotor = list()

        if self.name.upper() == 'I':
            self.rotor = Rotor.__rotor_i.copy()
            self.turnover = Rotor.__rotor_i_turnover
        elif self.name.upper() == 'II':
            self.rotor = Rotor.__rotor_ii.copy()
            self.turnover = Rotor.__rotor_ii_turnover
        elif self.name.upper() == 'III':
            self.rotor = Rotor.__rotor_iii.copy()
            self.turnover = Rotor.__rotor_iii_turnover
        elif self.name.upper() == 'IV':
            self.rotor = Rotor.__rotor_iv.copy()
            self.turnover = Rotor.__rotor_iv_turnover
        elif self.name.upper() == 'V':
            self.rotor = Rotor.__rotor_v.copy()
            self.turnover = Rotor.__rotor_v_turnover

    def __set_rotation(self, position):
        """Sets the rotation for this rotor.

        :param position: The intended position for this rotor relative to 'A' MOD 26.
        """



    def __rotate(self):
        """Rotates the rotor by one place.

        """

        self.__advance_position()
        self.rotor = (self.rotor[len(self.rotor) - 1:len(self.rotor)] + self.rotor[0:len(self.rotor) - 1])

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


    def encode(self, letter):
        if ord(letter) < 65 or ord(letter) > 90:
            raise ValueError
        self.__rotate()
        relative_letter_value = ord(letter) - ord('A')
        return self.rotor[relative_letter_value]




class RotorI(Rotor):
    """

    """

    __rotor_i = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
