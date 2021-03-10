from enum import Enum, auto
import itertools
import random


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


class Suits(Enum):
    SPADES = auto()
    CLUBS = auto()
    HEARTS = auto()
    DIAMONDS = auto()


class Pile:

    def __init__(self, cards=None):
        if cards is None:
            self.cards = list(itertools.product(list(Value), list(Suits)))
        else:
            self.cards = cards


    def shuffle(self):
        random.shuffle(self.cards)


    def split(self):
        size = len(self.cards) // 2
        return Pile(self.cards[:size]), Pile(self.cards[size:])


    def pop(self):
        return self.cards.pop(0)


    def push(self, card):
        self.cards.append(card)


    def pushall(self, cards):
        for card in cards: self.push(card)


    def __getitem__(self, index):
        return self.cards[index]


    def __iter__(self):
        self._index = 0
        return self


    def __next__(self):
        if self._index < len(self.cards):
            card = self.cards[self._index]
            self._index += 1
            return card
        else:
            raise StopIteration


    def __str__(self):
        return "\n".join("%s\t%s" % (value, suit) for value, suit in self)


    def __repr__(self):
        return self.__str__()
