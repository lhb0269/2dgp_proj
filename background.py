from pico2d import *

import collision
import game_world
import mario
import game_framework
import server

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 0.08
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

PIXEL_PER_METER = (10.0/0.3)
OBJ_SPEED_KMPH = 2.0
OBJ_SPEED_MPM = (OBJ_SPEED_KMPH * 1000.0 / 60.0)
OBJ_SPEED_MPS = (OBJ_SPEED_MPM/60.0)
OBJ_SPEED_PPS = (OBJ_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 4
class castle:
    def __init__(self):
        self.image = load_image('castle.png')
        self.x = -2000
        self.y = 140
    def update(self):
        self.x+=mario.dir/2
    def draw(self):
        self.image.draw(self.x,self.y)
    def setpos(self,x):
        self.x = x
class FLAG:
    def __init__(self):
        self.image = load_image('flag.png')
        self.x = server.cs.x- 200
        self.y = 310
    def update(self):
        self.x+=mario.dir/2
    def draw(self):
        self.image.draw(self.x,self.y,105,135*4)
    def get_bb(self):
        return self.x,self.y - 270,self.x + 52 , self.y + 270
    def setpos(self,x):
        self.x = x
class FLOOR:
    image = None
    def __init__(self):
        if self.image == None:
            self.image = load_image('floor.png')
        self.x,self.y = 400,20
        self.bgm = load_music('main_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
    def update(self):
        if server.hero.clear == True:
            self.bgm = None
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
            self.x = 2000
    def draw(self):
        self.image.clip_draw(22, 142, 290, 70, self.x,self.y)
class sewer:
    def __init__(self):
        self.x = 200
        self.y = 110
        self.image = load_image('sprite.png')
    def update(self):
        if server.time<40.0:
            self.x += (mario.dir / 2)
            if self.x < -100:
                self.x = 1000
            if self.x > 1100:
                self.x = -50
        else:
            self.setypos(1000)
    def draw(self):
        self.image.clip_draw(1165,140,142,140,self.x,self.y)
    def get_bb(self):
        return self.x - 71, self.y-70, self.x + 71, self.y + 70
    def get_top_bb(self):
        return self.x - 71, self.y+60, self.x + 71, self.y + 70
    def get_bottom_bb(self):
        return self.x - 71, self.y-70, self.x + 71, self.y+60
    def setypos(self,y):
        self.y = y


class FLOWER:
    def __init__(self,x,y,block):
        self.x = x
        self.y = y
        self.endy = y + 50
        self.image = load_image('flower.png')
        self.frame = 0
        self.parent = block
    def update(self):
        self.x += (mario.dir/2)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.y < self.endy and self.x == self.parent.getXpos():
            self.y += OBJ_SPEED_PPS * game_framework.frame_time
        if collision.collide(server.hero, self):
            self.parent.make = False
            server.hero.levelup(2)
            game_world.remove_object(self)
            server.score+=150
        if self.x < -100 or self.x > 1100:
            self.parent.make = False
            game_world.remove_object(self)
        if self.x != self.parent.getXpos():
            self.y -= OBJ_SPEED_PPS * game_framework.frame_time*2
    def draw(self):
        self.image.clip_draw(25*int(self.frame),0,25,25,self.x,self.y,50,50)
    def get_bb(self):
        return self.x - 25,self.y - 25,self.x + 25 , self.y + 25

class STAR:
    def __init__(self,x,y,block):
        self.x = x
        self.y = y
        self.endy = y+50
        self.image = load_image('star.png')
        self.frame = 0
        self.parent = block
    def update(self):
        self.x += (mario.dir / 2)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.y < self.endy and self.x == self.parent.getXpos():
            self.y += OBJ_SPEED_PPS * game_framework.frame_time
        if collision.collide(server.hero, self):
            self.parent.make = False
            server.hero.levelup(2)
            server.score+=1000
            game_world.remove_object(self)
        if self.x < -100 or self.x > 1100:
            self.parent.make = False
            game_world.remove_object(self)
        if self.x != self.parent.getXpos():
            self.y -= OBJ_SPEED_PPS * game_framework.frame_time*2
    def draw(self):
        self.image.clip_draw(25*int(self.frame),0,25,29,self.x,self.y,50,50)
    def get_bb(self):
        return self.x - 25,self.y - 25,self.x + 25 , self.y + 25

class COIN:
    def __init__(self,x,y,block):
        self.x = x
        self.y = y
        self.endy = y+100
        self.image = load_image('coin.png')
        self.frame = 0
        self.parent = block
        self.falling = False
        self.coinsound = load_wav('Coin.wav')
        self.coinsound.set_volume(32)
        self.coinsound.play()
    def update(self):
        self.x += (mario.dir / 2)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.y < self.endy and self.falling == False:
            self.y += OBJ_SPEED_PPS * game_framework.frame_time * 20
        if self.y >= self.endy:
            self.falling = True
        if self.falling == True:
            self. y -= OBJ_SPEED_PPS * game_framework.frame_time * 20
            if self.y <= self.endy - 50 :
                server.score+=500
                game_world.remove_object(self)
    def draw(self):
        self.image.clip_draw(60*int(self.frame),0,60,60,self.x,self.y,50,50)
    def get_bb(self):
        return self.x - 25,self.y - 25,self.x + 25 , self.y + 25

class MUSHROOM:
    def __init__(self,x,y,block):
        self.x = x
        self.y = y
        self.endy = y+50
        self.image = load_image('mush.png')
        self.frame = 0
        self.parent = block
    def update(self):
        self.x += (mario.dir / 2)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.y < self.endy and self.x == self.parent.getXpos():
            self.y += OBJ_SPEED_PPS * game_framework.frame_time
        if collision.collide(server.hero, self):
            self.parent.make = False
            if server.hero.levelcode!=2:
                server.hero.levelup(1)
                server.hero.levelupsound.play()
            server.score+=250
            game_world.remove_object(self)
        if self.x < -100 or self.x > 1100:
            self.parent.make = False
            game_world.remove_object(self)
        if self.x != self.parent.getXpos():
            self.y -= OBJ_SPEED_PPS * game_framework.frame_time*2
    def draw(self):
        self.image.clip_draw(0,0,50,50,self.x,self.y)
    def get_bb(self):
        return self.x - 25,self.y - 25,self.x + 25 , self.y + 25