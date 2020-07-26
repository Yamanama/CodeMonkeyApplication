from Player import Player
import random
import logging
import pygame
names = ["Harry","Ross", "Bruce","Cook", "Carolyn","Morgan","Albert","Walker",
         "Randy","Reed", "Larry","Barnes", "Lois","Wilson", "Jesse","Campbell",
         "Ernest","Rogers", "Theresa","Patterson", "Henry","Simmons", 
         "Michelle","Perry", "Frank","Butler", "Shirley" ]
class Computer(Player):
   """
   Computer player class

   Answers questions based on assigned difficulty level
   """
   def __init__(self, name, avatar, offsetX, offsetY, difficulty):
      super().__init__(name, avatar, offsetX, offsetY)
      self.name = random.choice(names) + "-Bot"
      self.difficulty = difficulty
   
   def answer_question(self, question, answers):
      """
      Answer the question based on random roll of correctness

      Returns: The selected question
      """
      chance_to_answer = random.randint(1, 100)
      if chance_to_answer >= self.difficulty:
         return question["correct"]
      else:
         return random.choice(answers)

   def move(self, board, width, height):
      up = self.x
      xPos = int(self.x/width)
      yPos = int(self.y/height)
      possibles = [
         [xPos - 1, yPos],
         [xPos + 1, yPos],
         [xPos, yPos - 1],
         [xPos, yPos + 1]
      ]
      positions = []
      for i in possibles:
         if self.check_cell(board,i[0], i[1]):
            positions.append([i[0]*width, i[1]*height])
      choice = random.choice(positions)
      self.x = choice[0]
      self.y = choice[1]
      pygame.time.wait(1000)
   
   def check_cell(self, board, xPos, yPos):
      if xPos < 0 or yPos < 0:
         return False
      if xPos > len(board)- 1 or yPos > len(board)-1:
         return False
      if board[xPos][yPos] is not None:
         return True
      else:
         return False