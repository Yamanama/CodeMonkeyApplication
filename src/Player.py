import logging
class Player():
    def __init__(self):
        self.name = ""
        self.square_hub = []
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s')

    def set_name(name, player_number):
        try:
            self.logger.info("What's the name of player " + player_number + "?")
            self.name = str(input())
        except ValueError:
            self.name = ""