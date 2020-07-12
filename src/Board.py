import random

class Board():
    def __init__(self):
        self.colors = [ 'red', 'white', 'blue', 'green']
    def location(self):
        return random.choice(self.colors)