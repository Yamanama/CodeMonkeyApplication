from Player import Player
import logging

class Computer(Player):
   def __init__(self):
      super().__init__()
      self.name = "Computer"