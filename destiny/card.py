class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def __str__(self):
        return "%s %s" % (self.value, self.suit)


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        return NotImplemented


    def __ne__(self, other):
        if isinstance(other, Card):
            return self.value != other.value
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        return NotImplemented


    def __le__(self, other):
        if isinstance(other, Card):
            return self.value <= other.value
        return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        return NotImplemented


    def __ge__(self, other):
        if isinstance(other, Card):
            return self.value >= other.value
        return NotImplemented
