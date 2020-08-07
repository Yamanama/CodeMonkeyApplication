import pygame
import logging
from Scene import Scene

class Settings(Scene):
    """
    Title scene. Entry point for the game
    """
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.font = pygame.font.SysFont("Arial", 32) 
        self.small_font = pygame.font.SysFont("Arial", 14)       
        self.title = self.font.render("Settings Menu", True, (0,128,0))
        self.input = self.font.render(str(""), True, (0, 128, 0))
        self.action = self.small_font.render("Press <return> to start!", True, (0,128,0))
        self.width, self.height = pygame.display.get_surface().get_size()
        self.title_rect = self.title.get_rect(center=(self.width/2, self.title.get_height()/2))
        self.input_rect = self.input.get_rect(center=(self.width/2, self.height/2))
        self.action_rect = self.action.get_rect(center=(self.width/2, self.height - self.action.get_height()))
        
        self.players = None
        self.active = 'human'
    def process_input(self, events):
        pass
    def update(self):
        pass
    
    def render(self, screen):
        pass
    
