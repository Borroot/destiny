import unittest
import context
from value import Value
from suit import Suit
from card import Card
from pile import Pile


class TestPile(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(Pile()), len(Value) * len(Suit))
        self.assertEqual(len(Pile([])), 0)
        self.assertEqual(len(Pile([Card(Value.TWO, Suit.SPADES)])), 1)


    def test_pop(self):
        with self.assertRaises(IndexError):
            Pile([]).pop()


if __name__ == "__main__":
    unittest.main()
