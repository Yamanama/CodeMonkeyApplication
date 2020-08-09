import unittest
from Board import Board


class TestBoard(unittest.TestCase):

    def test_location(self):
        board = Board()
        color = board.location()
        self.assertIn(color, board.colors)


if __name__ == '__main__':  # pragma no cover
    unittest.main()
