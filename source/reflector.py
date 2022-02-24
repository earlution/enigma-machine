from abc import ABC, abstractmethod


# @TODO is this the correct name?
class ReflectorsFactory:
    """

    """

    __reflector_a = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C',
                     'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']
    __reflector_b = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O',
                     'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']
    __reflector_c = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X',
                     'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']
    __reflector_b_thin = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P',
                          'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S']
    __reflector_c_thin = ['R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L',
                          'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q']

    def __init__(self, reflector_factory=None):
        """reflector_factory is the abstract factory

        """

        self.reflector_factory = reflectors_factory

    def show_reflector(self):
        """ creates and shoes reflectors using the abstract factory

        """

        reflector = self.reflector_factory()

        print(f'We have a reflector{reflector}')
        print('it has the following encodings pattern: ')
        print(f'{reflector.encodings}')


class Reflector(ABC):
    """

    """

    __encodings = list()

    @property
    def encodings(self):
        return self._encodings

    '''
    @abstractmethod
    def encode(self, letter):
        pass
    '''
    def encode(self, letter):
        """Encodes a letter using the specific reflector schema in the subclass.

                :param letter: The letter to be encoded.
                :return: The encoded letter.
                """

        if ord(letter) < 65 or ord(letter) > 90:
            raise ValueError
        index_value = ord(letter) - ord('A')

        return self._encodings[index_value]


class ReflectorA(Reflector):
    """

    """

    __encodings = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C',
                   'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']

    def __init__(self):
        self._encodings = ReflectorA.__encodings

