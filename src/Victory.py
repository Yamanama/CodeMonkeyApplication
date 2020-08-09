from Scene import Scene
import pygame


class Victory(Scene):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.width, self.height = pygame.display.get_surface().get_size()
        self.font = pygame.font.SysFont("Arial", 32)
        self.small_font = pygame.font.SysFont("Arial", 14)
        self.message = self.font.render(
            "Congratulations {0}. You win!".format(player.name), True, (0, 128, 0))
        self.exit_message = self.small_font.render(
            "Press <esc> to exit", True, (0, 128, 0))
        self.message_rect = self.message.get_rect(
            center=(self.width/2, self.height/3))
        self.exit_rect = self.exit_message.get_rect(
            center=(self.width/2, self.height - self.exit_message.get_height()/2))

    def process_input(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        caption = "Victory!"
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        self.player.draw_face(screen, self.width/2 - 100,
                              self.height/2 - 100, 200, 200)
        screen.blit(self.message, self.message_rect)
        screen.blit(self.exit_message, self.exit_rect)
