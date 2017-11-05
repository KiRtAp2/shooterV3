import base_class
import random
import constants
import textures


class Powerup(base_class.Base):
    """Powerup class"""

    def __init__(self, pos, type):
        self.x, self.y = pos
        self.sx, self.sy = constants.powerup_size
        self.type = type
        self.timer = constants.powerup_timer * constants.framerate

    def show(self, window):
        try:
            window.blit(textures.powerup_images[self.type], (self.x, self.y))
        except:
            window.blit(textures.powerup_null, (self.x, self.y))

    def tick(self):
        self.timer -= 1

    def is_old(self):
        return self.timer <= 0

    @staticmethod
    def spawn(powerup_list: list):
        position = random.randrange(200, constants.window_width-200), random.randrange(30, constants.frame_height-constants.powerup_size[1]-30)
        powerup_list.append(Powerup(position, random.randrange(1, 6)))
