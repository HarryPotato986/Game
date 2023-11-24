import pygame
from classes.CollisionBox import CollisionBox

class BaseObject:
    def __init__(self, surface, colour, x, y, width, height):
        self.surface = surface
        self.colour = colour
        self.collisionBox = CollisionBox(x, y, width, height)


    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.collisionBox.baseRect)
