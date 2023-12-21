import pygame


class RoomRenderer:

    def __init__(self, surface):
        self.surface = surface
        self.currentRoom = None
        self.activeTexture = None


    def ticker(self, room):
        self.draw(room)

    def draw(self, room):
        if room != self.currentRoom:
            self.activeTexture = pygame.image.load(room.texture)
            self.activeTexture = pygame.transform.scale_by(self.activeTexture, .75)
            self.currentRoom = room
        self.surface.blit(self.activeTexture, (0, 0, 1200, 900))
