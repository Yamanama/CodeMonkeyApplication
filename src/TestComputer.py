import unittest
from unittest.mock import patch
from Computer import Computer


class TestComputer(unittest.TestCase):

    @patch("random.randint", return_value=100)
    def test_answer_question_correct(self, random):
        computer = Computer("test", "test", "test", "test", 40)
        answer = computer.answer_question({"correct": "testCorrect"}, [
                                          "testCorrect", "test", "3", "4"])
        self.assertEqual(answer, "testCorrect")

    @patch("random.randint", return_value=0)
    def test_answer_question_incorrect(self, random):
        computer = Computer("test", "test", "test", "test", 40)
        answer = computer.answer_question({"correct": "testCorrect"}, [
                                          "testCorrect", "test", "3", "4"])
        # self.assertIn(answer - 1, [0, 1, 2, 3])


if __name__ == '__main__':  # pragma no cover
    unittest.main()
