import logging.config
import logging
from pile import Pile
from destiny import Destiny


def main():
    results = []
    games = 1000

    for _ in range(games):
        destiny = Destiny(decks=1, seed=None)
        results.append(destiny.run())

    print("Average %s; Minimum %s; Maximum %s;"
            % (sum(results) // games, min(results), max(results)))


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    main()
