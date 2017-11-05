import base_class
import pygame
import constants


class Bullet(base_class.Base):

    def __init__(self, pos: tuple, color: tuple, dxy: tuple, pierce_walls=False):
        self.x, self.y = pos
        self.color = color
        self.dx, self.dy = dxy
        self.sx, self.sy = constants.bullet_size
        self.pierce_walls = pierce_walls

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def show(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.sx, self.sy))

    def is_out_ouf_bounds(self):
        return self.x > constants.window_width or self.x+self.sx < 0 or self.y+self.sy < 0 or self.y > constants.frame_height

    @property
    def owner_num(self):
        return 1 if self.dx > 0 else 2
