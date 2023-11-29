import pygame


class CollisionBox:

    activeBoxs = []

    def __init__(self, x, y, width, height, boxOf):
        self.baseRect = pygame.Rect((x, y, width, height))
        self.boxOf = boxOf
        CollisionBox.activeBoxs.append(self)


