from pico2d import *

import game_framework

jumping = True
dir = 0
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


JUMP_SPEED_KMPH= 0.1
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM/60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 8

history = [] #()현재상태ㅐ,이벤트) 튜플의 리스트
LEFT_DOWN,RIGHT_DOWN,LEFT_UP,RIGHT_UP,JUMP_DOWN,JUMP_UP,JUMP_END = range(7)
event_name = 'LEFT_DOWN', 'RIGHT_DOWN', 'LEFT_UP', 'RIGHT_UP', 'JUMP_DOWN','JUMP_UP','JUMP_END'

key_event_table ={
    (SDL_KEYDOWN,SDLK_a):LEFT_DOWN,
    (SDL_KEYDOWN,SDLK_d):RIGHT_DOWN,
    (SDL_KEYUP,SDLK_a):LEFT_UP,
    (SDL_KEYUP,SDLK_d):RIGHT_UP,
    (SDL_KEYDOWN,SDLK_w):JUMP_DOWN,
    (SDL_KEYUP,SDLK_w):JUMP_UP
}

class IdleState:
    def enter(HERO,event):
        print('idle')
        global dir
        if event == LEFT_DOWN:
            HERO.velocity -= RUN_SPEED_PPS
            dir=1
        elif event == RIGHT_DOWN:
            HERO.velocity += RUN_SPEED_PPS
            dir=-1
        elif event == LEFT_UP:
            HERO.velocity += RUN_SPEED_PPS
            dir=0
        elif event == RIGHT_UP:
            HERO.velocity -= RUN_SPEED_PPS
            dir=0
    def exit(HERO,event):
        pass

    def do(HERO):
        HERO.frame = (HERO.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 50, HERO.x, HERO.y)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 50, 2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
            HERO.lookright = False
        if jumping == True or HERO.Falling == True:
            HERO.frame = 1
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
class RunState:
    def enter(HERO, event):
        global dir
        if event == LEFT_DOWN:
            HERO.velocity -= RUN_SPEED_PPS
            dir=1
        elif event == RIGHT_DOWN:
            HERO.velocity += RUN_SPEED_PPS
            dir=-1
        elif event == LEFT_UP:
            HERO.velocity += RUN_SPEED_PPS
            dir=0
        elif event == RIGHT_UP:
            HERO.velocity -= RUN_SPEED_PPS
            dir=0
    def exit(HERO,event):
        pass
    def do(HERO):
        HERO.frame = (HERO.frame + FRAMES_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % 8
        HERO.x += HERO.velocity * game_framework.frame_time
        HERO.x =clamp(25,HERO.x,1600-25)

    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 50, HERO.x, HERO.y)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 50, 2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
            HERO.lookright = False
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
class JumpState:
    def enter(HERO,event):
        pass
    def exit(HERO,event):
        print('jump out')
    def do(HERO):
        global jumping
        if jumping == True and HERO.Falling == False:
            HERO.frame = 1
            if HERO.y < HERO.endy:
                HERO.y += JUMP_SPEED_PPS
            if HERO.y >= HERO.endy:
                HERO.Falling = True
                jumping = False
        if jumping == False and HERO.Falling == True:
            HERO.frame = 1
            if HERO.y >= HERO.miny:
                HERO.y -= JUMP_SPEED_PPS
            if HERO.y <= HERO.miny:
                HERO.Falling = False
                jumping = True
                HERO.add_event(JUMP_END)
    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 50, HERO.x, HERO.y)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 50, 2 * 3.14, 'h', HERO.x,HERO.y, 50, 50)
            HERO.lookright = False
        if jumping == True or HERO.Falling == True:
            HERO.frame = 1
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)

next_state_table = {
    JumpState:{JUMP_DOWN:JumpState,JUMP_UP:JumpState,RIGHT_DOWN:RunState,LEFT_DOWN:RunState,LEFT_UP:RunState,RIGHT_UP:RunState,JUMP_END:RunState},
    IdleState:{LEFT_UP:RunState,RIGHT_UP:RunState,LEFT_DOWN:RunState,RIGHT_DOWN:RunState,JUMP_DOWN:JumpState,JUMP_UP:JumpState},
    RunState:{LEFT_UP:IdleState,RIGHT_UP:IdleState,LEFT_DOWN:IdleState,RIGHT_DOWN:IdleState,JUMP_DOWN:JumpState,JUMP_UP:RunState}
}
class HERO:
    def __init__(self):
        self.image = load_image('mario_run.png')
        self.image2 = load_image('mario_stand.png')
        self.x = 400
        self.y = 62
        self.miny = 62
        self.frame = 0
        self.velocity=0
        self.endy=self.y+200
        self.lookright = True #캐릭터 보고 있는 방향 체크
        self.Falling = False
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def update(self,mon,blocks):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                history.append((self.cur_state.__name__,event_name[event]))
                self.cur_state = next_state_table[self.cur_state][event]
            except:
                print('State: ', self.cur_state.__name__ , 'Event: ',event_name[event])
                exit(-1)
            self.cur_state.enter(self, event)
        # global jumping
        # self.frame=(self.frame+1)%8
        # if (mon.x == self.x and mon.y+10 >= self.y) or (mon.x+80 == self.x and mon.y+10 >= self.y):#죽음 판정
        #     self.x = 1000
        # if self.x>=mon.x-20 and self.x<=mon.x+80 and self.y <= mon.y + 60 and self.Falling == True:# 몬스터 사망
        #     mon.x=1000
        # for block in blocks:
        #  if self.x>=block.x-40 and self.x<=block.x+40 and self.y >= block.y-50  and jumping == True: #벽 위로 박기
        #         jumping = False
        #         self.Falling = True
        #         block.life -= 1
        # if self.x>=block.x and self.x<=block.x+60 and self.y <= block.y+50  and self.y >= block.y and jumping == False:#벽 위에 서기
        #     self.Falling = False
        #     self.miny = self.y-1
        #     self.y+=3
        #     self.endy = self.y + 200
    # def jump(self):
    #     global jumping
    #     if jumping == True and self.Falling == False:
    #         self.frame = 1
    #         if self.y < self.endy:
    #             self.y+=0.5
    #         if self.y >= self.endy:
    #             self.Falling = True
    #             jumping = False
    #     if jumping == False and self.Falling == True:
    #         self.frame=1
    #         if self.y >= self.miny:
    #             self.y-=1
    #         if self.y <= self.miny:
    #             self.Falling = False
    def add_event(self, event):
        self.event_que.insert(0, event)
    def draw(self):
        self.cur_state.draw(self)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            # if DEBUG_KEY == key_event:
            #     print(history[-10:])
            self.add_event(key_event)