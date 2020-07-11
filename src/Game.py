import logging
import random
import sys
import time

from Dice import Dice
from DatabaseHandler import DatabaseHandler
from QuestionHandler import QuestionHandler
from SettingsHandler import SettingsHandler
from Human import Human
from Computer import Computer

class Game():
    """
    Game class
    """
    def __init__(self):
        self.logger = logging.getLogger("Game")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.colors = [ 'red', 'white', 'blue', 'green']
        self.init_game()
    def init_game(self):
        """
        Initialize the game
        """
        self.logger.info("Initializing Database")
        self.database = DatabaseHandler()
        self.questionHandler = QuestionHandler()
        self.settingsHandler = SettingsHandler()
        self.settingsHandler.select_number_of_players()
        #create Computer instance (one computer always plays the game)
        self.computer = Computer()
        #create selected number of players
        self.players = [Human() for i in range(self.settingsHandler.number_players)] 
        #set player names
        for i in range(len(self.players)):
            self.players[i].set_name(i+1)
        #append computer player to the list of all players
        self.players.append(self.computer)

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
                for player in range(len(self.players)):
                    #Human starts a game
                    self.logger.info(self.players[player].name + " rolls a dice!")
                    # simulate roll
                    roll = self.dice.roll()
                    self.logger.info(self.players[player].name + " rolled a {0}".format(roll))
                    # simulate moving the piece
                    self.logger.info("Moving the piece of " + self.players[player].name + "...")
                    # simulate landing on a color
                    color = random.choice(self.colors)
                    self.logger.info(self.players[player].name +  " landed on {0}".format(color))
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