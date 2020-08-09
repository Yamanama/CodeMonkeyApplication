import unittest
from unittest.mock import patch
from SettingsHandler import SettingsHandler


class TestSettingsHandler(unittest.TestCase):

    @patch("builtins.input", return_value=1)
    def test_select_number_of_players(self, input):
        handler = SettingsHandler()
        ret = handler.select_number_of_players()
        self.assertEqual(ret, 1)

    @patch("builtins.input", return_value=40)
    def test_select_computer_difficulty_level(self, input):
        handler = SettingsHandler()
        ret = handler.select_computer_difficulty_level()
        self.assertEqual(ret, 40)


if __name__ == '__main__':  # pragma no cover
    unittest.main()
