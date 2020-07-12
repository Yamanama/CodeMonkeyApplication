import unittest
from unittest.mock import patch
from Player import Player

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', return_value="testName")
    def test_set_name(self, input):
        player = Player()
        player.set_name(1)
        self.assertEqual(player.name, "testName")

if __name__ == '__main__': #pragma no cover
    unittest.main()