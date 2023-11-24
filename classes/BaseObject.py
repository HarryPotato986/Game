import pygame


class BaseObject:
    def __init__(self, surface, colour, x, y, width, height):
        self.surface = surface
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collisionBox = pygame.Rect((self.x, self.y, self.width, self.height))

    def updateRect(self):
        self.collisionBox = pygame.Rect((self.x, self.y, self.width, self.height))

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.collisionBox)
