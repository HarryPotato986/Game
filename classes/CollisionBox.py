import pygame


class CollisionBox:

    activeBoxs = []

    def __init__(self, x, y, width, height, boxOf):
        self.baseRect = pygame.Rect((x, y, width, height))
        self.boxOf = boxOf
        CollisionBox.activeBoxs.append(self)
        self.active = True


    def resize(self, width, height):
        self.baseRect.width = width
        self.baseRect.height = height

    def activate(self):
        if self not in CollisionBox.activeBoxs:
            CollisionBox.activeBoxs.append(self)
            self.active = True

    def deactivate(self):
        if self in CollisionBox.activeBoxs:
            CollisionBox.activeBoxs.remove(self)
            self.active = False
