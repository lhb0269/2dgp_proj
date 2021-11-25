import random
import json
import os

from pico2d import *

import game_framework
import title_state
import server
import game_world
from mario import HERO
from monster import Monster
from block import BLOCK
from background import *

name = "MainState"

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
    server.floor = load_image('floor.png')
    server.mon = Monster()
    server.hero = HERO()

    server.cloud = CLOUDS()
    server.mountain = Mountain()
    server.woods = WOODS()
    server.cs = castle()
    server.se = sewer()
    server.floor = FLOOR()
    server.blocks = [BLOCK(400), BLOCK(460), BLOCK(520)]
    game_world.add_object(server.cloud,0)
    game_world.add_object(server.mountain,0)
    game_world.add_object(server.woods,0)
    game_world.add_object(server.floor,0)
    game_world.add_object(server.mon,1)
    game_world.add_object(server.hero,1)
    game_world.add_object(server.cs,0)
    game_world.add_object(server.se,0)
    game_world.add_objects(server.blocks,1)


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
            server.hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        if game_object == server.hero:
            game_object.update(server.mon,server.blocks)
        else:
            game_object.update()
def draw():
    clear_canvas()
    back.draw(200, 200)
    for game_obejct in game_world.all_objects():
       game_obejct.draw()
    update_canvas()





