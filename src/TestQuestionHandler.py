import unittest
from unittest.mock import patch, MagicMock
from QuestionHandler import QuestionHandler
from Human import Human
from Computer import Computer


class TestQuestionHandler(unittest.TestCase):
    @patch.object(Computer, 'answer_question', return_value=1)
    @patch('builtins.input', return_value=1)
    def test_query_user_computer(self, input, computer):
        testQuestion = {"question": "testQuestion",
                        "correct": "testCorrect", "incorrect": ["a", "b", "c"]}
        testPlayer = Computer("testName", "assets/shy.png", 50, 50, 40)
        handler = QuestionHandler()
        ret = handler.query_user(testQuestion, testPlayer)
        self.assertIn(ret, ["testCorrect", "a", "b", "c"])

    @patch('builtins.input', return_value=1)
    def test_query_user_human(self, input):
        testQuestion = {"question": "testQuestion",
                        "correct": "testCorrect", "incorrect": ["a", "b", "c"]}
        testPlayer = Human("testName", "assets/shy.png", 50, 50)
        handler = QuestionHandler()
        ret = handler.query_user(testQuestion, testPlayer)
        self.assertIn(ret, ["testCorrect", "a", "b", "c"])

    def test_evaluate(self):
        handler = QuestionHandler()
        handler.evaluate({"correct": "testCorrect"}, "testCorrect")
        handler.evaluate({"correct": "testCorrect"}, "testIncorrect")


if __name__ == '__main__':  # pragma no cover
    unittest.main()
