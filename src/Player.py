import pygame

class Player():
    """
    Player
    """
    def __init__(self, name, avatar="assets/laughing.png", offsetX=0, offsetY=0):
        # TODO: Hook up to settings scene?
        self.name = name
        self.avatar = avatar
        self.x = 400
        self.y = 400
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.pies = []

    def draw(self, screen):
        """
        Draw the player on the board
        """
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (50,50))
        screen.blit(img, (self.x + self.offsetX, self.y + self.offsetY))
        
    def draw_statistics(self, screen, x, y):
        """
        Draw the statistics (The big head)
        """
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (150,150))
        screen.blit(img, (x + 75, y))
        self.draw_pies(screen, x, y + 200)
    
    def draw_face(self, screen, x, y, width, height):
        img = pygame.image.load(self.avatar)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x, y))

    def draw_pies(self, screen, x, y):
        """
        Draw the pies
        """
        x += 12.5
        for pie in self.pies:
            pygame.draw.rect(screen, pygame.Color(pie), (x, y, 50, 50))
            x += 75
    
    def add_pie(self, color):
        if color not in self.pies:
            self.pies.append(color)