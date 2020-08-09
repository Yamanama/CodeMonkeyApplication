import unittest
from unittest.mock import patch, MagicMock
from Game import Game
from Human import Human
from Computer import Computer


class TestGame(unittest.TestCase):
    @patch('builtins.input', return_value=1)
    def test_init(self, input):
        game = Game()


if __name__ == '__main__':  # pragma no cover
    unittest.main()
