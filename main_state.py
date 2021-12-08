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
from monster import TURTLE
from block import BLOCK
from background import *

name = "MainState"
clear = False
def enter():
    global hero,mon,cloud,mountain,woods,cs,se,blocks,back,floor,clearbgm
    back = load_image('background.png')
    server.floor = load_image('floor.png')
    server.timefont = load_font('ENCR10B.TTF', 16)
    server.scorefont = load_font('ENCR10B.TTF', 16)
    server.mon = [Monster(800),Monster(1000)]
    server.turtle = TURTLE(900)
    server.hero = HERO()
    server.cloud = CLOUDS()
    server.mountain = Mountain()
    server.woods = WOODS()
    server.cs = castle()
    server.se = sewer()
    server.flag = FLAG()
    server.floor = FLOOR()
    server.blocks = [BLOCK(400), BLOCK(460), BLOCK(520),BLOCK(640),BLOCK(700)]
    game_world.add_object(server.cloud,0)
    game_world.add_object(server.mountain,0)
    game_world.add_object(server.woods,0)
    game_world.add_object(server.floor,0)
    game_world.add_object(server.flag, 0)
    game_world.add_objects(server.mon,1)
    game_world.add_object(server.turtle,1)
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
    global clear
    for game_object in game_world.all_objects():
        game_object.update()
    server.time = get_time()
    if server.time >= 40.0:
        if clear == False:
            server.cs.setpos(server.hero.x+1000)
            server.flag.setpos(server.hero.x+800)
            clear = True
def draw():
    clear_canvas()
    back.draw(200, 200)
    for game_obejct in game_world.all_objects():
       game_obejct.draw()
    server.timefont.draw(650,550,'Time : %3.1f'%server.time,(0,0,0))
    server.scorefont.draw(50,550,'Score : %d'%server.score,(0,0,0))
    update_canvas()