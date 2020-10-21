import pygame as py

class Beat:
    def __init__(self, lane):
        self.lane = lane
        self.pos = [100, 0]

    def draw(self, display):
        py.draw.circle(display, py.Color('blue'), self.pos, 20)