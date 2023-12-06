import pygame


class BaseItem:

    def __init__(self, resourceLocation, texture, itemName):
        self.resourceLocation = resourceLocation
        self.texture = texture
        self.itemName = itemName

