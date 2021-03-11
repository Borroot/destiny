import logging.config
import logging
from pile import Pile
from destiny import Destiny


def main():
    destiny = Destiny(decks=1, seed=None)
    print(destiny.run())


if __name__ == "__main__":
    main()
