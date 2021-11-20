from pico2d import *

import mario
import mario
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 0.08
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
class castle:
    def __init__(self):
        self.image = load_image('castle.png')
        self.x = 2400
        self.y = 140
    def update(self):
        self.x+=mario.dir/2
    def draw(self):
        self.image.draw(self.x,self.y)
class FLOOR:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('floor.png')
        self.x,self.y = 400,20
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0, 0, 800, 40, self.x, self.y)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 400, self.y - 20, self.x + 400, self.y + 20
class CLOUDS:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 450
        self.y = 550
    def update(self):
        self.x -=RUN_SPEED_PPS
        if self.x <-100:
            self.x = 1000
    def draw(self):
        self.image.clip_draw(680,300,280,200,self.x,self.y)
class Mountain:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 200
        self.y = 90
    def update(self):
        self.x +=(mario.dir/2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
    def draw(self):
        self.image.clip_draw(330, 142, 210, 100, self.x,self.y)
class WOODS:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 500
        self.y = 75
    def update(self):
        self.x += (mario.dir / 2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
    def draw(self):
        self.image.clip_draw(22, 142, 290, 70, self.x,self.y)
class sewer:
    def __init__(self):
        self.x = 750
        self.y = 110
        self.image = load_image('sprite.png')
    def update(self):
        self.x += (mario.dir / 2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
    def draw(self):
        self.image.clip_draw(1165,140,142,140,self.x,self.y)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 71, self.y-70, self.x + 71, self.y + 70
