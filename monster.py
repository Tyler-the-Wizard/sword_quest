import config
import constants
from sprite import Sprite

monsters = {
    "player": (constants.SS_TILES, (15, 15, 8, 8))
}

class Monster(Sprite):
    def __init__(self, name, coords):
        # spritesheet and rect are given by name
        super().__init__(monsters[name][0], monsters[name][1], coords)
        config.monsters.append(self) 