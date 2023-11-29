import pygame
from classes.CollisionBox import CollisionBox

class BaseObject:
    def __init__(self, surface, x, y, width, height, asset="red"):
        self.surface = surface
        self.asset = asset
        self.collisionBox = CollisionBox(x, y, width, height, self)


    def draw(self):
        pygame.draw.rect(self.surface, self.asset, self.collisionBox.baseRect)
