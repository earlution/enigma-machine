from abc import ABC, abstractmethod


# @TODO is this the correct name?
class Reflectors:
    """

    """

    def __init__(self, reflectors_factory=None):
        """reflector_factory is the abstract factory

        """

        self.reflector_factory = reflectors_factory

    def reflector_factory(self, name='A'):
        """Factory method to create a reflector of desired type.

        :param name: The name of the intended reflector
        :return: The specified reflector
        """

        reflectors = {'A': ReflectorA,
                      'B': ReflectorB,
                      'C':ReflectorC,
                      'B Thin': ReflectorBThin,
                      'C Thin': ReflectorCThin}

        if name not in reflectors:
            return reflectors['A']()
        else:
            return reflectors[name]()


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

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

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

    def __init__(self, name):
        super().__init__(name)

    '''
    def __init__(self):
        super.__init__()
        self._encodings = ReflectorA.__encodings
    '''


class ReflectorB(Reflector):
    """

    """

    __encodings = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O',
                   'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    def __init__(self):
        self._encodings = ReflectorB.__encodings


class ReflectorC(Reflector):
    """

    """

    __encodings = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X',
                   'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']

    def __init__(self):
        self._encodings = ReflectorC.__encodings


class ReflectorBThin(Reflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P',
                   'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S']

    def __init__(self):
        self._encodings = ReflectorBThin.__encodings


class ReflectorCThin(Reflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L',
                   'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q']

    def __init__(self):
        self._encodings = ReflectorCThin.__encodings


class ReflectorETW(Reflector):
    """An Enigma reflector.

    Date introduced:
    Model name and number: Enigma I
    """

    __encodings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self):
        self._encodings = ReflectorETW.__encodings


if __name__ == "__main__":
    reflector = ReflectorsFactory(ReflectorA)
    reflector.name()
