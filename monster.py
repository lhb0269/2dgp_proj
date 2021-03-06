import random

from pico2d import *

import collision
import game_world
import mario
import game_framework
import server

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 0.05
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 2
class Monster:
    def __init__(self,x):
        self.image = load_image('sprite.png')
        self.x = x
        self.y = 62
        self.frame = 0
        self.dir = 1
        self.die = False
        self.diesound = load_wav('enemy_die.wav')
        self.diesound.set_volume(64)
    def update(self):
        if self.die == False:
            self.frame = (self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2
            if collision.collide(self,server.se):
                self.dir *=-1
                self.x -= self.dir
            else:
                self.x -= RUN_SPEED_PPS * self.dir
        else:
            self.y -= RUN_SPEED_PPS*2
            if self.y <0:
                server.score += 100
                self.initialize()
        if self.x <= -100:
            self.initialize()
        if self.x > 2000:
            self.initialize()
    def draw(self):
        if self.die == True:
            self.image.clip_composite_draw(80, 0, 80, 80, 2 * 3.14, 'v', self.x, self.y,80,80)
        else:
            self.image.clip_draw(int(self.frame) * 80, 0, 80, 80, self.x, self.y)
    def get_bb(self):
        return self.x -20, self.y - 28, self.x + 40, self.y + 44

    def get_top_bb(self):
        return self.x - 20, self.y+35, self.x + 40, self.y + 40
    def get_bottom_bb(self):
        return self.x - 20, self.y+35, self.x + 40, self.y-32
    def initialize(self):
        if server.time<40.0:
            self.die = False
            self.x = 900
            self.y=62
            self.setypos(1000)
    def setypos(self,y):
        self.y = y

class TURTLE:
    def __init__(self, x):
        self.image = load_image('turtle.png')
        self.x = x
        self.y = 62
        self.dir = 1
        self.die = False
        self.diesound = load_wav('enemy_die.wav')
        self.diesound.set_volume(64)

    def update(self):
        if self.die == False:
            if collision.collide(self, server.se):
                self.dir *= -1
                self.x -= self.dir
            else:
                self.x -= RUN_SPEED_PPS * self.dir
        else:
            self.y -= RUN_SPEED_PPS * 2
            if self.y < 0:
                server.score += 100
                self.initialize()
        if self.x <= -100:
            self.initialize()
        if self.x > 2000:
            self.initialize()
    def draw(self):
        if self.die == True:
            self.image.clip_composite_draw(0, 0, 50, 50, 2 * 3.14, 'v', self.x, self.y, 50, 50)
        else:
            if self.dir == 1:
                self.image.clip_composite_draw(0, 0, 50, 50, 2 * 3.14, 'h', self.x, self.y, 50, 50)
            else:
                self.image.clip_draw(0,0,50,50,self.x,self.y)
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def get_top_bb(self):
        return self.x - 25, self.y + 20, self.x + 25, self.y + 25

    def get_bottom_bb(self):
        return self.x - 25, self.y + 20, self.x + 25, self.y - 25

    def initialize(self):
        if server.time < 40.0:
            self.die = False
            self.x = 1000
            self.y = 62
    def setypos(self,y):
        self.y = y
