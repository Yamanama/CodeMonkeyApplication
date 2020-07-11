import logging

class SettingsHandler():
    def __init__(self):
        self.number_players = 0
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s')

    def select_number_of_players(self):
        number_players = 0
        while number_players < 1 or 3 < number_players: 
            try:
                self.logger.info("How many human players are playing? Select 1-4")
                number_players = int(input())
                self.number_players = number_players
            except ValueError:
                number_players = 0
        return number_players
    
    def select_computer_difficulty_level(self):
        max_difficulty = 0
        while max_difficulty < 1 or 100 < max_difficulty:
            try:
                self.logger.info("What is the max difficulty for computer players? Select 0-100")
                max_difficulty = int(input())
            except ValueError:
                max_difficulty = 0
        return max_difficulty