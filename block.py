from pico2d import *
import mario
import random

ypos_list = [250,400]

class BLOCK:
    def __init__(self,xpos):
        self.x = xpos
        self.y = 250
        self.image = load_image('sprite.png')
        self.life = 3
    def update(self):
        self.x += (mario.dir / 2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
        if self.life ==0:
            self.x =random.randint(1,5)*60+900
            self.y = ypos_list[random.randint(0,1)]
            self.life=3
    def draw(self):
        self.image.clip_draw(950, 500, 60, 53, self.x, self.y)
        draw_rectangle(*self.get_top_bb())
        draw_rectangle(*self.get_bottom_bb())
    def get_bb(self):
        return self.x -30, self.y - 26, self.x + 30, self.y + 26
    def get_top_bb(self):
        return self.x - 30, self.y, self.x + 30, self.y + 28
    def get_bottom_bb(self):
        return self.x - 30, self.y-28, self.x + 30, self.y