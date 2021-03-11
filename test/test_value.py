import unittest
import context
from value import Value


class TestValue(unittest.TestCase):

    def test_equal_strict(self):
        self.assertEqual(Value.TWO, Value.TWO)
        self.assertEqual(Value.SIX, Value.SIX)
        self.assertEqual(Value.ACE, Value.ACE)

        self.assertNotEqual(Value.TWO, 0)
        self.assertNotEqual(Value.TWO, 1)
        self.assertNotEqual(Value.TWO, 2)

        self.assertNotEqual(Value.TWO, Value.SIX)
        self.assertNotEqual(Value.TWO, Value.ACE)


    def test_equal_loose(self):
        self.assertLessEqual(Value.TWO, Value.TWO)
        self.assertLessEqual(Value.ACE, Value.ACE)
        self.assertLessEqual(Value.SIX, Value.SIX)

        self.assertGreaterEqual(Value.TWO, Value.TWO)
        self.assertGreaterEqual(Value.ACE, Value.ACE)
        self.assertGreaterEqual(Value.SIX, Value.SIX)


    def test_order_strict(self):
        self.assertLess(Value.TWO, Value.THREE)
        self.assertLess(Value.TWO, Value.KING)

        self.assertLess(Value.FIVE, Value.SIX)
        self.assertLess(Value.FIVE, Value.ACE)

        self.assertLess(Value.ACE, Value.TWO)
        self.assertGreater(Value.TWO, Value.ACE)

        self.assertGreater(Value.THREE, Value.TWO)
        self.assertGreater(Value.KING,  Value.TWO)

        self.assertGreater(Value.SIX, Value.FIVE)
        self.assertGreater(Value.ACE, Value.FIVE)


    def test_order_loose(self):
        self.assertLessEqual(Value.TWO, Value.THREE)
        self.assertLessEqual(Value.TWO, Value.KING)

        self.assertLessEqual(Value.FIVE, Value.SIX)
        self.assertLessEqual(Value.FIVE, Value.ACE)

        self.assertLessEqual(Value.ACE, Value.TWO)
        self.assertGreaterEqual(Value.TWO, Value.ACE)

        self.assertGreaterEqual(Value.THREE, Value.TWO)
        self.assertGreaterEqual(Value.KING,  Value.TWO)

        self.assertGreaterEqual(Value.SIX, Value.FIVE)
        self.assertGreaterEqual(Value.ACE, Value.FIVE)


if __name__ == "__main__":
    unittest.main()
