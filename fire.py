from pico2d import *

import game_framework
import game_world
import main_state
import server
import collision
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 50
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Fire:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity*-1

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * game_framework.frame_time*RUN_SPEED_PPS
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
        if collision.collide(self,server.mon):
            server.mon.x = 1000
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5
