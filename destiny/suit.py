from enum import Enum, auto


class Suit(Enum):

    SPADES = auto()
    CLUBS = auto()
    HEARTS = auto()
    DIAMONDS = auto()


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.__str__()
