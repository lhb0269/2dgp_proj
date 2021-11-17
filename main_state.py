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
floor = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def heroblock(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bottom_bb()

    if left_a > right_b: return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

def heroblockstand(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_top_bb()

    if left_a > right_b: return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

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
    floor = FLOOR()
    blocks = [BLOCK(400), BLOCK(460), BLOCK(520)]
    game_world.add_object(cloud,0)
    game_world.add_object(mountain,0)
    game_world.add_object(woods,0)
    game_world.add_object(floor,0)
    game_world.add_object(mon,1)
    game_world.add_object(hero,1)
    game_world.add_object(cs,0)
    game_world.add_object(se,0)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        if game_object == hero:
            game_object.update(mon,blocks)
        else:
            game_object.update()
    if collide(hero, mon):
        pass
        hero.die = True
    for block in blocks:
        if collide(hero,block):
            if heroblock(hero,block):
                hero.Falling = True
                block.life -= 1
            if heroblockstand(hero, block):
                hero.Falling = False
    if collide(hero, floor):
        hero.Falling = False
    #if collide(hero,se):

def draw():
    clear_canvas()
    back.draw(200, 200)
    for game_obejct in game_world.all_objects():
       game_obejct.draw()
    update_canvas()





