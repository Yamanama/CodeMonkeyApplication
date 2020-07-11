import logging
class Player():
    """
    Player class
    """
    def __init__(self):
        self.name = ""
        self.number = 0
        self.square_hub = []
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s')

    def set_name(self, player_number):
        """
        Set name of the player
        """
        try:
            self.logger.info("What's the name of player " + str(player_number) + "?")
            self.name = str(input())
        except ValueError:
            self.name = ""