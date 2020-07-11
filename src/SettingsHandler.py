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
                self.logger.info("How many human players are playing? Select 1-3")
                number_players = int(input())
                self.number_players = number_players
            except ValueError:
                    number_players = 0
        return number_players