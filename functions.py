import pygame
import random

def posenemy(u, i, t, e, tab):
    k = random.randint(1, 9)
    while tab[k - 1] != 0:
        k = random.randint(1, 9)
    tab[k - 1] = e
    return tab

def checkgame(tab, t, n):
    if tab[0] == t and tab[1] == t and tab[2] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[3] == t and tab[4] == t and tab[5] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[6] == t and tab[7] == t and tab[8] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[0] == t and tab[3] == t and tab[6] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[1] == t and tab[4] == t and tab[7] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[2] == t and tab[5] == t and tab[8] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[0] == t and tab[4] == t and tab[8] == t:
        print("Wygrał gracz", n)
        return 0
    if tab[2] == t and tab[4] == t and tab[6] == t:
        print("Wygrał gracz", n)
        return 0

def check(u, k):
    i = len(u) - 1
    while i >= 0:
        if u[i] == k:
            return i
        else:
            i -= 1
    if i == -1:
        return 'f'

def check2(u, k):
    i = len(u) - 1
    o = []
    while i >= 0:
        if u[i] == k:
            o.append(u[i + 1])
        else:
            i -= 1
    if len(o) == 0:
        return 0
    else:
        return o

def check3(u, k):
    i = len(u) - 1
    o = 0
    while i >= 0:
        if u[i] == k:
            o += 1
            return o
        i -= 1
    return o

def printworld1(world):
    s = 0
    i = 1
    n = 0
    while s < 9:
        if n == 3:
            n = 0
            print()
            print(end = '')
        if world[s] == 0:
            print(' ', i, ' ', sep = '' , end='')
        if world[s] == 1:
            print(" o ", sep = '' , end='')
        if world[s] == 2:
            print(" x ", sep = '' , end='')
        s += 1
        i += 1
        n += 1
    print()

def printworld(world):
    s = 0
    while True:
        if world[s] == 0:
            print("  ", end='')
        if world[s] == 1:
            print("+ ", end='')
        if world[s] == 2:
            print()
            print(end='')
        if world[s] == 4:
            print("o ", end='')
        if world[s] == 5:
            print("x ", end='')
        if world[s] == 6:
            print("? ", end='')
        if world[s] == 7:
            print("[^", end='')
        if world[s] == 8:
            print("@@", end='')
        if world[s] == 9:
            print("^]", end='')
        if world[s] == 10:
            print("# ", end='')
        if world[s] == 11:
            print("/^", end='')
        if world[s] == 12:
            print("\ ", end='')
        if world[s] == 13:
            print("[*", end='')
        if world[s] == 14:
            print("] ", end='')
        if world[s] == 15:
            print("/ ", end='')
        if world[s] == 16:
            print("\ ", end='')
        if world[s] == 17:
            print("|0", end='')
        if world[s] == 23:
            print("| ", end='')
        if world[s] == 18:
            print("|_", end='')
        if world[s] == 19:
            print("_#", end='')
        if world[s] == 22:
            print("__", end='')
        if world[s] == 3:
            break
        s += 1
    print()

def movenemy(battle, life, str,defen,hearts,magic,fi, char0, char1, char2, char3, str1, hearts1, defen1,magic1, pos, pl, kh):

    mv = random.randint(0, 1)
    if mv == 0:
        if fi == 1:
            if pos - 1 == pl or pos + 1 == pl or pos + 13 == pl or pos - 13 == pl:
                ca = random.randint(0, 2)
                if ca == 2:
                    if str1 // 2 + str1 > defen // 2:
                        life = life - str1 - (str1 // 2) + (defen // 2)
                    else:
                        life -= 1
                else:
                    if str1 > defen // 2:
                        life = life - str1 + (defen // 2)
                    else:
                        life -= 1
        else:
            ca = random.randint(0, 5)
            if ca != 5:
                if magic1 // 2 > defen // 2:
                    if pos - 1 == pl or pos + 1 == pl or pos + 13 == pl or pos - 13 == pl or pos - 2 == pl or pos + 2 == pl or pos + 26 == pl or pos + 26 == pl:
                        life = life - (magic1 // 2) + (defen // 2)
                else:
                    if pos - 1 == pl or pos + 1 == pl or pos + 13 == pl or pos - 13 == pl or pos - 2 == pl or pos + 2 == pl or pos + 26 == pl or pos + 26 == pl:
                        life -= 1
            else:
                r = random.randint(0, 129)
                while battle[r] == 1 or battle[r] == 2 or battle[r] == 3 or battle[r] == 4 or battle[r] == 5:
                    r = random.randint(0, 129)
                battle[pos] = 0
                pos = r
                battle[pos] = 4
    else:
        if fi == 1:
            pos1 = pos
            battle[pos] = 0
            if pl + 26 == pos or pl - 26 == pos or pl + 2 == pos or pl - 2 == pos or pl + 14 == pos or pl - 14 == pos or pl + 12 == pos or pl - 12 == pos:
                if pl + 26 == pos:
                    pos += 13

                if pl - 26 == pos:
                    pos -= 13

                elif pl + 2 == pos:
                    pos += 1

                elif pl - 2 == pos:
                    pos -= 1

                elif pl + 14 == pos:
                    pos += 13

                elif pl - 14 == pos:
                    pos -= 13

                elif + 12 == pos:
                    pos += 13

                elif pl - 12 == pos:
                    pos -= 13

                if battle[pos] == 1 or battle[pos] == 2 or battle[pos] == 3 or battle[pos] == 4:
                    pos = pos1
                    battle[pos] = 5
            else:

                way = random.randint(0, 3)
                if way == 0:
                    pos -= 13
                elif way == 1:
                    pos += 13
                elif way == 2:
                    pos -= 1
                else:
                    pos += 1

                if battle[pos] == 1 or battle[pos] == 2 or battle[pos] == 3 or battle[pos] == 4 or battle[pos] == 5:
                    pos = pos1

        else:
            ca = random.randint(0, 5)
            if ca != 5:
                if magic1 // 2 > defen // 2:
                    if pos - 1 == pl or pos + 1 == pl or pos + 13 == pl or pos - 13 == pl or pos - 2 == pl or pos + 2 == pl or pos + 26 == pl or pos + 26 == pl:
                        life = life - (magic1 // 2) + (defen // 2)
                else:
                    if pos - 1 == pl or pos + 1 == pl or pos + 13 == pl or pos - 13 == pl or pos - 2 == pl or pos + 2 == pl or pos + 26 == pl or pos + 26 == pl:
                        life -= 1
            else:
                r = random.randint(0, 129)
                while battle[r] == 1 or battle[r] == 2 or battle[r] == 3 or battle[r] == 4 or battle[r] == 5:
                    r = random.randint(0, 129)
                battle[pos] = 0
                pos = r
                battle[pos] = 4

    battle[pos] = 5
    remove = [battle, hearts, str1, hearts1, defen1, magic1, pos, life]
    return remove

def levelup(str, hearts, defen, magic, power):
    levup = 3
    while levup > 0:
        print("(s - siła, z - życie, o - obrona, m - magia)Masz", levup, "punkt/y ulepszeń, wybierz co chciałbyś ulepszyć:", end=' ')
        k = input()
        print()
        if k == "s":
            str += 1
            levup -= 1
            power += 1

        if k == "z":
            hearts += 1
            levup -= 1
            power += 1

        if k == "o":
            defen += 1
            levup -= 1
            power += 1

        if k == "m":
            magic += 1
            levup -= 1
            power += 1

    print()
    print("Siła:", str)
    print("Życie:", hearts)
    print("Obrona:", defen)
    print("Magia:", magic)
    print("Twoja moc wynosi:", power)
    print()

    lev = [str, hearts, defen, magic, power]
    return lev

def ai(lev):
    fi = random.randint(0, 1)

    if fi == 1:
        str1 = random.randint(1 + lev, 9 + lev)

        hearts1 = random.randint(1 + lev, 9 + lev)

        defen1 = random.randint(1 + lev, 9 + lev)

        magic1 = 0
    else:
        str1 = 0

        hearts1 = random.randint(1 + lev, 5 + lev )

        defen1 = random.randint(1 + lev, 4 + lev)

        magic1 = random.randint(1 + lev, 12 + lev)

    power1 = str1 + hearts1 + defen1 + magic1
    att = [str1, hearts1, defen1, magic1, power1, fi]
    return att

def enemy(fi, char0, char1, char2, char3, str1, hearts1, defen1, magic1, str, hearts, defen, magic, power1):
    names0 = ["Czarnoksiężnik Chlewik", "Mag Schab", "Magik Zrazik", "Czarnoksiężnik Kotlecik"]
    names1 = ["Rozbójnik Kiełbaska", "Wojownik Chlewik", "Rycerz Ogromnego Gulaszu", "Mistrz Pulpecik"]
    n = random.randint(0, 3)
    print()
    r1 = str - str1
    r2 = hearts - hearts1
    r3 = defen - defen1
    r4 = magic - magic1
    if fi == 0:
        print("          Właściwości postaci:", names0[n], ". Jego moc wynosi:", power1)
        print()
        print(char0[0], "   Siła:", str1, '|', r1)
        print(char1[0], "Życie:", hearts1, '|', r2)
        print(char2[0], " Obrona:", defen1, '|', r3)
        print(char3[0], "  Magia:", magic1, '|', r4)
    else:
        print("          Właściwości postaci:", names1[n], ". Jego moc wynosi:", power1)
        print()
        print(char0[1], "          Siła:", str1, '|', r1)
        print(char1[1], "Życie:", hearts1, '|', r2)
        print(char2[1], " Obrona:", defen1, '|', r3)
        print(char3[1], "  Magia:", magic1, '|', r4)

def fight(battle, fi, str1, hearts1, defen1, magic1, str, hearts, defen, magic, false, char0, char1, char2, char3, t):
    kh = []
    furry = 0
    pos = 31
    life = hearts * 2
    life1 = hearts1 * 2
    yes = 0
    print()
    if t == 1:
        print("Spotkałeś świnskiego rozbójnika")
    elif t == 2:
        print("Spotkałeś świnśkiego wojownika!")
    elif t == 3:
        print("Atakuję Cię gladiator Świnek")
    else:
        print("Atakuje Cię Król Chlewik VI")
    print()
    pas = life
    pas1 = life1
    print("Twoje życie: ", end='')
    while pas > 0:
        print('❤', end='')
        pas -= 1
    print()
    print("Życie przeciwnika: ", end='')
    while pas1 > 0:
        print('❤', end='')
        pas1 -= 1
    pl = 96
    print()
    k1 = 'w'
    fightime = 1
    while fightime == 1:
        en = pos
        pl1 = pl
        printworld(battle)
        k = input()
        if k == '':
            k = k1
        else:
            k1 = k
        battle[pl] = 0
        if k == 'w':
            pl -= 13
        if k == 's':
            pl += 13
        if k == 'a':
            pl -= 1
        if k == 'd':
            pl += 1
        if battle[pl] == 1 or battle[pl] == 2 or battle[pl] == 3 or battle[pl] == 5:
            pl = pl1
            battle[pl] = 4
        else:
            battle[pl] = 4
        if false == 0:
            if k == 'm':
                if magic // 2 > defen1 // 2:
                    if pl - 1 == en or pl + 1 == en or pl + 13 == en or pl - 13 == en or pl - 2 == en or pl + 2 == en or pl + 26 == en or pl - 26 == en:
                        life1 = life1 - (magic // 2) + (defen1 // 2)
                elif pl - 1 == en or pl + 1 == en or pl + 13 == en or pl - 13 == en or pl - 2 == en or pl + 2 == en or pl + 26 == en or pl - 26 == en:
                    life1 -= 1
            if k == 't':
                tel = random.randint(0, 129)
                while battle[tel] != 0:
                    tel = random.randint(0, 129)
                battle[pl] = 0
                pl = tel
                battle[pl] = 4
        if false == 1:
            if k == 't':
                if pl - 1 == en or pl + 1 == en or pl + 13 == en or pl - 13 == en:
                    at = random.randint(0, 1)
                    if at == 0:
                        if str1 // 2 + str1 >= defen // 2:
                            life1 = life1 - str - (str // 2)
                        else:
                            life1 -= 1
                    else:
                        if str1 >= defen // 2:
                            life1 = life1 - str + (defen1 // 2)
                        else:
                            life1 -= 1
            if k == 'f':
                defen = defen * 2
                str = str * 2
                furry = 3
                yes = 1
                print("Kwiiiiiik!!!")
        if furry > 0:
            furry -= 1
        if furry == 0 and yes == 1:
            defen = defen / 2
            str = str / 2
            yes = 0
        renemy = movenemy(battle, life, str,defen,hearts,magic,fi, char0, char1, char2, char3, str1, hearts1, defen1,
                          magic1, pos, pl, kh)
        battle = renemy[0]
        hearts = renemy[1]
        str1 = renemy[2]
        hearts1 = renemy[3]
        defen1 = renemy[4]
        magic1 = renemy[5]
        pos = renemy[6]
        life = renemy[7]
        pas = life
        pas1 = life1
        print("Twoje życie: ", end='')
        while pas > 0:
            print('❤', end='')
            pas -= 1
        print()
        print("Życie przeciwnika: ", end='')
        while pas1 > 0:
            print('❤', end='')
            pas1 -= 1
        print()
        if life1 <= 0:
            print("Wygrałeś.")
            fightime = 0
            return 1
        if life <= 0:
            print("Niestety przegrałeś.")
            fightime = 0
            return 0

def printstat(str, hearts, defen, magic, power):
    print()
    print("Siła:", str)
    print("Życie:", hearts)
    print("Obrona:", defen)
    print("Magia:", magic)
    print("Twoja moc wynosi:", power)
    print()

def htp():
    print("W Dungeons of Pigs poruszasz się następującymi znakami: w, s, a, d.")
    print("Wybierając postać, możesz zdecydować czy będziesz grać magiem czy wojownikiem.")
    print("Jeżeli grasz magiem możesz rzucać zaklęcia (m), a naciskając klawisz (t) teleportujesz się do losowo wybranego miejsca.")
    print("A jeśli wojownikiem, atakujesz (t), a klikając (f) kwiczysz i stajesz się przez 3 tury dwukrotnie potężniejszy w ataku i obronie.")
    print("Gdy klikniesz (u) wyświetli twoje umiejętności (nie zadziała podczas walki)")
    print()

def newWorld(world, pos, w, a, b, biom, c):
    k = 19
    l = len(world)
    while k > 0:
        k -= 1
        if pos > l:
            pos += 1
        if biom != 6:
            if k == 18:
                world.insert(l, 3)
            elif a > k > b:
                world.insert(l, 1)
            elif k >= a:
                world.insert(l, 2)
            else:
                world.insert(l, 0)
        else:
            if k == 18:
                world.insert(l, 3)
            elif c + 1 > k > c - 2:
                world.insert(l, 4)
            elif random.randint(9, 12) > k > random.randint(13, 15):
                world.insert(l, 1)
            elif k >= random.randint(13, 15):
                world.insert(l, 2)
            else:
                world.insert(l, 0)
        l = l - (w + 1)
    l = len(world) - 1
    w += 1
    return world, pos, w


def changeWorld(world, w):
    i = 0
    while i < len(world):
        try:
            if world[i + w + 1] == 0 and world[i] == 4:
                world[i + w + 1] = 4
                world[i] = 0
            if world[i + 1] == 0 and world[i] == 4:
                world[i + 1] = 4
            if world[i - 1] == 0 and world[i] == 4:
                world[i - 1] = 4
        except:
            print()
        i += 1
    return world


def digging(b1, world, pos, w, xMouse, yMouse, x, y, eq):
    if b1:
        try:
            if world[pos + (w + 1)] != 3 and world[pos + (w + 1)] != 0 and x <= xMouse <= x + 100 and yMouse >= y + 100:
                eq.append(world[pos + (w + 1)])
                world[pos + (w + 1)] = 0
            elif world[pos - w] != 3 and  world[pos - w] != 0 and xMouse >= x and yMouse <= y and yMouse >= y - 100:
                eq.append(world[pos - w])
                world[pos - w] = 0
            elif world[pos + 1] != 3 and  world[pos + 1] != 0 and xMouse >= x and yMouse >= y and yMouse <= y + 100:
                eq.append(world[pos + 1])
                world[pos + 1] = 0
            elif world[pos - 1] != 3 and  world[pos - 1] != 0 and xMouse <= x and yMouse >= y and yMouse <= y + 100:
                eq.append(world[pos - 1])
                world[pos - 1] = 0
            elif world[pos - (w + 2)] != 3 and world[pos - (w + 2)] != 0 and xMouse <= x and yMouse <= y and yMouse >= y - 100:
                eq.append(world[pos - (w + 2)])
                world[pos - (w + 2)] = 0
            elif world[pos - (w + w + 2)] != 3 and  world[pos - (w + w + 2)] != 0 and xMouse >= x and xMouse <= x + 100 and yMouse <= y:
                eq.append(world[pos - (w + w + 2)])
                world[pos - (w + w + 2)] = 0
            elif world[pos - (w + w + 1)] != 3 and  world[pos - (w + w + 1)] != 0 and xMouse >= x and yMouse <= y - 100 and yMouse >= y - 200:
                eq.append(world[pos - (w + w + 1)])
                world[pos - (w + w + 1)] = 0
            elif world[pos - (w + w + 3)] != 3 and  world[pos - (w + w + 3)] != 0 and xMouse <= x and yMouse <= y - 100 and yMouse >= y - 200:
                eq.append(world[pos - (w + w + 3)])
                world[pos - (w + w + 3)] = 0
            elif world[pos + w] != 3 and  world[pos + w] != 0 and xMouse <= x and yMouse >= y + 100 and yMouse <= y + 200:
                eq.append(world[pos + w])
                world[pos + w] = 0
            elif world[pos + w + 2] != 3 and  world[pos + w + 2] != 0 and xMouse >= x and yMouse >= y + 100 and yMouse <= y + 200:
                eq.append(world[pos + w + 2])
                world[pos + w + 2] = 0
        except:
            print(Exception)
    return [world, eq]

def building(b3, newBlock, world, eq, pos, w, xMouse, yMouse, x, y):
    if b3:
        try:
            eq.index(newBlock)
            if (world[pos + w + 1] == 0 or world[pos + w + 1] == 4) and xMouse >= x - 100 and xMouse <= x + 100 and yMouse >= y + 100:
                world[pos + w + 1] = newBlock
                eq.remove(newBlock)
            elif (world[pos - w] == 0 or world[pos - w] == 4) and xMouse >= x and yMouse <= y and yMouse >= y - 100:
                world[pos - w] = newBlock
                eq.remove(newBlock)
            elif (world[pos + 1] == 0 or world[pos + 1] == 4) and xMouse >= x and yMouse >= y and yMouse <= y + 100:
                world[pos + 1] = newBlock
                eq.remove(newBlock)
            elif (world[pos - 1] == 0 or world[pos - 1] == 4) and xMouse <= x and yMouse >= y and yMouse <= y + 100:
                world[pos - 1] = newBlock
                eq.remove(newBlock)
            elif (world[pos - (w + 2)] == 0 or world[pos - (w + 2)] == 4) and xMouse <= x and yMouse <= y and yMouse >= y - 100:
                world[pos - (w + 2)] = newBlock
                eq.remove(newBlock)
            elif (world[pos - (w + w + 2)] == 0 or world[pos - (w + w + 2)] == 4) and xMouse >= x and xMouse <= x + 100 and yMouse <= y:
                world[pos - (w + w + 2)] = newBlock
                eq.remove(newBlock)
            elif (world[pos - (w + w + 1)] == 0 or world[pos - (w + w + 1)] == 4) and xMouse >= x and yMouse <= y - 100 and yMouse >= y - 200:
                world[pos - (w + w + 1)] = newBlock
                eq.remove(newBlock)
            elif (world[pos - (w + w + 3)] == 0 or world[pos - (w + w + 1)] == 4) and xMouse <= x and yMouse <= y - 100 and yMouse >= y - 200:
                world[pos - (w + w + 3)] = newBlock
                eq.remove(newBlock)
            elif (world[pos + w] == 0 or world[pos + w] == 4) and xMouse <= x and yMouse >= y + 100 and yMouse <= y + 200:
                world[pos + w] = newBlock
                eq.remove(newBlock)
            elif (world[pos + w + 2] == 0 or world[pos + w + 2] == 4) and xMouse >= x + 100 and yMouse >= y + 100:
                world[pos + w + 2] = newBlock
                eq.remove(newBlock)
        except:
            print(Exception)
    return [world, eq]

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)