import pygame
from Board import Board
from Player import Player
class Game(object):
    """
    The Game - Based on the pygame framework

    """
    def __init__(self):
        super().__init__()
        pygame.init()
        # colors
        self.colors = {    
            'black': (0,0,0),
            'blue': (0,0,255),
            'green': (0,255,0),
            'white': (255,255,255),
            'red': (255,0,0)
        }
        # clock - for FPS
        self.clock = pygame.time.Clock()
        self.background = self.colors['black']
        self.screen_width = 900
        self.screen_height = 900
        self.board = Board(self.colors, self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.cell_width = self.screen_width / len(self.board.board) 
        self.cell_height = self.screen_height / len(self.board.board[0])
        self.running = True
    def run(self):
        """
        Run loop - Show the game board
        """
        while self.running:
            # Change the caption to the player and moves
            caption = "Player:" + str(self.board.players[self.board.current_player].avatar) + " Moves: " + str(self.board.moves)
            # Display the caption
            pygame.display.set_caption(caption)
            # Paint the background
            self.screen.fill(self.background)
            # Draw the board
            self.board.draw(self.screen)
            # Handle key events
            self.handle_events()
            # Update the drawing
            self.update()
        pygame.quit()
    def update(self):
        """
        Update the drawing
        """
        pygame.display.update()
        self.clock.tick(60)

    def handle_events(self):
        """
        Handle user events
        """
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYUP:
                # send key strokes to the board
                self.board.move_player(event.key, self.board.players[self.board.current_player])
                # escape to quit
                if event.key == pygame.K_ESCAPE: 
                    self.running = False   
            if event.type == pygame.QUIT:
                self.running = False

if __name__ == "__main__": 
    game = Game()
    game.run() 