from pico2d import *

jumping = False
dir = 0
class HERO:
    def __init__(self):
        self.image = load_image('mario_run.png')
        self.image2 = load_image('mario_stand.png')
        self.x = 400
        self.y = 62
        self.miny = 62
        self.frame = 0
        self.endy=self.y+200
        self.lookright = True #캐릭터 보고 있는 방향 체크
        self.Falling = False
    def update(self,mon,blocks):
        global jumping
        self.frame=(self.frame+1)%8
        if (mon.x == self.x and mon.y+10 >= self.y) or (mon.x+80 == self.x and mon.y+10 >= self.y):#죽음 판정
            self.x = 1000
        if self.x>=mon.x-20 and self.x<=mon.x+80 and self.y <= mon.y + 60 and self.Falling == True:# 몬스터 사망
            mon.x=1000
        for block in blocks:
         if self.x>=block.x-40 and self.x<=block.x+40 and self.y >= block.y-50  and jumping == True: #벽 위로 박기
                jumping = False
                self.Falling = True
                block.life -= 1
        if self.x>=block.x and self.x<=block.x+60 and self.y <= block.y+50  and self.y >= block.y and jumping == False:#벽 위에 서기
            self.Falling = False
            self.miny = self.y-1
            self.y+=3
            self.endy = self.y + 200
    def jump(self):
        global jumping
        if jumping == True and self.Falling == False:
            self.frame = 1
            if self.y < self.endy:
                self.y+=0.5
            if self.y >= self.endy:
                self.Falling = True
                jumping = False
        if jumping == False and self.Falling == True:
            self.frame=1
            if self.y >= self.miny:
                self.y-=1
            if self.y <= self.miny:
                self.Falling = False
    def draw(self):
        self.jump()
        if dir == -1:
            self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
            self.lookright = True
        if dir == 1:
            self.image.clip_composite_draw(self.frame * 50, 0 ,50, 50, 2*3.14,'h',self.x, self.y,50,50)
            self.lookright = False
        if jumping == True or self.Falling == True:
            self.frame = 1
        if self.lookright == True and dir == 0:
            self.image2.draw(self.x,self.y)
        if self.lookright == False and dir == 0:
            self.image2.composite_draw(2*3.14,'h',self.x,self.y,50,50)