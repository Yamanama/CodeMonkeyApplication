import pygame
import logging
from Title import Title


class Game(object):
    """
    The Game - Based on the pygame framework

    """

    def __init__(self):
        super().__init__()
        pygame.init()
        self.logger = logging.getLogger("Game")
        logging.basicConfig(
            format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.logger.info("Initializing Game")
        self.logger.info("Winding the clock")
        # clock - for FPS
        self.clock = pygame.time.Clock()
        self.background = pygame.Color('black')
        self.screen_width = 900
        self.screen_height = 900
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.logger.info("Moving to Title Scene")
        self.active_scene = Title()
        self.running = True

    def run(self):
        """
        Run loop - Show the game board
        """
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.active_scene.process_input(events)
            self.active_scene.update()
            self.active_scene.render(self.screen)
            self.active_scene = self.active_scene.next
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
