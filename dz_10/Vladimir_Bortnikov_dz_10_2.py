from enum import Enum
from abc import ABC, abstractmethod

class ClothType(Enum):
    """ type of Cloth """
    COAT = 0
    COSTUME = 1

class ACloth(ABC):
    """ Abstract class """
    __name: str
    __type: 'ClothType'

    def __init__(self, name: str, cloth_type: 'ClothType') -> None:
        self.__name = name
        self.__type = cloth_type

    @abstractmethod
    def calc_cloth(self) -> float:
        """ calc how mutch cloth need """

class Coat(ACloth):
    __size: float

    def __init__(self, name: str, size: float) -> None:
        super().__init__(name, ClothType.COAT)
        self.__size = size

    def calc_cloth(self) -> float:
        return self.__size / 6.5 + 0.5

class Costume(ACloth):
    __height: float

    def __init__(self, name: str, height) -> None:
        super().__init__(name, ClothType.COSTUME)
        self.__height = height

    def calc_cloth(self) -> float:
        return 3 * self.__height + 0.2