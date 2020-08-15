import unittest
from Human import Human


class TestHuman(unittest.TestCase):
    def test_human(self):
        human = Human("testName", "assets/shy.png", 50, 50)
        self.assertTrue(type(human) is Human)


if __name__ == '__main__':  # pragma no cover
    unittest.main()
