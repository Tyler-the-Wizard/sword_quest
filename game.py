import pygame
from pygame.constants import SCALED

import config
import constants

import event_handler

pygame.init()
config.init()
clock = pygame.time.Clock()
pygame.display.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("Quest of the Two Swords")

import level

# Test code: draw a level
# test_level = [48, 24] + [1, 0] * 24 + [0] * 48 + ([1] + [0] * 45 + [1, 0] + [0] * 48) * 10 + [1, 0] * 24 + [0] * 48
# level.save("levels/big_level.lv", test_level)

# test_level = [8, 4,
#     2, 2, 2, 2, 2, 2, 2, 2,
#     2, 0, 0, 0, 0, 0, 0, 2,
#     2, 0, 0, 0, 0, 0, 0, 2,
#     2, 2, 2, 2, 2, 2, 2, 2
# ]
# level.save("levels/wide_level.lv", test_level)

my_level = level.load("levels/big_level.lv")
camera = pygame.Surface((my_level[0] * constants.TILE_SCALE * constants.GRAPHICS_SCALE,
                         my_level[1] * constants.TILE_SCALE * constants.GRAPHICS_SCALE))
level.draw(my_level, camera)

# Initialize the player
import player as pl
config.player = pl.Player()

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Add the level to the screen
    screen.blit(camera, config.camera_pos)

    # Draw all miscellaneous sprites
    for sprite in config.sprites:
        sprite.draw(camera)

    # Draw all actors
    for actor in config.actors:
        actor.draw(camera)

    pygame.display.flip()
    clock.tick(constants.FPS)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            event_handler.handle(event)

    # Movement
    # Temporary location: may be moved later
    if config.L:
        config.player.x -= constants.PLAYER_SPEED
    if config.R:
        config.player.x += constants.PLAYER_SPEED
    # if config.U:
    #     config.player.y -= constants.PLAYER_SPEED
    # if config.D:
    #     config.player.y += constants.PLAYER_SPEED

    if config.Jump:
        config.player.dy = -constants.PLAYER_JUMP_POWER

    # Camera position
    config.camera_pos = (
        min(0, constants.SCREEN_SIZE[0] / 2 - config.player.x), 
        min(0, max(constants.SCREEN_SIZE[1], constants.SCREEN_SIZE[1] / 2 - config.player.y) )
    )
