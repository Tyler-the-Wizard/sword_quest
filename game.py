import pygame

import constants

pygame.init()
clock = pygame.time.Clock()
pygame.display.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("Quest of the Two Swords")

import tile

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Test code: draw some tiles
    tile.TILES[1].draw(screen, (0, 0))
    tile.TILES[1].draw(screen, (64, 0))
    tile.TILES[1].draw(screen, (0, 64))

    pygame.display.flip()
    clock.tick(constants.FPS)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass