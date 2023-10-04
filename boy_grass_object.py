from pico2d import *
import random

# Game object class here

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 300), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 590
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= 5

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)


def reset_world():
    global grass
    global team,Balls
    global world
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    Balls = [Ball() for i in range(20)]
    world += team
    world += Balls


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# 초기화 코드
open_canvas()

# 변수 초기화
running = True
world = []

# 게임 루프
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# 종료 코드
close_canvas()