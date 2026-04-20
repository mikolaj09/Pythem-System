import random
import functions
import level3

def level2(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i):
    print("Poziom 2")
    print()
    names0 = ["Czarnoksiężnik Chlewik", "Mag Schab", "Magik Zrazik", "Czarnoksiężnik Kotlecik"]
    names1 = ["Rozbójnik Kiełbaska", "Wojownik Chlewik", "Rycerz Ogromnego Gulaszu", "Mistrz Pulpecik"]
    t = 2
    print("Zostałeś teleportowany do Krainy Świńskich Gór.")
    print("W środku tej krainy znajduje się Zamek Komitetu Gulaszu.")
    print("Jednak, żeby wejść trzeba pokonać strażników...")
    lev = 10
    world = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 4, 5, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 2,
             1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 5, 1, 0, 0, 0, 0,15,16,15,16, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 0, 0, 0, 0, 0, 0,17,18,17,23, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 0, 0, 0, 0, 0, 0,18,19,22,23, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    functions.printworld(world)
    pl = 111
    ch = 9
    k = "None"
    end = 0
    while end == 0:
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

            if world[pl] == 19:
                print()
                print("Wchodzisz do Zamku Komitetu Rycerzy Gulaszu.")
                print("Lecz nagle strażnicy wyskakują z ukrycia, chwytają Cię i przyprowadzają Cię do oblicza Najwyższego Rycerza Gulaszu.")
                print("-Ha! Chciało się zamordować Króla! Nie, nie ma go tutaj, lecz przyprowadzę Cię do Króla, który orzeknie sąd - mówił Rycerz.")
                print()
                print("Wybierz:")
                print("     1. Ja chciałem tylko zgłosić skargę! Błota nie ma w Świńskim Hipermarkecie!")
                print("     2. Nic nie powiem.")
                k = input()
                if (k == '1'):
                    print("I jeszcze nas obrażasz! Zabrać Go do Króla - powiedział.")
                else:
                    print("Tym lepiej dla Mnie. Tymczasem przyprowadzę Cię do Króla - powiedział.")
                colosseum(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i)
                break

            if world[pl] == 5:
                if false == 0:
                    print("          Właściwości postaci:", names0[n],". Twoja moc wynosi:", power)
                    print()
                    print(char0[0], "   Siła:", str)
                    print(char1[0], "Życie:", hearts)
                    print(char2[0], " Obrona:", defen)
                    print(char3[0], "  Magia:", magic)
                elif false == 1:
                    print("          Właściwości postaci:", names1[n],". Twoja moc wynosi:", power)
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
                if world[pl] == 1 or world[pl] == 2 or world[pl] == 3 or world[pl] == 7 or world[pl] == 9 or world[pl] == 15 or world[pl] == 16 or world[pl] == 17 or world[pl] == 18 or world[pl] == 20 or world[pl] == 21 or world[pl] == 22 or world[pl] == 23:
                    pl = pl1
                    world[pl] = 4
                else:
                    world[pl] = 4
        world[pl] = 4
        time = functions.check3(world, 5)
        functions.printworld(world)

def colosseum(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i):
    print()
    print("Król orzekł karę. Będziesz walczyć na śmierć i życie z naljepszym gladiatorem Świnkiem!")
    print()
    t = 3
    names0 = ["Czarnoksiężnik Chlewik", "Mag Schab", "Magik Zrazik", "Czarnoksiężnik Kotlecik"]
    names1 = ["Rozbójnik Kiełbaska", "Wojownik Chlewik", "Rycerz Ogromnego Gulaszu", "Mistrz Pulpecik"]
    col = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
             1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2,
             1, 1, 0, 0, 0, 5, 0, 0, 0, 0, 1, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2,
             1, 1, 0, 0, 0, 4, 0, 0, 0, 0, 1, 1, 2,
             1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    fi = 1
    str1 = 30
    hearts1 = 50
    defen1 = 5
    magic1 = 0
    power1 = 85
    w = 1
    while w == 1:
        if false == 0:
            print("          Właściwości postaci:", names0[n],". Twoja moc wynosi:", power)
            print()
            print(char0[0], "   Siła:", str)
            print(char1[0], "Życie:", hearts)
            print(char2[0], " Obrona:", defen)
            print(char3[0], "  Magia:", magic)
        elif false == 1:
            print("          Właściwości postaci:", names1[n],". Twoja moc wynosi:", power)
            print()
            print(char0[1], "          Siła:", str)
            print(char1[1], "Życie:", hearts)
            print(char2[1], " Obrona:", defen)
            print(char3[1], "  Magia:", magic)
        functions.enemy(fi, char0, char1, char2, char3, str1, hearts1, defen1, magic1, str, hearts, defen,magic, power1)
        if functions.fight(col, fi, str1, hearts1, defen1, magic1, str, hearts, defen, magic, false, char0, char1, char2, char3, t) == 1:
            print("Przeszedłeś drugi poziom. Pozostał ostatni przed Tobą.")
            print()
            print("W nagrodę zyskujesz nowy poziom!")
            print()
            lev1 = functions.levelup(str, hearts, defen, magic, power)
            str = lev1[0]
            hearts = lev1[1]
            defen = lev1[2]
            magic = lev1[3]
            power = lev1[4]
            w = 0
            level3.level3(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i)
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