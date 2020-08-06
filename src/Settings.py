import pygame
from Scene import Scene
from Board import Board
from Player import Player
from Question import Question
class Settings(Scene):
    """
    Title scene. Entry point for the game
    """
    def __init__(self, players):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 32) 
        self.small_font = pygame.font.SysFont("Arial", 14)       
        self.title = self.font.render("Settings Menu", True, (0,128,0))
        self.action = self.small_font.render("Press <return> to start!", True, (0,128,0))
        self.width, self.height = pygame.display.get_surface().get_size()
        self.title_rect = self.title.get_rect(center=(self.width/2, 0 - self.title.get_height()/2))
        self.action_rect = self.action.get_rect(center=(self.width/2, self.height - self.action.get_height()))
        self.players = players
    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switch_scene(Board(self.width, self.height))
    def update(self):
        pass
    
    def render(self, screen):
        caption = "Trivial Purfuit - Independence Edition"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.action, self.action_rect)
    

