# from pico2d import *
# import mario
# import monster
# import block
# import background
# import random
# def handle_events():
#    global running
#    events = get_events()
#    for event in events:
#        if event.type == SDL_QUIT:
#            running = False
#        elif event.type == SDL_KEYDOWN:
#            if event.key == SDLK_ESCAPE:
#                running = False
#            elif event.key == SDLK_a:
#                mario.dir =1
#            elif event.key == SDLK_d:
#                mario.dir =-1
#            elif event.key == SDLK_w:
#                mario.jumping = True
#        elif event.type == SDL_KEYUP:
#            mario.dir = 0
# open_canvas()
#
# #initialize Obj
# running = True
# back = load_image('background.png')
# floor = load_image('floor.png')
#
# mon = monster.Monster()
# hero = mario.HERO()
#
# cloud = background.CLOUDS()
# mountain = background.Mountain()
# woods = background.WOODS()
# cs = background.castle()
# se = background.sewer()
# blocks = [block.BLOCK(400),block.BLOCK(460),block.BLOCK(520)]
# #
# def Update_Obj():
#     mon.update()
#     hero.update(mon,blocks)
#     cloud.update()
#     mountain.update()
#     woods.update()
#     cs.update()
#     se.update()
#     for block in  blocks:
#         block.update()
#
# def Draw_obj():
#     back.draw(200, 200)
#     floor.clip_draw(0, 0, 800, 40, 400, 20)
#     cloud.draw()
#     mountain.draw()
#     woods.draw()
#     cs.draw()
#     mon.draw()
#     hero.draw()
#     se.draw()
#     for block in blocks:
#         block.draw()
#
# while running:
#     #update obj
#     Update_Obj()
#     #draw object
#     Draw_obj()
#
#
#     update_canvas()
#     handle_events()
#     #delay(0.001)
import game_framework
import pico2d

import start_state

pico2d.open_canvas()
game_framework.run(start_state)
pico2d.clear_canvas()