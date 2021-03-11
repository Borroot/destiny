import itertools
import random
import logging
from value import Value
from suit import Suit
from card import Card


class Pile:

    def __init__(self, decks=1, cards=None):
        if cards is None:
            self.cards = list(map(lambda card: Card(card[0], card[1]), \
                    itertools.product(list(Value), list(Suit)))) * decks
        else:
            self.cards = cards


    def shuffle(self, seed=None):
        if seed is not None: random.seed(seed)
        random.shuffle(self.cards)
        return self


    def split(self):
        if len(self.cards) % 2 == 1: logging.warning("Pile could not be split equally in two.")
        size = len(self.cards) // 2
        return Pile(cards=self.cards[:size]), Pile(cards=self.cards[size:])


    def pop(self):
        return self.cards.pop(0)


    def push(self, card):
        self.cards.append(card)


    def pushall(self, cards):
        for card in cards: self.push(card)


    def __getitem__(self, index):
        return self.cards[index]


    def __len__(self):
        return len(self.cards)


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
        return "\n".join(str(card) for card in self)


    def __repr__(self):
        return self.__str__()
