import config
import constants
from sprite import Sprite

actors = {
    "player": (constants.SS_TILES, (0, 0, 8, 8))
}

class Actor(Sprite):
    def __init__(self, name, coords):
        # spritesheet and rect are given by name
        super().__init__(actors[name][0], actors[name][1], coords)
        config.actors.append(self)