import pygame



class BaseRoom:

    def __init__(self, resourceLocation, texture):
        self.texture = resourceLocation + '/' + texture


    def draw(self):
        pass
