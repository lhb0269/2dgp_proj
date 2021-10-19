from pico2d import *
def handle_events():
   global running
   global dir
   global jumping
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_ESCAPE:
               running = False
           elif event.key == SDLK_a:
               dir =1
           elif event.key == SDLK_d:
               dir =-1
           elif event.key == SDLK_w:
               jumping = True
       elif event.type == SDL_KEYUP:
           dir = 0
open_canvas()
running = True
jumping = False
class Monster:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 500
        self.y = 62
        self.frame = 0
    def update(self):
        self.frame = (self.frame+1)%2
        self.x += (dir / 2) -0.25
    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        if self.x <=-100:
            self.x=1000
class castle:
    def __init__(self):
        self.image = load_image('castle.png')
        self.x = 1800
        self.y = 140
    def update(self):
        self.x+=dir/2
    def draw(self):
        self.image.draw(self.x,self.y)
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
    def update(self,mon,block):
        global jumping
        self.frame=(self.frame+1)%8
        if (mon.x == self.x and mon.y == self.y) or (mon.x+60 == self.x and mon.y == self.y):#죽음 판정
            self.x = 1000
        if self.x>=mon.x and self.x<=mon.x+77 and self.y <= mon.y + 60 and self.Falling == True:# 몬스터 피격
            mon.x=1000
        if self.x>=block.x-40 and self.x<=block.x+60 and self.y >= block.y-50  and jumping == True:
            jumping = False
            self.Falling = True
            block.life -= 1
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
        if self.lookright == True and dir == 0:
            self.image2.draw(self.x,self.y)
        if self.lookright == False and dir == 0:
            self.image2.composite_draw(2*3.14,'h',self.x,self.y,50,50)
class CLOUDS:
    def __init__(self):
        self.image = load_image('sprite.png')
        self.x = 450
        self.y = 550
    def update(self):
        self.x -=1
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
        self.x +=(dir/2)
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
        self.x += (dir / 2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
    def draw(self):
        self.image.clip_draw(22, 142, 290, 70, self.x,self.y)
class BLOCK:
    def __init__(self):
        self.x = 500
        self.y = 200
        self.image = load_image('sprite.png')
        self.life = 3
        self.i=3
    def update(self):
        self.x += (dir / 2)
        if self.x < -100:
            self.x = 1000
        if self.x > 1100:
            self.x = -50
        if self.life % self.i != 0:
            self.i -= 1
        if self.life ==0:
            self.x = 1000
    def draw(self):
        for i in range(2, 5):
            self.y += i
        for i in range(2, 5):
            self.y -= i
        self.image.clip_draw(950, 500, 60, 53, self.x, self.y)

dir = 0 #방향값
background = load_image('background.png')
floor = load_image('floor.png')

mon = Monster()
hero = HERO()
cloud = CLOUDS()
mountain = Mountain()
woods = WOODS()
cs = castle()
block = BLOCK()

def Update_Obj():
    mon.update()
    hero.update(mon,block)
    cloud.update()
    mountain.update()
    woods.update()
    cs.update()
    block.update()

def Draw_obj():
    background.draw(200, 200)
    floor.clip_draw(0, 0, 800, 40, 400, 20)
    cloud.draw()
    mountain.draw()
    woods.draw()
    cs.draw()
    mon.draw()
    hero.draw()
    block.draw()

while running:
    #update obj
    Update_Obj()
    #draw object
    Draw_obj()


    update_canvas()
    handle_events()
    #delay(0.001)