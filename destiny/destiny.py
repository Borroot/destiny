from pile import Pile


class Destiny:

    def __init__(self):
        self.pile1, self.pile2 = Pile().shuffle().split()


    def __str__(self):
        return "%s\n\n%s" % (self.pile1, self.pile2)
