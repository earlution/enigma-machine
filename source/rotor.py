from string import ascii_uppercase


class Rotor_System:
    # @TODO imp. with *varargs
    def __init__(self, rotor_1_name=None, rotor_2_name=None, rotor_3_name=None):
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


class Rotor:
    """Implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].

    :param name:
    Name of the intended Enigma rotor, must be in ['I', 'II', 'III', 'IV', 'V'].
    """

    __rotor_i_chars = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                       'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
    __rotor_ii_chars = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                        'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
    __rotor_iii_chars = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                         'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    __rotor_iv_chars = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                        'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
    __rotor_v_chars = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                       'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
    __rotor_i_turnover = 'R'
    __rotor_ii_turnover = 'F'
    __rotor_iii_turnover = 'W'
    __rotor_iv_turnover = 'K'
    __rotor_v_turnover = 'A'


    def __init__(self, name):
        if name.upper() not in ['I', 'II', 'III', 'IV', 'V']:
            raise NameError
        self.name = name
        self.rotor = dict()
        self.__position = 'A'
        '''
        uppercase_letters_list = list(ascii_uppercase)
        rotor_iterator = zip(uppercase_letters_list, type(self).__rotor_i_chars)
        rotor_i_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, type(self).__rotor_ii_chars)
        rotor_ii_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, type(self).__rotor_iii_chars)
        rotor_iii_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, type(self).__rotor_iv_chars)
        rotor_iv_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, type(self).__rotor_v_chars)
        rotor_v_dict = dict(rotor_iterator)
        '''

        rotors = {'I': rotor_i_dict,
                  'II': rotor_ii_dict,
                  'III': rotor_iii_dict,
                  'IV': rotor_iv_dict,
                  'V': rotor_v_dict}

        if self.name.upper() == 'I':
            self.rotor = rotors['I']
        elif self.name.upper() == 'II':
            self.rotor = rotors['II']
        elif self.name.upper() == 'III':
            self.rotor = rotors['III']
        elif self.name.upper() == 'IV':
            self.rotor = rotors['IV']
        elif self.name.upper() == 'V':
            self.rotor = rotors['IV']

    def get_name(self):
        return self.name

    def get_position(self):
        return self.__position

    def set_position(self, letter):
        if letter.upper() not in list(ascii_uppercase):
            # @TODO error handling required here
            raise NameError
        else:
            self.__position = letter.upper()

    def encode(self, letter):
        """Encodes an inputted letter.

        Uses the specific Enigma rotor map to encode a letter.

        :param letter:
        The letter to encode.
        :return:
        The encoded letter
        """
        return self.rotor[letter.upper()]

