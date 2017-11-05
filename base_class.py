import constants


class Base(object):

    def __init__(self, pos=(0, 0), size=(0, 0)):
        """Unpacks pos into x, y and size into sx, sy"""
        self.x, self.y = pos
        self.sx, self.sy = size

    def is_hit(self, other):
        """Returns whether 'self' is intercepting 'other'"""
        return self.x < other.x+other.sx and self.x+self.sx > other.x and self.y < other.y+other.sy and self.y+self.sy > other.y

    def correct_bounds(self):
        """Corrects position if object is out of bound"""
        if self.y < 0:
            self.y = 0

        if self.y+self.sy > constants.frame_height:
            self.y = constants.frame_height-self.sy

        if self.x < 0:
            self.x = 0

        if self.x+self.sx > constants.window_width:
            self.x = constants.window_width-self.sx
