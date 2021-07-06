import pygame

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

running = True
while running:
    screen.fill(constants.C_BLACK)


    screen.blit(camera, config.camera_pos)
    pygame.display.flip()
    clock.tick(constants.FPS)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            event_handler.handle(event)

    # Movement
    # Temporary location: these just move the camera for now.
    if config.L:
        config.camera_pos = (config.camera_pos[0] + 2, config.camera_pos[1])
    if config.R:
        config.camera_pos = (config.camera_pos[0] - 2, config.camera_pos[1])
    if config.U:
        config.camera_pos = (config.camera_pos[0], config.camera_pos[1] + 2)
    if config.D:
        config.camera_pos = (config.camera_pos[0], config.camera_pos[1] - 2)
