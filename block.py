from pico2d import *
import mario
import random
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
            self.x +=random.randint(1,5)*60+480
            self.life=3
    def draw(self):
        self.image.clip_draw(950, 500, 60, 53, self.x, self.y)