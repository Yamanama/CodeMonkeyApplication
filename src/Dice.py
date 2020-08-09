import random
import pygame


class Dice:
    """
    Dice class for rolling in the game
    Keyword arguments:
        sides -- the number of sides on the dice
    Raises: 
        Value Error - Sides must be > 1
    """

    def __init__(self, sides=6):
        if(sides <= 1):
            raise ValueError("Dice must have sides")
        self.sides = sides
        self.current = None

    def roll(self):
        """
        Roll the dice

        Returns:
            A random number between 1 and the number of sides on the dice
        """
        self.current = random.randint(1, self.sides)
        return self.current

    def draw(self, screen):
        if self.current is None:
            return
        if self.current == 1:
            img = pygame.image.load('assets/dice_one.png')
        if self.current == 2:
            img = pygame.image.load('assets/dice_two.png')
        if self.current == 3:
            img = pygame.image.load('assets/dice_three.png')
        if self.current == 4:
            img = pygame.image.load('assets/dice_four.png')
        if self.current == 5:
            img = pygame.image.load('assets/dice_five.png')
        if self.current == 6:
            img = pygame.image.load('assets/dice_six.png')
        img = pygame.transform.scale(img, (150, 150))
        screen.blit(img, (0, 0))
