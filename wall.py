import base_class
import colors
import constants


class Wall(base_class.Base):
    """Wall class"""

    def __init__(self, ycenterpos, xpos):
        self.y = ycenterpos-(constants.wall_height/2)
        self.x = xpos
        self.sx = constants.wall_width
        self.sy = constants.wall_height
        self.timer = constants.framerate * constants.wall_last  # 5 seconds

    def tick(self):
        """Should be called once per tick. Updates timer"""
        self.timer -= 1

    def is_old(self):
        """Returns True if self should be destroyed"""
        return self.timer <= 0

    def show(self, window):
        if constants.theme == "black":
            window.fill(colors.wall_black_theme, (self.x, self.y, self.sx, self.sy))
        elif constants.theme == "white":
            window.fill(colors.wall_white_theme, (self.x, self.y, self.sx, self.sy))
