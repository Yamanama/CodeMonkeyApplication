import unittest
from Human import Human


class TestHuman(unittest.TestCase):
    def test_human(self):
        human = Human()
        self.assertTrue(type(human) is Human)


if __name__ == '__main__':  # pragma no cover
    unittest.main()
