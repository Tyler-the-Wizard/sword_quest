import config
import constants
from sprite import Sprite

actors = {
    "player": (constants.SS_PLAYER, (0, 0, 20, 24))
}

class Actor(Sprite):
    def __init__(self, name, coords):
        # spritesheet and rect are given by name
        super().__init__(actors[name][0], actors[name][1], coords)
        self.dx = 0
        self.dy = 0
        self.has_gravity = True

        config.actors.append(self)

    def draw(self, surface):
        super().draw(surface)
        self.x += self.dx
        self.y += self.dy
        if self.y > 600:
            self.y = 600

        if self.has_gravity:
            self.dy += constants.GRAVITY