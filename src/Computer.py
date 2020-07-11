from Player import Player
import random
import logging
names = ["Harry","Ross", "Bruce","Cook", "Carolyn","Morgan","Albert","Walker",
         "Randy","Reed", "Larry","Barnes", "Lois","Wilson", "Jesse","Campbell",
         "Ernest","Rogers", "Theresa","Patterson", "Henry","Simmons", 
         "Michelle","Perry", "Frank","Butler", "Shirley" ]
class Computer(Player):
   """
   Computer player class

   Answers questions based on assigned difficulty level
   """
   def __init__(self, difficulty):
      super().__init__()
      self.name = random.choice(names) + "-Bot"
      self.difficulty = difficulty
   
   def answer_question(self, question, answers):
      """
      Answer the question based on random roll of correctness

      Returns: The selected question
      """
      chance_to_answer = random.randint(1, 100)
      if chance_to_answer >= self.difficulty:
         return answers.index(question["correct"]) + 1
      else:
         return random.randint(1 , 4)
