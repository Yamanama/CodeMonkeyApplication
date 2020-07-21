from Scene import Scene
import pygame
class Victory(Scene):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.width, self.height = pygame.display.get_surface().get_size()
    def process_input(self, events):
        pass
    def update(self):
        pass
    def render(self, screen):
        caption = "Victory!"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        self.player.draw_face(screen, self.width/2 - 100, self.height/2 - 100, 200, 200)