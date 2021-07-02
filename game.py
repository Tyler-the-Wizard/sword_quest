import pygame

import constants

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("My awesome swords game!!!!")

from tile import Tile

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Test code: draw a tile
    tile0 = Tile(pygame.Rect(0, 8, 16, 16), (200, 400), {"can_touch": True})
    tile0.draw(screen)

    tile0.x, tile0.y = 400, 600
    tile0.draw(screen)

    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass