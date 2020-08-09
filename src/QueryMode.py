import pygame
import logging
import string
from Board import Board
from Settings import Settings


class QueryMode(Settings):
    """
    Query player names settings scene. 
    """

    def __init__(self, players):
        super().__init__()
        self.logger = logging.getLogger("Settings")
        logging.basicConfig(
            format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.players = players
        self.mode = "traditional"
        self.width, self.height = pygame.display.get_surface().get_size()
        self.logger.info("Querying for mode")

    def process_input(self, events):
        for event in events:
            self.handle_input(event)

    def update(self):
        pass

    def render(self, screen):
        caption = "Select Game Mode"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.action, self.action_rect)
        screen.blit(self.input, self.input_rect)
        self.query_user(screen)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                self.mode = "traditional"
            if event.key == pygame.K_r:
                self.mode = "rapid"
            if event.key == pygame.K_RETURN:
                self.logger.info("{0} mode selected".format(
                    self.mode.capitalize()))
                self.switch_scene(
                    Board(self.width, self.height, self.mode, self.players))

    def query_user(self, screen):
        self.title = self.font.render("Select Game Mode", True, (0, 128, 0))
        self.title_rect = self.title.get_rect(
            center=(self.width/2, self.title.get_height()/2))
        self.input = self.font.render(
            self.mode.capitalize(), True, (0, 128, 0))
        self.input_rect = self.input.get_rect(
            center=(self.width/2, self.height/2))
        self.action = self.small_font.render(
            "Press <R> for Rapid Mode or <T> for Traditional Mode", True, (0, 128, 0))
        self.action_rect = self.action.get_rect(
            center=(self.width/2, self.height - self.action.get_height()))
