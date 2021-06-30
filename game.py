import pygame

import constants

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("My awesome swords game!!!!")

import sprite

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Test code: draw a sprite
    tile0 = sprite.load(constants.SS_TILES, pygame.Rect(0, 8, 16, 16))

    screen.blit(tile0, (200, 200))

    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False