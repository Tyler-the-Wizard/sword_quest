import pygame

import constants

def load_filename(filename):
    return pygame.image.load("sprites/" + filename).convert()

sheet_cache = []

sheet_cache.insert(constants.SS_TILES, load_filename("tiles.png"))

def load(sheet_index, rect):
    sheet = sheet_cache[sheet_index]
    sprite = pygame.Surface(rect.size).convert()
    sprite.blit(sheet, (0, 0), rect)
    sprite = pygame.transform.scale(sprite, (constants.TILE_SCALE, constants.TILE_SCALE))
    return sprite