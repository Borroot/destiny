import logging
from pile import Pile


class Destiny:

    def __init__(self, decks=1, seed=None):
        self.pile1, self.pile2 = Pile(decks).shuffle(seed).split()


    def run(self):
        rounds = 0
        while not self.iswon():
            self.round([], [])
            rounds += 1
        return rounds


    def round(self, cards1, cards2):
        if len(self.pile1) == 0:
            self.pile1.pushall(cards1 + cards2)
            return

        if len(self.pile2) == 0:
            self.pile2.pushall(cards2 + cards1)
            return

        card1, card2 = self.pile1.pop(), self.pile2.pop()

        cards1.append(card1)
        cards2.append(card2)

        if card1 > card2:
            self.pile1.pushall(cards1 + cards2)
            return

        if card2 > card1:
            self.pile2.pushall(cards2 + cards1)
            return

        self.round(cards1, cards2)


    def iswon(self):
        return len(self.pile1) == 0 or len(self.pile2) == 0


    def __str__(self):
        return "%s\n\n%s" % (self.pile1, self.pile2)
