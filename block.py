from pico2d import *

import game_world
import mario
import random
import game_framework
import server

from background import STAR

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 3
ypos_list = [250,400]

class BLOCK:
    BOY_X0, BOY_Y0 = -20, 60
    def __init__(self,xpos):
        self.x = xpos
        self.y = 250
        self.image = load_image('sprite.png')
        self.image2= load_image('itembox.png')
        self.life = 3
        self.code = 1 #블럭 종류 판별
        self.make = False
        self.frame = 0
    def setbox(self):
        self.x = random.randint(1, 5) * 60 + 900
        self.y = ypos_list[random.randint(0, 1)]
        self.code = random.randint(0,1)
        if self.code == 0:
            self.life = 3
        elif self.code == 1:
            self.life = 2
    def update(self):
        self.x += (mario.dir / 2)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if self.x < -100:
            self.x = 1000
            self.setbox()
        if self.x > 1100:
            self.x = -50
            self.setbox()
        if self.life == 0:
            self.setbox()
    def draw(self):
        if self.code == 0:
            self.image.clip_draw(950, 500, 60, 53, self.x, self.y)
        else:
            self.image2.clip_draw(33*int(self.frame),0,32,35,self.x,self.y,60,60)
        draw_rectangle(*self.get_top_bb())
        draw_rectangle(*self.get_bottom_bb())
    def get_bb(self):
        return self.x -30, self.y - 26, self.x + 30, self.y + 26
    def get_top_bb(self):
        return self.x - 30, self.y, self.x + 30, self.y + 28
    def get_bottom_bb(self):
        return self.x - 30, self.y-28, self.x + 30, self.y
    def make_obj(self):
        if self.code == 1 and self.life == 1 and self.make == False:
            server.star=STAR(self.x,self.y)
            game_world.add_object(server.star,1)
            self.make=True

