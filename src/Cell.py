import pygame

class Cell():
    """
    Cells on the board
    """
    def __init__(self, color):
        self.color = color
        self.x = self.y = 0
    