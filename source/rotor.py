import string

class Rotor:
    """Implementation of the rotors used in the Enigma Machine.

    Technical specifications of the Enigma rotors from:

    Sale, T.E., 2000. Technical specification of the Enigma [Online]. The Late Tony Sale's Codes and Ciphers Website
     (https://www.codesandciphers.org.uk/index.htm). Available from:
     https://www.codesandciphers.org.uk/enigma/rotorspec.htm [06 February 2022].

    """
    def __init__(self, name):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        rotor_i_letters = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
                           'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
        rotor_ii_letters = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
                            'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
        rotor_iii_letters = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
                             'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
        rotor_iv_letters = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
                            'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
        rotor_v_letters = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
                           'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']

        rotor_iterator = zip(uppercase_letters_list, rotor_i_letters)
        rotor_i_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, rotor_ii_letters)
        rotor_ii_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, rotor_iii_letters)
        rotor_iii_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, rotor_iv_letters)
        rotor_iv_dict = dict(rotor_iterator)
        rotor_iterator = zip(uppercase_letters_list, rotor_v_letters)
        rotor_v_dict = dict(rotor_iterator)

        rotors = {'I': rotor_i_dict,
                  'II': rotor_ii_dict,
                  'III': rotor_iii_dict,
                  'IV': rotor_iv_dict,
                  'V': rotor_v_dict}


        if name.upper() == 'I':
            self.rotor = rotors['I']
        elif name.upper() == 'II':
            self.rotor = rotors['II']
        elif name.upper() == 'III':
            self.rotor = rotors['III']
        elif name.upper() == 'IV':
            self.rotor = rotors['IV']
        elif name.upper() == 'V':
            self.rotor = rotors['IV']
