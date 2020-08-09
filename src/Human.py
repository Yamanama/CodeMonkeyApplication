import logging
from Player import Player


class Human(Player):
    """
    Human Player class
    """

    def __init__(self, name, avatar, offsetX, offsetY):
        super().__init__(name, avatar, offsetX, offsetY)
