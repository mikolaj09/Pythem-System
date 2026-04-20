import pygame as py
import random


def game(u, i):
    x = 490
    y = 900
    run = True
    x2 = 450
    vel_y = -0.7
    vel_x = -0.5
    py.init()
    win = py.display.set_mode((1000, 1000))
    py.display.set_caption("The Ball (Single player)")
    if random.randint(0, 1) == 1:
        vel_x = vel_x * -1
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            x2 -= 1
        if keys[py.K_RIGHT]:
            x2 += 1
        x3 = x
        if keys[py.K_ESCAPE]:
            break
        x += vel_x
        y += vel_y
        if y > 990 and x2 - 50 < x <= x2 + 50:
            y = 980
            vel_y = vel_y * -1
        elif y < 10 and x >= x3 - 50 <= x <= x3 + 50:
            y = 10
            vel_y = vel_y * -1
        elif y > 990:
            print("Gracz 2 wygrał")
            break
        elif y < 0:
            print("Gracz 1 wygrał")
            break
        if x >= 990:
            x = 990
            vel_x = vel_x * -1
        if x <= 0:
            x = 0
            vel_x = vel_x * -1
        if x2 <= 50:
            x2 = 50
        elif x2 >= 950:
            x2 = 950
        if x3 <= 50:
            x3 = 50
        elif x3 >= 950:
            x3 = 950
        win.fill((0, 0, 0))
        py.draw.rect(win, (255, 255, 255), (x, y, 10, 10))
        py.draw.rect(win, (255, 255, 255), (x2 - 50, 990, 100, 10))
        py.draw.rect(win, (255, 255, 255), (x3 - 50, 0, 100, 10))
        py.display.update()
    py.quit()