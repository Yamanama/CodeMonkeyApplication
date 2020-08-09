from Player import Player
import random
import logging
import pygame
names = ["Harry", "Ross", "Bruce", "Cook", "Carolyn", "Morgan", "Albert", "Walker",
         "Randy", "Reed", "Larry", "Barnes", "Lois", "Wilson", "Jesse", "Campbell",
         "Ernest", "Rogers", "Theresa", "Patterson", "Henry", "Simmons",
         "Michelle", "Perry", "Frank", "Butler", "Shirley"]


class Computer(Player):
    """
    Computer player class

    Answers questions based on assigned difficulty level
    """

    def __init__(self, name, avatar, offsetX, offsetY, difficulty):
        super().__init__(name, avatar, offsetX, offsetY)
        self.name = random.choice(names) + "-Bot"
        self.difficulty = difficulty
        self.last_direction = None

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

    def move(self, board, width, height, mode):
        xPos = int(self.x/width)
        yPos = int(self.y/height)
        possibles = self.build_possibles(
            board, xPos, yPos, width, height, mode)
        choice = random.choice(possibles)
        self.last_direction = self.determine_direction(choice)
        self.x = choice[0]
        self.y = choice[1]
        pygame.time.wait(1000)

    def check_cell(self, board, xPos, yPos):
        if xPos < 0 or yPos < 0:
            return False
        if xPos > len(board) - 1 or yPos > len(board)-1:
            return False
        if board[xPos][yPos] is not None:
            return True
        else:
            return False

    def build_possibles(self, board, xPos, yPos, width, height, mode):
        possibles = []
        if mode == 'traditional':
            if self.last_direction != "north" and self.check_cell(board, xPos, yPos - 1):
                possibles.append([xPos*width, (yPos - 1)*height])
            if self.last_direction != "south" and self.check_cell(board, xPos, yPos + 1):
                possibles.append([xPos*width, (yPos + 1)*height])
            if self.last_direction != "west" and self.check_cell(board, xPos + 1, yPos):
                possibles.append([(xPos + 1)*width, yPos*height])
            if self.last_direction != "east" and self.check_cell(board, xPos - 1, yPos):
                possibles.append([(xPos - 1)*width, yPos*height])
        else:
            if self.check_cell(board, xPos, yPos - 1):
                possibles.append([xPos*width, (yPos - 1)*height])
            if self.check_cell(board, xPos, yPos + 1):
                possibles.append([xPos*width, (yPos + 1)*height])
            if self.check_cell(board, xPos + 1, yPos):
                possibles.append([(xPos + 1)*width, yPos*height])
            if self.check_cell(board, xPos - 1, yPos):
                possibles.append([(xPos - 1)*width, yPos*height])
        return possibles

    def determine_direction(self, choice):
        if choice[0] < self.x:
            return "west"
        if choice[0] > self.x:
            return "east"
        if choice[1] < self.y:
            return "south"
        if choice[1] > self.y:
            return "north"
