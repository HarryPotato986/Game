import copy

import pygame

from Init import ItemInit
from classes.BaseObject import BaseObject
from classes.Entities.Character.Character import Character
from classes.Entities.Enemys.BaseEnemy import BaseEnemy

pygame.init()
screen = pygame.display.set_mode((1200, 900), pygame.SCALED)
clock = pygame.time.Clock()

running = True
dt = 0

roomTexture = pygame.image.load("assets/room_textures/Room number 1.png")
roomTexture = pygame.transform.scale_by(roomTexture, .75)

characterAssets = ["back profile.png", "right-profile-1-(new).png", "left-profile-1-(new).png", "front profile.png",
                   ["back profile left walk.png", "back profile right walk.png"], ["right-profile-walk-1-(newer).png", "right-profile-walk-2-(newer).png"],
                   ["left-profile-walk-2-(newer).png", "left-profile-walk-1-(newer).png"], ["front profile left walk.png", "front profile right walk.png"]]

smallGoblinAssets = ["goblin back 1.png", "goblin right profile 1.png", "goblin left profile 1.png", "goblin front 1.png",
             ["goblin back walk left foot 1.png", "goblin back walk right foot 1.png"], ["goblin right profile left foot walk 1.png", "goblin right profile right foot walk 1.png"],
             ["goblin left profile left foot walk 1.png", "goblin left profile right foot walk 1.png"], ["goblin back walk left foot 1.png", "goblin back walk right foot 1.png"]]

allFiller = ["filler.png", "filler.png", "filler.png", "filler.png",
             ["filler.png", "filler.png"], ["filler.png", "filler.png"],
             ["filler.png", "filler.png"], ["filler.png", "filler.png"]]

character = Character(screen, 600, 450, "assets/character_textures", characterAssets, 0.5, "character", copy.deepcopy(ItemInit.testSword), copy.deepcopy(ItemInit.testBow), copy.deepcopy(ItemInit.testSingleUse), 100)
testRect = BaseObject(screen, 200, 200, 100, 100, "green")
testRect2 = BaseObject(screen, 750, 500, 80, 200, "blue")
testRect3 = BaseObject(screen, 200, 700, 50, 50, "yellow")
testRect4 = BaseObject(screen, 900, 200, 50, 50, 'purple')
testEnemy = BaseEnemy(screen, 600, 50, "assets/small_goblin_textures", smallGoblinAssets, 0.5, "test enemy", copy.deepcopy(ItemInit.testSword), 100)


while running:

    screen.fill("black")
    #screen.blit(roomTexture, (0, 0, 1200, 900))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            character.attack(event)
            character.changeActiveSlot(event)

    testRect.draw()
    testRect2.draw()
    testRect3.draw()
    testRect4.draw()
    testEnemy.draw()

    keys = pygame.key.get_pressed()
    character.ticker(keys, dt)


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
