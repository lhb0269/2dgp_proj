from pico2d import *
import mario
class Monster:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 500
        self.y = 62
        self.frame = 0
    def update(self):
        self.frame = (self.frame+1)%2
        self.x += (mario.dir / 2) -0.25
    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        if self.x <=-100:
            self.x=1000