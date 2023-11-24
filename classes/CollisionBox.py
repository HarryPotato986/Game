import pygame


class CollisionBox:

    activeBoxs = []

    def __init__(self, x, y, width, height):
        self.baseRect = pygame.Rect((x, y, width, height))

        CollisionBox.activeBoxs.append(self)


