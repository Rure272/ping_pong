from pygame import *

# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
FPS = 60

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

# игровой цикл
game = True
while game:
    # отобразить картинку фона
    window.blit(background,(0, 0))

    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)