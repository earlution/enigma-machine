from abc import ABC, abstractmethod

'''
The docstring notes regarding the abstract factory pattern are from: 
https://refactoring.guru/design-patterns/abstract-factory/python/example
'''

class AbstractReflectorFactory(ABC):
    """

    The Abstract Factory interface declares a set of methods that return different abstract products. These products
    are called a family and are related by a high-level theme or concept. Products of one family are usually able to
    collaborate among themselves. A family of products may have several variants, but the products of one variant are
    incompatible with products of another.
    """

    @abstractmethod
    def create_reflector(self) -> AbstractReflector:
        pass


class ConcreteReflectorFactory(AbstractReflectorFactory):
    """

    Concrete Factories produce a family of products that belong to a single variant. The factory guarantees that
    resulting products are compatible. Note that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_reflector_a(self):
        """

        """

        pass

    def create_reflector_b(self):
        """

        """

        pass

    def create_reflector_c(self):
        """

        """

        pass


class AbstractReflector(ABC):
    """

    Each distinct product of a product family should have a base interface. All variants of the product must implement
    this interface.
    """

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def encodings(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def encode(self) -> str:
        raise NotImplementedError


class ConcreteReflector(AbstractReflector):
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

    def encode(self, letter):
        """Encodes a letter using the specific reflector schema in the subclass.

        :param letter: The letter to be encoded.
        :return: The encoded letter.
        """

        if ord(letter) < 65 or ord(letter) > 90:
            raise ValueError
        index_value = ord(letter) - ord('A')

        return self._encodings[index_value]


class ReflectorA(ConcreteReflector):
    """

    """

    __encodings = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C',
                   'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorA.__encodings


class ReflectorB(ConcreteReflector):
    """

    """

    __encodings = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O',
                   'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorB.__encodings


class ReflectorC(ConcreteReflector):
    """

    """

    __encodings = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X',
                   'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorC.__encodings


class ReflectorBThin(ConcreteReflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P',
                   'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorBThin.__encodings


class ReflectorCThin(ConcreteReflector):
    """An Enigma reflector.

    Date introduced: 1940
    Model name and number: M4 R1 (M3 + Thin)
    """

    __encodings = ['R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L',
                   'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorCThin.__encodings


class ReflectorETW(ConcreteReflector):
    """An Enigma reflector.

    Date introduced:
    Model name and number: Enigma I
    """

    __encodings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, name):
        super().__init__(name)
        self._encodings = ReflectorETW.__encodings


if __name__ == "__main__":
    reflector = ReflectorsFactory(ReflectorA)
    reflector.name()
