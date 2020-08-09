import unittest
from Dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.sides = 8
        self.dice = Dice(self.sides)

    def test_roll(self):
        for i in range(1000):
            self.assertLessEqual(self.dice.roll(), self.sides)

    def test_error(self):
        self.assertRaises(ValueError, Dice, 0)


if __name__ == '__main__':  # pragma no cover
    unittest.main()
