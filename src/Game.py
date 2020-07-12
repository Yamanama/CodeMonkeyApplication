import logging
import random
import sys
import time

from Board import Board
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
        self.board = Board()
        self.logger.info("Gathering Settings")
        human_player_number = self.settingsHandler.select_number_of_players()
        max_difficulty = self.settingsHandler.select_computer_difficulty_level()

        #create selected number of players
        self.players = [Human() for i in range(self.settingsHandler.number_players)] 

        #set player names
        for i in range(len(self.players)):
            self.players[i].set_name(i+1)

        # fill the rest of the players with computers
        for i in range(0, 4 - human_player_number):
            self.players.append(Computer(random.randint(0, max_difficulty)))
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
                for player in self.players:
                    #Human starts a game
                    self.logger.info(player.name + " rolls a dice!")
                    # simulate roll
                    roll = self.dice.roll()
                    self.logger.info(player.name + " rolled a {0}".format(roll))
                    # simulate moving the piece
                    self.logger.info("Moving the piece of " + player.name + "...")
                    # simulate landing on a color
                    color = self.board.location();
                    self.logger.info(player.name +  " landed on {0}".format(color))
                    self.logger.debug("Selecting {0} question".format(color))
                    # get a question from the color type
                    question = self.database.select_color_question(color)
                    # get an answer from the user
                    answer = self.questionHandler.query_user(question, player)
                    # evaluate the answer
                    self.questionHandler.evaluate(question, answer)
                    time.sleep(1)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__": #pragma no cover
    game = Game()
    game.run()