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


class s_Ball:
    def __init__(self):

        self.x, self.y = random.randint(0, 800), 590
        self.image = load_image('ball21x21.png')

    def update(self):
        global speed
        speed = random.randint(-15, -1)
        if self.y >= 65:
            self.y += speed
            if self.y <= 65:
                self.y = 65
    def draw(self):

       self.image.draw(self.x,self.y)


class b_Ball:
    def __init__(self):

        self.x, self.y = random.randint(0, 800), 590
        self.image = load_image('ball41x41.png')


    def update(self):
        global speed
        speed = random.randint(-15, -1)
        if self.y >= 75:
            self.y += speed
            if self.y <= 75:
                self.y = 75

    def draw(self):
     self.image.draw(self.x,self.y)


def reset_world():
    global grass
    global team, small_Balls, big_Balls
    global world
    ball_size_num = random.randint(0,20)
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    small_Balls = [s_Ball() for i in range(ball_size_num)]
    big_Balls = [b_Ball() for i in range(20-ball_size_num)]
    world += team
    world += small_Balls
    world += big_Balls


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
