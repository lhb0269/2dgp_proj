from pico2d import *
def handle_events():
   global running
   global dir
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_ESCAPE:
               running = False
           elif event.key == SDLK_LEFT:
               dir =1
           elif event.key == SDLK_RIGHT:
               dir =-1
       elif event.type == SDL_KEYUP:
           dir = 0
open_canvas()
running = True
movex,movey=0,0 #움직이지 않는 오브젝트들의 이동
dir = 0 #방향값
background = load_image('background.png')
mountain = load_image('sprite.png')
woods = load_image('sprite.png')
clouds = load_image('sprite.png')
floor = load_image('floor.png')
character=load_image('character.png')
cloud_move=1    #움직이는 구름
cloudx=0        #구름의 위치를 초기화할때 필요함.
cx,cy=400,70    #캐릭터 좌표
def draw_object():      #오브젝트 그리기,움직임
    global cloud_move
    global movex
    global cloudx
    global cx,cy
    clouds_x=450+ cloudx / 2 + cloud_move / 5
    if clouds_x < -100:
        clouds_x = 450
        cloud_move = 0
        cloudx=0
    background.draw(200, 200)
    mountain.clip_draw(330, 142, 210, 100, 200 + movex / 5, 80 + movey)
    woods.clip_draw(22, 142, 290, 70, 450 + movex / 5, 70 + movey)
    clouds.clip_draw(680, 300, 280, 200, clouds_x, 550 + movey)
    floor.clip_draw(0,0,800,40,400,20)
    character.draw(cx,cy)
    movex+=dir*5

    cloud_move+=dir*2-1
while running:
    draw_object()
    update_canvas()
    handle_events()
    delay(0.001)

