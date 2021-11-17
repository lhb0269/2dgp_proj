from pico2d import *
import mario
import game_framework

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 0.05
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 2
class Monster:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 500
        self.y = 62
        self.frame = 0
    def update(self):
        self.frame = (self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%2
        self.x += (mario.dir / 2) -RUN_SPEED_PPS
    def draw(self):
        self.image.clip_draw(int(self.frame) * 80, 0, 80, 80, self.x, self.y)
        if self.x <=-100:
            self.x=1000
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x -20, self.y - 28, self.x + 40, self.y + 44