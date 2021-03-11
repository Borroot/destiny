import unittest
import context
from value import Value
from suit import Suit
from card import Card


class TestCard(unittest.TestCase):

    def test_equal_strict(self):
        self.assertEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.SPADES))

        self.assertEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.HEARTS))
        self.assertEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertNotEqual(Card(Value.TWO, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertNotEqual(Card(Value.SIX, Suit.SPADES), Card(Value.TWO, Suit.SPADES))


    def test_equal_loose(self):
        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertLessEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertLessEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.SPADES))

        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertLessEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.HEARTS))
        self.assertLessEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertGreaterEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.SPADES))

        self.assertGreaterEqual(Card(Value.TWO, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertGreaterEqual(Card(Value.SIX, Suit.SPADES), Card(Value.SIX, Suit.HEARTS))
        self.assertGreaterEqual(Card(Value.ACE, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

    def test_order_strict(self):
        self.assertLess(Card(Value.TWO, Suit.SPADES), Card(Value.THREE, Suit.SPADES))
        self.assertLess(Card(Value.TWO, Suit.SPADES), Card(Value.THREE, Suit.HEARTS))
        self.assertLess(Card(Value.TWO, Suit.SPADES), Card(Value.KING,  Suit.SPADES))
        self.assertLess(Card(Value.TWO, Suit.SPADES), Card(Value.KING,  Suit.HEARTS))

        self.assertLess(Card(Value.FIVE, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertLess(Card(Value.FIVE, Suit.SPADES), Card(Value.SIX, Suit.HEARTS))
        self.assertLess(Card(Value.FIVE, Suit.SPADES), Card(Value.ACE, Suit.SPADES))
        self.assertLess(Card(Value.FIVE, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertLess(Card(Value.ACE, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertLess(Card(Value.ACE, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertGreater(Card(Value.TWO, Suit.SPADES), Card(Value.ACE, Suit.SPADES))
        self.assertGreater(Card(Value.TWO, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertGreater(Card(Value.THREE, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertGreater(Card(Value.THREE, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertGreater(Card(Value.KING,  Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertGreater(Card(Value.KING,  Suit.SPADES), Card(Value.TWO, Suit.HEARTS))

        self.assertGreater(Card(Value.SIX, Suit.SPADES), Card(Value.FIVE, Suit.SPADES))
        self.assertGreater(Card(Value.SIX, Suit.SPADES), Card(Value.FIVE, Suit.HEARTS))
        self.assertGreater(Card(Value.ACE, Suit.SPADES), Card(Value.FIVE, Suit.SPADES))
        self.assertGreater(Card(Value.ACE, Suit.SPADES), Card(Value.FIVE, Suit.HEARTS))


    def test_order_loose(self):
        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.THREE, Suit.SPADES))
        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.THREE, Suit.HEARTS))
        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.KING,  Suit.SPADES))
        self.assertLessEqual(Card(Value.TWO, Suit.SPADES), Card(Value.KING,  Suit.HEARTS))

        self.assertLessEqual(Card(Value.FIVE, Suit.SPADES), Card(Value.SIX, Suit.SPADES))
        self.assertLessEqual(Card(Value.FIVE, Suit.SPADES), Card(Value.SIX, Suit.HEARTS))
        self.assertLessEqual(Card(Value.FIVE, Suit.SPADES), Card(Value.ACE, Suit.SPADES))
        self.assertLessEqual(Card(Value.FIVE, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertLessEqual(Card(Value.ACE, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertLessEqual(Card(Value.ACE, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertGreaterEqual(Card(Value.TWO, Suit.SPADES), Card(Value.ACE, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.TWO, Suit.SPADES), Card(Value.ACE, Suit.HEARTS))

        self.assertGreaterEqual(Card(Value.THREE, Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.THREE, Suit.SPADES), Card(Value.TWO, Suit.HEARTS))
        self.assertGreaterEqual(Card(Value.KING,  Suit.SPADES), Card(Value.TWO, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.KING,  Suit.SPADES), Card(Value.TWO, Suit.HEARTS))

        self.assertGreaterEqual(Card(Value.SIX, Suit.SPADES), Card(Value.FIVE, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.SIX, Suit.SPADES), Card(Value.FIVE, Suit.HEARTS))
        self.assertGreaterEqual(Card(Value.ACE, Suit.SPADES), Card(Value.FIVE, Suit.SPADES))
        self.assertGreaterEqual(Card(Value.ACE, Suit.SPADES), Card(Value.FIVE, Suit.HEARTS))


if __name__ == "__main__":
    unittest.main()
