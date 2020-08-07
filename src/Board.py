import logging
from Cell import Cell
from Computer import Computer
from Human import Human
from Question import Question
from Victory import Victory
from Scene import Scene
from Dice import Dice
import pygame
import os
class Board(Scene):
    """
    The board
    """
    def __init__(self, width, height, mode, players):
        super().__init__()
        self.logger = logging.getLogger("Board")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.logger.info("Creating Board")
        self.players = players
        self.current_player = 0
        self.logger.info("Polishing Dice")
        self.dice = Dice()
        self.moves = self.dice.roll()
        self.mode = mode
        # The board
        self.board = [
            [Cell('red'), Cell('white'), Cell('blue'), Cell('green'), Cell('red'), Cell('white'), Cell('blue'), Cell('green'), Cell('white')],
            [Cell('white'), None, None, None, Cell('blue'), None, None, None, Cell('blue')],
            [Cell('blue'), None, None, None, Cell('white'), None, None, None, Cell('green')],
            [Cell('green'), None, None, None, Cell('green'), None, None, None, Cell('red')],
            [Cell('red'), Cell('white'), Cell('blue'), Cell('green'), Cell('black'), Cell('green'), Cell('red'), Cell('blue'), Cell('white')],
            [Cell('blue'), None, None, None, Cell('green'), None, None, None, Cell('blue')],
            [Cell('green'), None, None, None, Cell('white'), None, None, None, Cell('green')],
            [Cell('red'), None, None, None, Cell('red'), None, None, None, Cell('red')],
            [Cell('white'), Cell('blue'), Cell('red'), Cell('green'), Cell('blue'), Cell('white'), Cell('red'), Cell('green'), Cell('blue')],      
        ]
        self.width = width
        self.height = height
        self.cell_width = width / len(self.board) 
        self.cell_height = height / len(self.board[0])

    def move_player(self, direction, player):
        """
        Move players around the board
        """
        if direction == pygame.K_LEFT:
            left = int((player.x-self.cell_width)/self.cell_width)
            if left < 0:
                return
            cell = self.board[left][int(player.y/self.cell_height)]
            if cell is not None:
                player.x -= 100
                self.cycle_turn()
        if direction == pygame.K_RIGHT:
            right = int((player.x+self.cell_width)/self.cell_width)
            print("RIGHT:", right)
            if right > len(self.board[0]) - 1:
                return
            cell = self.board[right][int(player.y/self.cell_height)]
            if cell is not None:
                player.x += 100
                self.cycle_turn()
        if direction == pygame.K_UP:
            up = int((player.y-self.cell_height)/self.cell_height)
            print("UP:", up)
            if up < 0:
                return
            cell = self.board[int((player.x)/self.cell_width)][int(up)]
            if cell is not None:
                player.y -= 100
                self.cycle_turn()
        if direction == pygame.K_DOWN:
            down = int((player.y+self.cell_height)/self.cell_height)
            print("DOWN", down)
            if down > len(self.board) - 1:
                return
            cell = self.board[int((player.x)/self.cell_width)][int(down)]
            if cell is not None:
                player.y += 100
                self.cycle_turn()
    def cycle_turn(self):
        """
        Cycle the turn after moves are 0
        """
        self.moves -= 1
        if self.moves <= 0:
            self.moves = self.dice.roll()
            self.next_player()
    def next_player(self):
        """
        Go to the next player
        """
        current_player = self.players[self.current_player]
        column = int(current_player.x/self.cell_width)
        row = int(current_player.y/self.cell_height)
        color = self.get_cell_color(row, column)
        if color != 'black':
            self.switch_scene(Question(color, self, current_player, False))
        else:
            if len(current_player.pies) == 4:
                self.switch_scene(Question(color, self, current_player, True))
            else:
                self.switch_scene(Question(color, self, current_player, False))
        self.current_player +=1
        if self.current_player > 3:
            self.current_player = 0
    def draw(self, screen):
        """
        Draw the board on screen
        """
        screen.fill(pygame.Color('black'))
        self.draw_board(screen)
        self.draw_player_stats(screen)
        self.draw_players(screen)
    def draw_player_stats(self, screen):
        """
        Draw the 'player stats (The big head)
        """
        self.players[0].draw_statistics(screen, 100, 110)
        self.players[1].draw_statistics(screen, 500, 110)
        self.players[2].draw_statistics(screen, 100, 510)
        self.players[3].draw_statistics(screen, 500, 510)
    def draw_players(self, screen):
        """
        Draw the players on the square they're on
        """
        for player in range(len(self.players)):
            self.players[player].draw(screen)
    def draw_board(self, screen):
        """
        Draw the board
        """
        cell_width = self.width / len(self.board) 
        cell_height = self.height / len(self.board[0])
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[column][row] is not None:
                    cell = self.board[column][row]
                    pygame.draw.rect(screen, pygame.Color(cell.color), (row*self.cell_width, column*self.cell_height, self.cell_width, self.cell_height))
    def get_cell_color(self, x,y):
        """
        Get the color of a cell
        """
        return self.board[x][y].color
    
    def process_input(self, events):
        if type(self.players[self.current_player]) is Human:    
            for event in events:
                # print(event)
                if event.type == pygame.KEYUP:
                    # send key strokes to the board
                    self.move_player(event.key, self.players[self.current_player])
                    # escape to quit
                    if event.key == pygame.K_ESCAPE: 
                        self.running = False
        else:
            self.players[self.current_player].move(self.board, self.cell_width, self.cell_height)
            self.cycle_turn()
    def update(self):
        pass

    def render(self,screen):
        # Change the caption to the player and moves
        caption = "Player:" + str(self.players[self.current_player].name) + " Moves: " + str(self.moves)
        # Display the caption
        pygame.display.set_caption(caption)
        self.draw(screen)