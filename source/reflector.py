from abc import ABC
from typing import Any


# @TODO is this the correct name?
class Reflectors:
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
        return enc

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

    __encodings: list[Any] = list()

    def __init__(self, name='A'):
        self._name = name

    def name(self):
        return self._name

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

    # have removed param name as workaround to issue described below
    def __init__(self):
        # @TODO trying to be polymorphic, figure out why I cannot call 'self._name = name' from super const.
        # super.__init__(name)
        super().__init__()
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


if __name__ == "__main__":
    pass
