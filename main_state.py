import random
import json
import os

from pico2d import *

import game_framework
import title_state
import game_world
from mario import HERO
from monster import Monster
from block import BLOCK
from background import *

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
    mon = Monster()
    hero = HERO()

    cloud = CLOUDS()
    mountain = Mountain()
    woods = WOODS()
    cs = castle()
    se = sewer()
    blocks = [BLOCK(400), BLOCK(460), BLOCK(520)]
    game_world.add_object(cloud,0)
    game_world.add_object(mountain,0)
    game_world.add_object(woods,0)
    game_world.add_object(mon,1)
    game_world.add_object(hero,1)
    game_world.add_object(cs,1)
    game_world.add_object(se,1)
    game_world.add_objects(blocks,1)


def exit():
    game_world.clear()

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
    for game_object in game_world.all_objects():
        if game_object == hero:
            game_object.update(mon,blocks)
        else:
            game_object.update()

def draw():
    clear_canvas()
    back.draw(200, 200)
    floor.clip_draw(0, 0, 800, 40, 400, 20)
    for game_obejct in game_world.all_objects():
       game_obejct.draw()
    update_canvas()





