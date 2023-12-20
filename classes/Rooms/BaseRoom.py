import pygame

from classes.CollisionBox import CollisionBox


class BaseRoom:

    def __init__(self, resourceLocation, texture, collisionBoxs):
        self.texture = resourceLocation + '/' + texture
        self.collisionBoxs = []
        if isinstance(collisionBoxs, tuple):
            if isinstance(collisionBoxs[0], tuple):
                for box in collisionBoxs:
                    newBox = CollisionBox(box[0], box[1], box[2], box[3], self)
                    self.collisionBoxs.append(newBox)
            else:
                newBox = CollisionBox(collisionBoxs[0], collisionBoxs[1], collisionBoxs[2], collisionBoxs[3], self)
                self.collisionBoxs.append(newBox)

        self.deactivateCollisionBoxs()

    def activateCollisionBoxs(self):
        for boxs in self.collisionBoxs:
            boxs.activate()

    def deactivateCollisionBoxs(self):
        for boxs in self.collisionBoxs:
            boxs.deactivate()
