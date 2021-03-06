import pygame
import logging


class Player():
    """
    Player
    """

    def __init__(self, name, avatar="assets/laughing.png", offsetX=0, offsetY=0):
        self.name = name
        self.logger = logging.getLogger(self.name)
        logging.basicConfig(
            format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.avatar = avatar
        self.x = 400
        self.y = 400
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.pies = []

    def draw(self, screen):
        """
        Draw the player on the board
        """
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (50, 50))
        screen.blit(img, (self.x + self.offsetX, self.y + self.offsetY))

    def draw_statistics(self, screen, x, y):
        """
        Draw the statistics (The big head)
        """
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (150, 150))
        screen.blit(img, (x + 75, y))
        self.font = pygame.font.SysFont("Arial", 12)
        self.name_text = self.font.render(
            self.name, True, pygame.Color('white'))
        self.name_rect = self.name_text.get_rect(
            center=(x + 150, y + 175))
        screen.blit(self.name_text, self.name_rect)
        self.draw_pies(screen, x, y + 200)

    def draw_face(self, screen, x, y, width, height):
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x, y))

    def draw_pies(self, screen, x, y):
        """
        Draw the pies
        """
        x += 12.5
        for pie in self.pies:
            pygame.draw.rect(screen, pygame.Color(pie), (x, y, 50, 50))
            x += 75

    def add_pie(self, color):
        if color not in self.pies:
            self.logger.info("Getting a piece of cake!")
            self.pies.append(color)
