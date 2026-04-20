import pygame as py
import random
import functions

def game(u, i):
    py.init()
    flags = py.RESIZABLE
    win = py.display.set_mode((1000, 1000), flags)
    py.display.set_caption("The Digcraft 2D")
    eq = []
    x = 400
    y = 500
    x2 = 0
    y2 = 0
    w = 9
    day = 1
    biom = random.randint(0, 1)
    long = 40
    world = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             3, 0, 1, 4, 1, 0, 0, 0, 0, 0,
             3, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             3, 2, 2, 2, 1, 2, 1, 1, 1, 1,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 2, 2, 2, 0, 0, 0, 2, 2, 2,
             3, 2, 2, 2, 0, 0, 0, 0, 2, 2,
             3, 2, 2, 2, 2, 4, 4, 4, 2, 2,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    width = 80
    height = 180
    vel = 100
    g = 100
    run = True
    pos = 54
    sunX = 0
    sunY = 1000
    timeJump = 0
    newBlock = 1
    newWorld = 10
    b = True
    new1 = random.randint(8, 10)
    new3 = random.randint(-1, 1)
    o = 2
    h = random.randint(9, 11)
    while run:
        if long == 0:
            h = random.randint(9, 11)
            biom = random.randint(0, 6)
            long = 40
        new2 = new1 - random.randint(2, 3)
        if o == 0:
            new3 = random.randint(-1, 1)
            o = 2
        else:
            new3 += random.randint(-1, 1)
            o -= 1
        if b:
            while newWorld > 0:
                a = functions.newWorld(world, pos, w, new1 - new3, new2 - new3, biom, h)
                world = a[0]
                pos = a[1]
                w = a[2]
                newWorld -= 1
            b = False
        posMouse = py.mouse.get_pos()
        xMouse = posMouse[0]
        yMouse = posMouse[1]
        mouse = py.mouse.get_pressed()
        b1 = mouse[0]
        b3 = mouse[2]
        py.time.delay(100)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys = py.key.get_pressed()

        if keys[py.K_1]:
            newBlock = 1

        if keys[py.K_2]:
            newBlock = 2

        if keys[py.K_LEFT]:
            if (world[pos - 1] == 0 and world[pos - (w + 2)] == 0) or world[pos - 1] == 4 and (world[pos - (w + 2)] == 4 or world[pos - (w + 2)] == 0):
                pos -= 1
                x2 += vel

        if keys[py.K_RIGHT]:
            if world[pos + 1] == 0 and world[pos - w] == 0 or world[pos + 1] == 4 and (world[pos - w] == 4 or world[pos - w] == 0):
                pos += 1
                x2 -= vel

        if keys[py.K_UP] and world[pos + (w + 1)] != 0:
            if world[pos] == 0:
                timeJump = 1
            elif world[pos] == 4 and (world[pos - (w + 1)] == 4 or world[pos - (w + 1)] == 0) and (world[pos - ((w + 1) * 2)] == 4 or world[pos - ((w + 1) * 2)] == 0):
                pos -= ((w + 1) * 2)
                y2 += 200

        if world[pos + 15] == 3:
            a = functions.newWorld(world, pos, w, new1 - new3, new2 - new3, biom, h)
            world = a[0]
            pos = a[1]
            w = a[2]

        if timeJump > 0:
            if world[pos - ((w + 1) * 2)] == 0:
                pos -= ((w + 1) * 2)
                y2 += 200
                timeJump = 0

        if world[pos + w + 1] == 0 or world[pos + w + 1] == 4:
            y2 -= g
            pos += (w + 1)

        if keys[py.K_ESCAPE]:
            run = False
        i = 0
        x1 = x2
        y1 = y2
        if day == 1:
            win.fill((0, 120, 220))
        else:
            win.fill((10, 10, 50))
        if sunX <= 640:
            sunX += 1
            sunY -= 1.5
            sun = 0
        elif sunX >= 640 and sunX <= 1280:
            sunX += 1
        else:
            sunY += 1.5
            sunX += 1
        if sunY >= 1000:
            sunX = 0
            sunY = 1000
            if day == 1:
                day = 0
            else:
                day = 1
        if day == 1:
            py.draw.rect(win, (250, 230, 0), (sunX, sunY, 200, 200))
            functions.draw_rect_alpha(win, (250, 230, 0, 200), (sunX - 10, sunY - 10, 220, 220))
            functions.draw_rect_alpha(win, (250, 230, 0, 150), (sunX - 20, sunY - 20, 240, 240))
        else:
            py.draw.rect(win, (150, 150, 150), (sunX, sunY, 150, 150))
            functions.draw_rect_alpha(win, (150, 150, 150, 100), (sunX - 20, sunY - 20, 190, 190))
        if y >= 900:
            run = False
        py.draw.rect(win, (255, 0, 0), (x + 10, y - 80, width, height))
        e = 0
        world = functions.changeWorld(world, w)
        while i < len(world):
            if world[i] == 1:
                py.draw.rect(win, (110, 40, 0), (x1, y1, 100, 100))
                if world[i - w - 1] == 0:
                    py.draw.rect(win, (0, 200, 0), (x1, y1, 100, 10))
            elif world[i] == 2:
                py.draw.rect(win, (125, 125, 125), (x1, y1, 100, 100))
            elif world[i] == 3:
                py.draw.rect(win, (50, 50, 50), (x1, y1, 100, 100))
            elif world[i] == 4:
                functions.draw_rect_alpha(win, (50, 50, 250, 230), (x1, y1 + 10, 100, 90))
                if world[i - w - 1] == 4 or world[i - w] == 4 or world[i - w - 2] == 4:
                    functions.draw_rect_alpha(win, (50, 50, 250, 230), (x1, y1, 100, 10))
            x3 = xMouse % 100
            y3 = yMouse % 100
            if world[pos - w] != 3 and world[pos + (w + 1)] != 0 and xMouse >= x and xMouse <= x + 100 and yMouse >= y + 100 and yMouse <= y + 200:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos - w] != 3 and world[pos - w] != 0 and xMouse >= x + 100 and xMouse <= x + 200 and yMouse <= y and yMouse >= y - 100:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos + 1] != 3 and world[pos + 1] != 0 and xMouse >= x + 100 and xMouse <= x + 200 and yMouse >= y and yMouse <= y + 100:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos - 1] != 3 and world[pos - 1] != 0 and xMouse <= x and xMouse >= x - 100 and yMouse >= y and yMouse <= y + 100:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos - (w + 2)] != 3 and world[pos - (w + 2)] != 0 and xMouse <= x and xMouse >= x - 100 and yMouse <= y and yMouse >= y - 100:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos - (w + w + 1)] != 3 and  world[pos - (w + w + 1)] != 0 and xMouse >= x and xMouse <= x + 200 and yMouse <= y - 100 and yMouse >= y - 200:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos - (w + w + 3)] != 3 and world[pos - (w + w + 3)] != 0 and xMouse <= x and xMouse >= x - 100 and yMouse <= y - 100 and yMouse >= y - 200:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos + w] != 3 and world[pos + w] != 0 and xMouse <= x and xMouse >= x - 100 and yMouse >= y + 100 and yMouse <= y + 200:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            elif world[pos + w + 2] != 3 and world[pos + w + 2] != 0 and xMouse >= x and xMouse <= x + 200 and yMouse >= y + 100 and yMouse <= y + 200:
                py.draw.rect(win, (255, 255, 255), (xMouse - x3, yMouse - y3, 100, 100))

            if e == w:
                e = -1
                y1 += 100
                x1 = x2 - 100
            x1 += 100
            i += 1
            e += 1
        dig = functions.digging(b1, world, pos, w, xMouse, yMouse, x, y, eq)
        world = dig[0]
        eq = dig[1]

        build = functions.building(b3, newBlock, world, eq, pos, w, xMouse, yMouse, x, y)
        world = build[0]
        eq = build[1]
        long -= 1
        py.display.update()

    py.quit()