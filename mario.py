from pico2d import *

import game_framework
import game_world
import main_state
from fire import Fire
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
LEFT_DOWN,RIGHT_DOWN,LEFT_UP,RIGHT_UP,JUMP_DOWN,JUMP_UP,JUMP_END,SPACE,LEVELUP = range(9)
event_name = 'LEFT_DOWN', 'RIGHT_DOWN', 'LEFT_UP', 'RIGHT_UP', 'JUMP_DOWN','JUMP_UP','JUMP_END','SPACE','LEVEL_UP'
Run_Img_code = 'mario_run.png','big_mario_run.png'
stand_img_code = 'mario_stand.png'

img_ylist=50,90
key_event_table ={
    (SDL_KEYDOWN,SDLK_a):LEFT_DOWN,
    (SDL_KEYDOWN,SDLK_d):RIGHT_DOWN,
    (SDL_KEYUP,SDLK_a):LEFT_UP,
    (SDL_KEYUP,SDLK_d):RIGHT_UP,
    (SDL_KEYDOWN,SDLK_w):JUMP_DOWN,
    (SDL_KEYUP,SDLK_w):JUMP_UP,
    (SDL_KEYDOWN,SDLK_SPACE):SPACE,
    (SDL_KEYDOWN,SDLK_r):LEVELUP
}

class IdleState:
    def enter(HERO,event):
        global dir
        if HERO.die == False:
            if event == LEFT_DOWN:
                dir=1
            elif event == RIGHT_DOWN:
                dir=-1
            elif event == LEFT_UP:
                dir=0
            elif event == RIGHT_UP:
                dir=0
    def exit(HERO,event):
        if event == SPACE:
            HERO.fire()
        if event == LEVELUP:
            HERO.levelup()
            print('level')

    def do(HERO):
        HERO.frame = (HERO.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 50, HERO.x, HERO.y)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 50, 2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
            HERO.lookright = False
        if  HERO.Falling == True:
            HERO.frame = 1
        if HERO.die == True:
            HERO.image2 = load_image('mario_dead.png')
            JumpState.do(HERO)
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
class RunState:
    def enter(HERO, event):
        global dir
        if HERO.die == False:
            if event == LEFT_DOWN:
                dir=1
            elif event == RIGHT_DOWN:
                dir=-1
            elif event == LEFT_UP:
                dir=0
            elif event == RIGHT_UP:
                dir=0
    def exit(HERO,event):
        if event == SPACE:
            HERO.fire()
        if event == LEVELUP:
            HERO.levelup()
            print('level')
    def do(HERO):
        HERO.frame = (HERO.frame + FRAMES_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % 8
        HERO.x += HERO.velocity * game_framework.frame_time
        HERO.x =clamp(25,HERO.x,1600-25)

    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 100, HERO.x, HERO.y,50,50)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 100, 2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
            HERO.lookright = False
        if HERO.die == True:
            HERO.image2 = load_image('mario_dead.png')
            JumpState.do(HERO)
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)
class JumpState:
    def enter(HERO,event):
        if HERO.Jumping == False:
            HERO.Falling = False
            HERO.Jumping = True
            HERO.endy = HERO.y+400
            print(HERO.endy)
        pass
    def exit(HERO,event):
        if event == SPACE:
            HERO.fire()
        HERO.Jumping = True
    def do(HERO):
        if HERO.Falling == False and HERO.Jumping == True:
            HERO.y += JUMP_SPEED_PPS
        if HERO.y >= HERO.endy:
            HERO.Falling = True
            HERO.add_event(JUMP_END)
        HERO.frame = 1
    def draw(HERO):
        if dir == -1:
            HERO.image.clip_draw(int(HERO.frame) * 50, 0, 50, 50, HERO.x, HERO.y)
            HERO.lookright = True
        if dir == 1:
            HERO.image.clip_composite_draw(int(HERO.frame) * 50, 0, 50, 50, 2 * 3.14, 'h', HERO.x,HERO.y, 50, 50)
            HERO.lookright = False
        if HERO.Falling == True:
            HERO.frame = 1
        if HERO.lookright == True and dir == 0:
            HERO.image2.draw(HERO.x, HERO.y)
        if HERO.lookright == False and dir == 0:
            HERO.image2.composite_draw(2 * 3.14, 'h', HERO.x, HERO.y, 50, 50)

next_state_table = {
    JumpState:{JUMP_DOWN:JumpState,JUMP_UP:JumpState,RIGHT_DOWN:RunState,LEFT_DOWN:RunState,LEFT_UP:RunState,RIGHT_UP:RunState,JUMP_END:RunState,SPACE:JumpState,},
    IdleState:{LEFT_UP:RunState,RIGHT_UP:RunState,LEFT_DOWN:RunState,RIGHT_DOWN:RunState,JUMP_DOWN:JumpState,JUMP_UP:JumpState,SPACE:IdleState,JUMP_END:IdleState
               ,LEVELUP:IdleState},
    RunState:{LEFT_UP:IdleState,RIGHT_UP:IdleState,LEFT_DOWN:IdleState,RIGHT_DOWN:IdleState,JUMP_DOWN:JumpState,JUMP_UP:RunState,SPACE:RunState,JUMP_END:RunState,
              LEVELUP:RunState}
}
class HERO:

    def __init__(self):
        self.image = load_image('mario_run.png')
        self.image2 = load_image('mario_stand.png')
        self.die_image = load_image('mario_dead.png')
        self.x = 400
        self.y = 62
        self.miny = 62
        self.frame = 0
        self.velocity=0
        self.levelcode = 0  #0 일반 1 커짐 2 불공격가능 3 무적
        self.die = False
        self.endy=self.y+400
        self.lookright = True #캐릭터 보고 있는 방향 체크
        self.Falling = False
        self.Jumping = False #점프가 가능하냐?
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
        if self.Falling == True:
            self.frame = 1
            self.y -= JUMP_SPEED_PPS
    def add_event(self, event):
        self.event_que.insert(0, event)
    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            # if DEBUG_KEY == key_event:
            #     print(history[-10:])
            self.add_event(key_event)
    def fire(self):
        fire = Fire(self.x,self.y,dir)
        game_world.add_object(fire,1)
    def levelup(self):
        self.levelcode +=1
        self.image=load_image(Run_Img_code[self.levelcode])

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25