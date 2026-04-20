import random
import functions
import level2

def level1(str, hearts, defen, magic, power, false, char0, char1, char2, char3, n, u, i):
    names0 = ["Czarnoksiężnik Chlewik", "Mag Schab", "Magik Zrazik", "Czarnoksiężnik Kotlecik"]
    names1 = ["Rozbójnik Kiełbaska", "Wojownik Chlewik", "Rycerz Ogromnego Gulaszu", "Mistrz Pulpecik"]
    world0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
              1,11,12, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2,
              1,13,14, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2,
              1, 4, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2,
              1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2,
              1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 5, 10,2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
              0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2,
              0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2,
              0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2,
              0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 2,
              0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 2,
              0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 2,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]

    print()
    lev = -2
    print("Poszedłeś do Świńskiego Sklepu poszukując pewnego produktu bez którego żadna świnka nie może żyć. Tym artykułem jest Błotko")
    print("Niestety zauważasz jego brak, więc idziesz zgłosić skargę do Komitetu Rycerzy Gulaszu, który znajduje się w Krainie Świńskich Gór.")
    print()
    way = 0
    k = ''
    k1 = 'w'
    pl = 64
    ch = 9
    t = 1
    functions.printworld(world0)
    while way == 0:
        if k != '':
            k1 = k
        pl1 = pl
        k = input()
        if k == 'u':
            functions.printstat(str, hearts, defen, magic, power)
        else:
            world0[pl] = 0
            if k == '':
                if k1 == 'w':
                    pl -= 21
                if k1 == 's':
                    pl += 21
                if k1 == 'a':
                    pl -= 1
                if k1 == 'd':
                    pl += 1
            else:
                if k == 'w':
                    pl -= 21
                if k == 's':
                    pl += 21
                if k == 'a':
                    pl -= 1
                if k == 'd':
                    pl += 1

        if world0[pl] == 5:
            if false == 0:
                print("          Właściwości postaci:", names0[n], ". Twoja moc wynosi:", power)
                print()
                print(char0[0], "   Siła:", str)
                print(char1[0], "Życie:", hearts)
                print(char2[0], " Obrona:", defen)
                print(char3[0], "  Magia:", magic)
            elif false == 1:
                print("          łaściwości postaci:", names1[n], ". Twoja moc wynosi:", power)
                print()
                print(char0[1], "          Siła:", str)
                print(char1[1], "Życie:", hearts)
                print(char2[1], " Obrona:", defen)
                print(char3[1], "  Magia:", magic)

            att1 = functions.ai(lev)
            str1 = att1[0]
            hearts1 = att1[1]
            defen1 = att1[2]
            magic1 = att1[3]
            power1 = att1[4]
            fi = att1[5]
            functions.enemy(fi, char0, char1, char2, char3, str1, hearts1, defen1, magic1, str, hearts, defen,
                            magic, power1)

            battle = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 2,
                      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
            functions.htp()
            if functions.fight(battle, fi, str1, hearts1, defen1, magic1, str, hearts, defen, magic, false, char0,
                               char1, char2, char3, t) == 1:
                lev1 = functions.levelup(str, hearts, defen, magic, power)
                str = lev1[0]
                hearts = lev1[1]
                defen = lev1[2]
                magic = lev1[3]
                power = lev1[4]
            else:
                if ch > 0:
                    ch -= 1
                    print("Przegrałeś walkę. Ilość pozostałych szans:", ch)
                elif ch == 0:
                    print("Masz ostatnią szansę!")
                else:
                    print("Twój bohater został pokonany.")
                    print("Koniec gry!")
                    print()
                    return 0
        if world0[pl] == 1 or world0[pl] == 2 or world0[pl] == 3 or world0[pl] == 7 or world0[pl] == 9 or world0[pl] == 11 or world0[pl] == 12 or world0[pl] == 13 or world0[pl] == 14:
            pl = pl1
            world0[pl] = 4
        elif world0[pl] == 10:
            way = 1
        else:
            world0[pl] = 4
        world0[pl] = 4
        functions.printworld(world0)



    world = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
             1, 6, 6, 1, 0, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2,
             1, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 1, 2,
             1, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 4, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 5, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 1, 6, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    print()
    print("Wędrowałeś sobie po okolicy i nagle spotykasz Wielkiego Kapłana Wielkiej Świątyni Świnek,")
    print("który prosi Cię, żebyś pokonał okolicznych rozbójników ograbiających świątynię.")
    print("Obiecuje Ci przekazać część wiedzy i przenieść Cię do Krainy Świńskich Gór (do których podążałeś) za wykonanie tego zadania. Zgadzasz się i bierzesz się do pracy.")
    print()
    functions.printworld(world)
    pl = 134
    time = functions.check3(world, 5)
    lev = 0
    k = "None"
    end = 0
    while end == 0:
        t = 1
        if k != '':
            k1 = k
        pl1 = pl
        k = input()
        if k == 'u':
            functions.printstat(str, hearts, defen, magic, power)
            functions.printworld(world)
        else:
            world[pl] = 0
            if k == '':
                if k1 == 'w':
                    pl -= 22
                if k1 == 's':
                    pl += 22
                if k1 == 'a':
                    pl -= 1
                if k1 == 'd':
                    pl += 1
            else:
                if k == 'w':
                    pl -= 22
                if k == 's':
                    pl += 22
                if k == 'a':
                    pl -= 1
                if k == 'd':
                    pl += 1

            if world[pl] == 6:
                print()
                print("Odnalazłeś skrzynię ze skarbami. Wybierz skarb, który chcesz wziąć:")
                print("     1. 3 punkty ulepszeń)")
                print("     2. Dodatkowa szansa")
                print("     3. Kryształ teleportacji")
                k = input()
                if k == '1':
                    lev1 = functions.levelup(str, hearts, defen, magic, power)
                    str = lev1[0]
                    hearts = lev1[1]
                    defen = lev1[2]
                    magic = lev1[3]
                    power = lev1[4]
                if k == '2':
                    ch += 1
                    print("Dostałeś dodatkową szansę. Ilość pozostałych szans:", ch)
                if k == '3':
                    tel = random.randint(0, 461)
                    while world[tel] != 0:
                        tel = random.randint(0, 461)
                    world[pl] = 0
                    pl = tel
                    world[pl] = 4

            if world[pl] == 8:
                if time == 0:
                    print()
                    print("Wszedłeś do Wielkiej Świątyni Świnek.")
                    print(
                        "Pokonałeś wszystkich przeciwników, więc Wielki Kapłan Wielkiej Świątyni Świnek może Cię teleportować do Krainy Świńskich Gór.")
                    end = 1
                else:
                    print()
                    print("Wielki Kapłan Wielkiej Świątyni Świnek, nie chce Cię przenieść, ponieważ nie pokonałeś wszystkich przeciwników.")
                    print()

            if world[112] != 4:
                world[112] = 8

            if world[pl] == 5:
                if false == 0:
                    print("          Właściwości postaci:", names0[n],". Twoja moc wynosi:", power)
                    print()
                    print(char0[0], "   Siła:", str)
                    print(char1[0], "Życie:", hearts)
                    print(char2[0], " Obrona:", defen)
                    print(char3[0], "  Magia:", magic)
                elif false == 1:
                    print("          łaściwości postaci:", names1[n], ". Twoja moc wynosi:", power)
                    print()
                    print(char0[1], "          Siła:", str)
                    print(char1[1], "Życie:", hearts)
                    print(char2[1], " Obrona:", defen)
                    print(char3[1], "  Magia:", magic)

                att1 = functions.ai(lev)
                str1 = att1[0]
                hearts1 = att1[1]
                defen1 = att1[2]
                magic1 = att1[3]
                power1 = att1[4]
                fi = att1[5]
                functions.enemy(fi, char0, char1, char2, char3, str1, hearts1, defen1, magic1, str, hearts, defen,
                                magic, power1)

                battle = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 2,
                          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
                if functions.fight(battle, fi, str1, hearts1, defen1, magic1, str, hearts, defen, magic, false, char0,
                                   char1, char2, char3, t) == 1:
                    lev1 = functions.levelup(str, hearts, defen, magic, power)
                    str = lev1[0]
                    hearts = lev1[1]
                    defen = lev1[2]
                    magic = lev1[3]
                    power = lev1[4]
                else:
                    if ch > 0:
                        ch -= 1
                        print("Przegrałeś walkę. Ilość pozostałych szans:", ch)
                    elif ch == 0:
                        print("Masz ostatnią szansę!")
                    else:
                        print("Twój bohater został pokonany.")
                        print("Koniec gry!")
                        print()
                        return 0


            else:
                if world[pl] == 1 or world[pl] == 2 or world[pl] == 3 or world[pl] == 7 or world[pl] == 9:
                    pl = pl1
                    world[pl] = 4
                else:
                    world[pl] = 4
        world[pl] = 4
        time = functions.check3(world, 5)
        functions.printworld(world)

    print("Przeszedłeś pierwszy poziom. Pozostały Ci 2 poziomy.")
    print()
    print("W nagrodę zyskujesz nowy poziom!")
    print()

    lev1 = functions.levelup(str, hearts, defen, magic, power)
    str = lev1[0]
    hearts = lev1[1]
    defen = lev1[2]
    magic = lev1[3]
    power = lev1[4]
    level2.level2(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i)