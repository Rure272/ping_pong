from pygame import *
from random import randint
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
FPS = 60
x1 = 10
y1 = 10
x2 = 640
y2 = 10
w1 = 50
h1 = 200
w_ball = 75
h_ball = 75
y_ball = WIN_H / 2
x_ball = (WIN_W - w_ball) / 2
step = 5
# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("пинг-понг")

# задать картинку фона такого же размера, как размер окна
background = transform.scale(
    image.load("grey.jpg"),
    # здесь - размеры картинки
    (WIN_W, WIN_H)
)

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed = step, hp =3):
        super().__init__(img, x, y, w, h)
        self.speed = speed

    def update(self, left, right):
        keys_pressed = key.get_pressed()
        if keys_pressed[left] and self.rect.x > 5:
            self.rect.x -= step
        if keys_pressed[right] and self.rect.x < WIN_W - size:
            self.rect.x += step


class Enemy(Player):
    def __init__(self, img, x, y, w, h):
        super().__init__(img, x, y, w, h)

    
    def update(self):
        self.rect.y += self.speed



player1 = Player('rb_noobb.png', x1, y1, w1, h1)
player2 = Player('rb_noobb.png', x2, y2, w1, h1)
ball = Enemy('roblox.jpg', x_ball, y_ball, w_ball, h_ball)
game = True
while game:
    window.blit(background,(0, 0))
    player1.draw(window)
    player2.draw(window)
    ball.draw(window)

    for e in event.get():

        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
