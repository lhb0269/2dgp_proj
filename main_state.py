import random
import json
import os

from pico2d import *

import game_framework
import title_state
import mario
import monster
import block
import background

name = "MainState"

hero = None
mon = None
font = None
cloud = None
mountain = None
woods = None
cs = None
se = None
blocks = None


def enter():
    global hero,mon,cloud,mountain,woods,cs,se,blocks,back,floor
    back = load_image('background.png')
    floor = load_image('floor.png')

    mon = monster.Monster()
    hero = mario.HERO()

    cloud = background.CLOUDS()
    mountain = background.Mountain()
    woods = background.WOODS()
    cs = background.castle()
    se = background.sewer()
    blocks = [block.BLOCK(400), block.BLOCK(460), block.BLOCK(520)]

def exit():
    global hero,mon,cloud,mountain,woods,cs,se,blocks,back,floor
    del(hero)
    del (mon)
    del (cloud)
    del (mountain)
    del (woods)
    del (cs)
    del (se)
    del (blocks)
    del (back)
    del (floor)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_a:
                mario.dir = 1
            elif event.key == SDLK_d:
                mario.dir = -1
            elif event.key == SDLK_w:
                mario.jumping = True
        elif event.type == SDL_KEYUP:
            mario.dir = 0


def update():
    mon.update()
    hero.update(mon, blocks)
    cloud.update()
    mountain.update()
    woods.update()
    cs.update()
    se.update()
    for block in blocks:
        block.update()
    update_canvas()


def draw():
    back.draw(200, 200)
    floor.clip_draw(0, 0, 800, 40, 400, 20)
    cloud.draw()
    mountain.draw()
    woods.draw()
    cs.draw()
    mon.draw()
    hero.draw()
    se.draw()
    for block in blocks:
        block.draw()






