import pygame

import constants

class Sheet:
    def __init__(self, filename):
        self.image = pygame.image.load(filename).convert()

loaded_sheets = []

loaded_sheets.insert(constants.SS_ENEMIES, "")

def load(sheet_index, rect):
    sheet = loaded_sheets[sheet_index]
    sprite = pygame.Surface(rect.size).convert()
    sprite.blit(sheet, (0, 0), rect)
    return sprite