class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def __str__(self):
        return "%s\t%s" % (self.value, self.suit)


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        return NotImplemented


    def __ne__(self, other):
        if isinstance(other, Card):
            return self.value != other.value or self.suit != other.suit
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        return NotImplemented


    def __le__(self, other):
        if isinstance(other, Card):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        return NotImplemented


    def __ge__(self, other):
        if isinstance(other, Card):
            return self.__gt__(other) or self.__eq__(other)
        return NotImplemented
