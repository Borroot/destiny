from enum import Enum, auto


class Value(Enum):

    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if isinstance(other, Value):
            return self.value == other.value
        return NotImplemented


    def __ne__(self, other):
        if isinstance(other, Value):
            return self.value != other.value
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Value):
            if self.value == Value.TWO.value and other.value == Value.ACE.value:
                return False
            if self.value == Value.ACE.value and other.value == Value.TWO.value:
                return True
            return self.value < other.value
        return NotImplemented


    def __le__(self, other):
        if isinstance(other, Value):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Value):
            return not self.__le__(other)
        return NotImplemented


    def __ge__(self, other):
        if isinstance(other, Value):
            return self.__gt__(other) or self.__eq__(other)
        return NotImplemented
