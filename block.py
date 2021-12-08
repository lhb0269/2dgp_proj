from pico2d import *

import game_world
import mario
import random
import game_framework
import server

from background import STAR
from background import FLOWER
from background import COIN
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 3
ypos_list = [200,400]

class BLOCK:
    BOY_X0, BOY_Y0 = -20, 60
    def __init__(self,xpos):
        self.x = xpos
        self.y = 200
        self.image = load_image('sprite.png')
        self.image2= load_image('itembox.png')
        self.image3= load_image('emptyblock.png')
        self.life = 2
        self.code = 1 #블럭 종류 판별
        self.make = False
        self.frame = 0
        self.objectcode=0
    def setbox(self):
        self.x = random.randint(15, 18) * 60
        if self.x > server.se.x-71 and self.x < server.se.x+71:
            self.x = random.randint(1, 5) * 30 + 900
        self.y = ypos_list[random.randint(0, 1)]
        self.code = random.randint(0,1)
        if self.code == 0:
            self.life = 3
        elif self.code == 1:
            self.life = 2
        self.make = False
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
        elif self.code == 1:
            self.image2.clip_draw(33*int(self.frame),0,32,35,self.x,self.y,60,60)
        elif self.code == 2:
            self.image3.clip_draw(0, 0, 35, 35, self.x, self.y,60,60)
    def get_bb(self):
        return self.x -30, self.y - 26, self.x + 30, self.y + 26
    def get_top_bb(self):
        return self.x - 30, self.y, self.x + 30, self.y + 28
    def get_bottom_bb(self):
        return self.x - 30, self.y-28, self.x + 30, self.y
    def make_obj(self):
        if self.code == 1 and self.life == 1 and self.make == False:
            self.objectcode = random.randint(0,8)
            if self.objectcode == 0:
                server.star=STAR(self.x,self.y,self)
                game_world.add_object(server.star,0)
                self.make=True
            elif self.objectcode == 1:
                server.flower = FLOWER(self.x, self.y,self)
                game_world.add_object(server.flower, 0)
                self.make = True
            else:
                server.coin = COIN(self.x, self.y, self)
                game_world.add_object(server.coin, 0)
                self.make = True
            self.code=2
    def getXpos(self):
        return self.x

