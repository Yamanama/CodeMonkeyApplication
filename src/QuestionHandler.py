
import random
import logging
from Human import Human


class QuestionHandler():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            format='%(asctime)s - %(name)s: %(levelname)s - %(message)s')

    def query_user(self, question, player):
        """
        query the user

        Keyword Args:
          question - the question to pose the user

        Return - the selection from the user
        """
        self.logger.info(question["question"])
        answers = []
        answers.append(question['correct'])
        answers += question['incorrect']
        # mix the answers
        random.shuffle(answers)
        # print the mixed answers
        for index, answer in enumerate(answers):
            self.logger.info("\t{0}: {1}".format(str(index+1), answer.strip()))
        selection = 0
        if(type(player) is Human):
            # get a valid selection from the user
            while selection < 1 or 4 < selection:
                try:
                    self.logger.info("Select an answer(1-4): ")
                    selection = int(input())
                except ValueError:  # pragma: no cover
                    selection = 0
        else:
            selection = player.answer_question(question, answers)
        return answers[selection - 1]

    def evaluate(self, question, answer):
        """
        Evaluate the user answer

        Keyword Args:
          question - the question
          answer - the user selected answer
        """
        if(answer == question['correct']):
            self.logger.info("You selected correctly!")
        else:
            self.logger.info("You were incorrect")
