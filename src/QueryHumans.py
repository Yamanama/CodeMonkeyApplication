import pygame
import logging
from Settings import Settings
from QueryNames import QueryNames
class QueryHumans(Settings):
    """
    Title scene. Entry point for the game
    """
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("Settings")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.logger.info("Querying Number of humans")
        self.number_of_players = ""
    
    def process_input(self, events):
        for event in events:
            self.handle_human_players_input(event)
    
    def update(self):
        pass
    
    def render(self, screen):
        caption = "Choose Human Players"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.action, self.action_rect)
        screen.blit(self.input, self.input_rect)
        self.query_human_players(screen)
    def handle_human_players_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            self.logger.info("One human player selected")
            self.number_of_players = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            self.logger.info("Two human players selected")
            self.number_of_players = 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            self.logger.info("Three human player selected")
            self.number_of_players = 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            self.logger.info("Four human player selected")
            self.number_of_players = 4
        if self.number_of_players != "":
            self.switch_scene(QueryNames(self.number_of_players))
    def query_human_players(self, screen):
        self.title = self.font.render("How Many Human Players? Enter 1-4", True, (0,128,0))
        self.title_rect = self.title.get_rect(center=(self.width/2, self.title.get_height()/2))
        self.input = self.font.render(str(self.number_of_players), True, (0, 128, 0))
        self.input_rect = self.input.get_rect(center=(self.width/2, self.height/2))
