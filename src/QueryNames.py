import pygame
import logging
import string
from Human import Human
from Computer import Computer
from QueryMode import QueryMode
from Settings import Settings

class QueryNames(Settings):
    """
    Query player names settings scene. 
    """
    def __init__(self, player_number):
        super().__init__()
        self.logger = logging.getLogger("Settings")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.logger.info("Querying for player names")
        self.player_number = player_number
        self.players = []
        self.offsets = [
            (0, 0),
            (0, 50),
            (50, 0),
            (50, 50)
        ]
        self.avatars = [
            "assets/laughing.png",
            "assets/neutral.png",
            "assets/shy.png",
            "assets/smile.png",
            ]
        self.current_number = 1
        self.name = ""
    def process_input(self, events):
        for event in events:
            self.handle_human_players_input(event)
    
    def update(self):
        pass
    
    def render(self, screen):
        caption = "Player {0}".format(self.current_number)
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.action, self.action_rect)
        screen.blit(self.input, self.input_rect)
        self.handle_name_inputs(screen)
    def handle_human_players_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.logger.info("Making Player {0}".format(self.name))
                self.players.append(Human(self.name, self.avatars[self.current_number - 1], self.offsets[self.current_number - 1][0], self.offsets[self.current_number - 1][1]))
                self.current_number += 1
                self.name = ""
                if self.current_number > self.player_number:
                    self.logger.info("Creating Bots")
                    for i in range(self.current_number, 5):
                        self.players.append(Computer(self.name, self.avatars[i - 1], self.offsets[i- 1][0], self.offsets[i - 1][1], 50))
                    self.switch_scene(QueryMode(self.players))
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            else:
                key = pygame.key.name(event.key)
                if key in string.ascii_lowercase:
                    self.name += key
                    self.name = self.name.capitalize()
        
    def handle_name_inputs(self, screen):
        self.title = self.font.render("Enter the player name for {0}:".format(self.current_number), True, (0,128,0))
        self.title_rect = self.title.get_rect(center=(self.width/2, self.title.get_height()/2))
        self.input = self.font.render(str(self.name), True, (0, 128, 0))
        self.input_rect = self.input.get_rect(center=(self.width/2, self.height/2))
        self.action = self.small_font.render("Press <return> to save!", True, (0,128,0))
        self.action_rect = self.action.get_rect(center=(self.width/2, self.height - self.action.get_height()))
