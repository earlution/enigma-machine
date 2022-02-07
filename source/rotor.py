import string

class Rotor:
    """Implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].

    :param name:
    Name of the intended Enigma rotor, must be in ['I', 'II', 'III', 'IV', 'V'].
    """

    __rotor_i_chars = ('E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                       'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J')
    __rotor_ii_chars = ('A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                        'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E')
    __rotor_iii_chars = ('B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                         'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O')
    __rotor_iv_chars = ('E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                        'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B')
    __rotor_v_chars = ('V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                       'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K')

    def __init__(self, name, rotor_i_chars=None):
        if name.upper() not in ['I', 'II', 'III', 'IV', 'V']:
            raise NameError
        self.name = name
        self.rotor = dict()
        uppercase_letters_str = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_str)

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

    def encode(self, letter):
        """Encodes an inputted letter.

        Uses the specific Enigma rotor map to encode a letter.

        :param letter:
        The letter to encode.
        :return:
        The encoded letter
        """
        return self.rotor[letter.upper()]

