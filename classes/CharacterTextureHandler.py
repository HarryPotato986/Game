import pygame

class CharacterTextureHandler:

    def __init__(self, resourceLocation, idleUp, idleRight, idleLeft, idleDown, walkingUp, walkingRight, walkingLeft, walkingDown, scale):
        self.idleUp = pygame.image.load(resourceLocation + "/" + idleUp)
        self.idleRight = pygame.image.load(resourceLocation + "/" + idleRight)
        self.idleLeft = pygame.image.load(resourceLocation + "/" + idleLeft)
        self.idleDown = pygame.image.load(resourceLocation + "/" + idleDown)
        self.walkUp = [pygame.image.load(resourceLocation + "/" + walkingUp[0]), pygame.image.load(resourceLocation + "/" + walkingUp[1])]
        self.walkRight = [pygame.image.load(resourceLocation + "/" + walkingRight[0]), pygame.image.load(resourceLocation + "/" + walkingRight[1])]
        self.walkLeft = [pygame.image.load(resourceLocation + "/" + walkingLeft[0]), pygame.image.load(resourceLocation + "/" + walkingLeft[1])]
        self.walkDown = [pygame.image.load(resourceLocation + "/" + walkingDown[0]), pygame.image.load(resourceLocation + "/" + walkingDown[1])]
        self.scaleTextures(scale)
        self.idles = [self.idleUp, self.idleRight, self.idleLeft, self.idleDown]


    def scaleTextures(self, scale):
        self.idleUp = pygame.transform.scale_by(self.idleUp, scale)
        self.idleRight = pygame.transform.scale_by(self.idleRight, scale)
        self.idleLeft = pygame.transform.scale_by(self.idleLeft, scale)
        self.idleDown = pygame.transform.scale_by(self.idleDown, scale)
        self.walkUp = [pygame.transform.scale_by(self.walkUp[0], scale), pygame.transform.scale_by(self.walkUp[1], scale)]
        self.walkRight = [pygame.transform.scale_by(self.walkRight[0], scale), pygame.transform.scale_by(self.walkRight[1], scale)]
        self.walkLeft = [pygame.transform.scale_by(self.walkLeft[0], scale), pygame.transform.scale_by(self.walkLeft[1], scale)]
        self.walkDown = [pygame.transform.scale_by(self.walkDown[0], scale), pygame.transform.scale_by(self.walkDown[1], scale)]
