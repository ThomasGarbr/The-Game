import pygame
import random
import math

pygame.init()  # настройка
win = pygame.display.set_mode((900, 900))  # размеры окна

pygame.display.set_caption("jew, old, cool jew")  # название окна


def center_origin(screen, p):
    return p[0] + screen.get_width() // 2, p[1] + screen.get_height() // 2

def turn(p, angle):
    rad_angle = math.radians(angle)
    r = pow(pow(p[0], 2) + pow(p[1], 2), 1 / 2)
    point = (r * math.cos(rad_angle), r * math.sin(rad_angle))
    return point[0], point[1]

class Pol(object):
    def __init__(self, x1, y1, x2, y2, r, g, b, a):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.r = r
        self.b = b
        self.g = g
        self.a = a
objs = list()
for i in range(10):
    objs.append(
        Pol(0, 0, 0, 0, 0, 0, 0, 0))
color = (0, 0, 0)
i = 0
angle = 45
run = True

while run:
    pygame.time.delay(150)  # скорость обновления окна

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # события ввода
            run = False  # Основной выход
    objs.append(
        Pol(0, 0, 0, 0, 0, 0, 0, 0))
    angle = angle+5
    objs.insert(0,
                Pol(25,
                    25,
                    25,
                    25,
                    random.randint(100, 200),
                    random.randint(100, 200),
                    random.randint(100, 200),
                    angle))
    for i in range(10):
        objs[10-i].r = objs[9-i].r
        objs[10-i].b = objs[9-i].b
        objs[10-i].g = objs[9-i].g
        objs[10-i].a = objs[9-i].a
    objs.pop(0)
    objs.pop(10)


    for i in range(9):
        x1_y1 = (5 + 5 * i * i, 5 + 5 * i * i)
        x2_y2 = (5 + 5 * (i + 1) * (i + 1), 5 + 5 * (i + 1) * (i + 1))

        pygame.draw.polygon(win, (objs[i].r, objs[i].g, objs[i].b),
                            [center_origin(win, (turn(x1_y1, objs[i].a + 5)[0], turn(x1_y1, objs[i].a + 5))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a)[0], turn(x2_y2, objs[i].a))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 90)[0], turn(x2_y2, objs[i].a - 90))[1]),
                             center_origin(win, (turn(x1_y1, objs[i].a - 90)[0], turn(x1_y1, objs[i].a - 90))[1])])
        pygame.draw.polygon(win, (objs[i].r, objs[i].g, objs[i].b),
                            [center_origin(win, (turn(x1_y1, objs[i].a - 85)[0], turn(x1_y1, objs[i].a - 85))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 90)[0], turn(x2_y2, objs[i].a - 90))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 180)[0], turn(x2_y2, objs[i].a - 180))[1]),
                             center_origin(win, (turn(x1_y1, objs[i].a - 180)[0], turn(x1_y1, objs[i].a - 180))[1])])
        pygame.draw.polygon(win, (objs[i].r, objs[i].g, objs[i].b),
                            [center_origin(win, (turn(x1_y1, objs[i].a - 175)[0], turn(x1_y1, objs[i].a - 175))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 180)[0], turn(x2_y2, objs[i].a - 180))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 270)[0], turn(x2_y2, objs[i].a - 270))[1]),
                             center_origin(win, (turn(x1_y1, objs[i].a - 270)[0], turn(x1_y1, objs[i].a - 270))[1])])
        pygame.draw.polygon(win, (objs[i].r, objs[i].g, objs[i].b),
                            [center_origin(win, (turn(x1_y1, objs[i].a - 265)[0], turn(x1_y1, objs[i].a - 265))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 270)[0], turn(x2_y2, objs[i].a - 270))[1]),
                             center_origin(win, (turn(x2_y2, objs[i].a - 360)[0], turn(x2_y2, objs[i].a - 360))[1]),
                             center_origin(win, (turn(x1_y1, objs[i].a - 360)[0], turn(x1_y1, objs[i].a - 360))[1])])

    pygame.display.update()
    win.fill(color)