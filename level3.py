import functions
import endgame

def level3(str, hearts, defen, magic, power, false, char0, char1, char2, char3, ch, n, u, i):
    print()
    print("Poziom 3")
    print()
    print("Król nie mogąc znieść Twojej wygranej ogłasza, że oszukiwałeś i  będzie walczyć przeciwko Tobie na arenie.")

    print()
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
    w = 1
    str1 = 40
    hearts1 = 50
    defen1 = 10
    magic1 = 0
    power1 = 100
    while w == 1:
        if false == 0:
            print("          Właściwości postaci:", names0[n], ". Twoja moc wynosi:", power)
            print()
            print(char0[0], "   Siła:", str)
            print(char1[0], "Życie:", hearts)
            print(char2[0], " Obrona:", defen)
            print(char3[0], "  Magia:", magic)
        elif false == 1:
            print("          Właściwości postaci:", names1[n], ". Twoja moc wynosi:", power)
            print()
            print(char0[1], "          Siła:", str)
            print(char1[1], "Życie:", hearts)
            print(char2[1], " Obrona:", defen)
            print(char3[1], "  Magia:", magic)

        print()
        print("          Właściwości postaci:", "Król Chlewik VI", ". Jego moc wynosi:", power1)
        print()
        print(char0[2], "          Siła:", str1)
        print(char1[2], "Życie:", hearts1)
        print(char2[2], " Obrona:", defen1)
        print(char3[2], "  Magia:", magic1)
        if functions.fight(col, 1, str1, hearts1, defen1, magic1, str, hearts, defen, magic, false, char0, char1, char2, char3, 4) == 1:
            w = 0
            score = str + defen + hearts + magic + power + (ch * 10)
            endgame.endgame(score, u, i)
        else:
            ch -= 1
            if ch > 0:
                print("Przegrałeś walkę. Ilość pozostałych szans:", ch)
            elif ch == 0:
                print("Masz ostatnią szansę!")
            else:
                print("Twój bohater został pokonany.")
                print("Koniec gry!")
                print()
                return 0