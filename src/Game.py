import logging
import random
import sys
import time

from Dice import Dice
from DatabaseHandler import DatabaseHandler
from QuestionHandler import QuestionHandler

class Game():
    """
    Game class
    """
    def __init__(self):
        self.logger = logging.getLogger("Game")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.colors = [ 'red', 'white' ]
        self.init_game()
    def init_game(self):
        """
        Initialize the game
        """
        self.logger.info("Initializing Database")
        self.database = DatabaseHandler()
        self.questionHandler = QuestionHandler()
        self.dice = Dice(6)
        self.logger.info("Polishing Dice")
        self.logger.info("Starting Game - Welcome to trivial purfuit")
    def run(self):
        """
        Run loop for the game

        Raises:
            - sys.exit on keyboard interrupt
        """
        try:
            while(True):
                # simulate roll
                roll = self.dice.roll()
                self.logger.info("You rolled a {0}".format(roll))
                # simulate moving the piece
                self.logger.info("Moving your piece...")
                # simulate landing on a color
                color = random.choice(self.colors)
                self.logger.info("You landed on {0}".format(color))
                self.logger.debug("Selecting {0} question".format(color))
                # get a question from the color type
                question = self.database.select_color_question(color)
                # get an answer from the user
                answer = self.questionHandler.query_user(question)
                # evaluate the answer
                self.questionHandler.evaluate(question, answer)
                time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__": #pragma no cover
    game = Game()
    game.run()