import unittest
from unittest.mock import patch, mock_open
from DatabaseHandler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    @patch('csv.reader', return_value=['Approximately, how many hotdogs do Americans consume while celebrating Independence Day?', '150 million', '160 million, 100 million, 200 million', 'green'])
    def test_populate_database_from_file(self, mock_reader):
        with patch('builtins.open', mock_open(read_data="a,b,\"c, d, e\",blue")) as mock_file:
            handler = DatabaseHandler()
            handler.populate_database_from_file("somefile")
            self.assertGreater(len(handler.data), 0)

    @patch('csv.reader', return_value="a,")
    def test_populate_database_from_file_error(self, mock_reader):
        with patch('builtins.open', mock_open(read_data="a,b,\"c, d, e\",blue")) as mock_file:
            handler = DatabaseHandler()
            handler.populate_database_from_file("somefile")

    @patch('random.choice', return_value="something")
    def test_select_color_question(self, random):
        with patch('builtins.open', mock_open(read_data="a,b,\"c, d, e\",blue")) as mock_file:
            handler = DatabaseHandler()
            self.assertEqual(handler.select_color_question('red'), "something")
            self.assertEqual(
                handler.select_color_question('blue'), "something")
            self.assertEqual(
                handler.select_color_question('green'), "something")
            self.assertEqual(
                handler.select_color_question('white'), "something")


if __name__ == '__main__':  # pragma no cover
    unittest.main()
