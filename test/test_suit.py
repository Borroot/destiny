import unittest
import context
from suit import Suit


class TestSuit(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Suit.SPADES, Suit.SPADES)
        self.assertEqual(Suit.HEARTS, Suit.HEARTS)

        self.assertNotEqual(Suit.SPADES, 0)
        self.assertNotEqual(Suit.SPADES, 1)
        self.assertNotEqual(Suit.SPADES, 2)

        self.assertNotEqual(Suit.SPADES, Suit.CLUBS)
        self.assertNotEqual(Suit.HEARTS, Suit.DIAMONDS)


    def test_order(self):
        with self.assertRaises(TypeError):
            self.assertLess(Suit.SPADES, Suit.HEARTS)

        with self.assertRaises(TypeError):
            self.assertLess(Suit.SPADES, Suit.SPADES)

        with self.assertRaises(TypeError):
            self.assertLessEqual(Suit.SPADES, Suit.HEARTS)

        with self.assertRaises(TypeError):
            self.assertLessEqual(Suit.SPADES, Suit.SPADES)


if __name__ == "__main__":
    unittest.main()
