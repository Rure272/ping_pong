from pygame import *
from random import randint
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
FPS = 60
x1 = 10
y1 = 5
x2 = 640
y2 = 5
w1 = 50
h1 = 200
w_ball = 75
h_ball = 75
y_ball = WIN_H / 2
x_ball = (WIN_W - w_ball) / 2
step = 5
RED = (255, 0, 0)

font.init()
title_font = font.SysFont('arial', 35)
lost1 = title_font.render('Проиграл игрок №1', True, RED)
lost2 = title_font.render('Проиграл игрок №2', True, RED)
window = display.set_mode((WIN_W, WIN_H))

clock = time.Clock()


display.set_caption("пинг-понг")

background = transform.scale(
    image.load("grey.jpg"),
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

    def update(self, up, down):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 5:
            self.rect.y -= step
        if keys_pressed[down] and self.rect.y < WIN_H - self.rect.h:
            self.rect.y += step


class Enemy(Player):
    def __init__(self, img, x, y, w, h, speed = 3):
        super().__init__(img, x, y, w, h)
        self.speed_y = speed
        self.speed_x = speed
    def update(self):
        if self.rect.y <= 0 or self.rect.y >= WIN_H - self.rect.h:
            self.speed_y *= -1
        self.rect.y += self.speed_y
        if self.rect.x <= 0 or self.rect.x >= WIN_W - self.rect.w:
            self.speed_x *= -1
        self.rect.x += self.speed_x


player1 = Player('rb_noobb.png', x1, y1, w1, h1)
player2 = Player('rb_noobb.png', x2, y2, w1, h1)
ball = Enemy('roblox.jpg', x_ball, y_ball, w_ball, h_ball)


finish = False
game = True
while game:
    if not finish:       
        window.blit(background,(0, 0))
        player1.draw(window)
        player1.update(K_w, K_s)
        player2.draw(window)
        player2.update(K_UP, K_DOWN)


        ball.draw(window)
        ball.update()
        if sprite.collide_rect(player1, ball):
            ball.speed_x *= -1
        if sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
        if ball.rect.x <= 0:
            window.blit(lost1, (200, 200))
            display.update()
            finish = True
        if ball.rect.x >= WIN_W - ball.rect.w:
            window.blit(lost2, (200, 200))
            display.update()
            finish = True        
    else:
        ball.kill()
        time.delay(3000)
        finish = False
        ball = Enemy('roblox.jpg', x_ball, y_ball, w_ball, h_ball)


    for e in event.get():

        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
