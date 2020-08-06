import pygame
from Scene import Scene
from Settings import Settings
from Human import Human
from Computer import Computer
from Question import Question
class Title(Scene):
    """
    Title scene. Entry point for the game
    """
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 32) 
        self.small_font = pygame.font.SysFont("Arial", 14)       
        self.title = self.font.render("Trivial Purfuit", True, (0,128,0))
        self.company = self.small_font.render("Brought to you by Code Monkey's", True, (0,128,0))
        self.subtitle = self.font.render("Minimal Edition", True, (0,128,0))
        self.action = self.small_font.render("Press <RETURN> To Start", True, (0,128,0))
        self.width, self.height = pygame.display.get_surface().get_size()
        self.title_rect = self.title.get_rect(center=(self.width/2, self.height/3))
        self.subtitle_rect = self.subtitle.get_rect(center=(self.width/2, self.height/2))
        self.action_rect = self.action.get_rect(center=(self.width/2, self.height*2/3))
        self.company_rect = self.company.get_rect(center=(self.width/2, self.height - self.company.get_height()/2))
        self.players = [
            Human("1", "assets/laughing.png", 0, 0),
            Computer("2","assets/neutral.png", 0, 50, 50),
            Computer("3", "assets/shy.png", 50, 0, 90), 
            Computer("4","assets/smile.png", 50, 50, 100)
            ]
        self.direction = 1
        self.current = 0
    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switch_scene(Settings(self.players))
    def update(self):
        pass
    
    def render(self, screen):
        caption = "Trivial Purfuit - Minimal Edition"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.subtitle, self.subtitle_rect)
        screen.blit(self.action, self.action_rect)
        screen.blit(self.company, self.company_rect)
        self.update_players_position(screen)
        self.draw_players(screen, self.current, screen.get_width()/2 + 50)
    
    def draw_players(self, screen, x, y):
        for player in self.players:
            player.draw_face(screen, x, y, 50, 50)
            x += 75
    def update_players_position(self, screen):
        if self.current == 0:
            self.direction = 1
        if self.current == screen.get_width() - (75 *4 -25 ):
            self.direction = -1
        self.current += self.direction