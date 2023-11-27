import pygame


class BaseItem:

    def __init__(self, resourceLocation, texture, itemName):
        self.texture = pygame.image.load(resourceLocation + "/" + texture)
        self.itemName = itemName

