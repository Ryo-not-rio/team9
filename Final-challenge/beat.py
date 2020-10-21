import pygame as py

beat_width = 40

class Beat:
    def __init__(self, lane):
        self.lane = lane
        self.pos = [int(((800 - beat_width*4)/2 + beat_width/2) + lane*beat_width), 0]

    def is_success(self, pos):
        if abs(pos[1] - self.pos[1]) < 5:
            return True
        return False

    def draw(self, display):
        py.draw.circle(display, py.Color('blue'), self.pos, int(beat_width/2))
