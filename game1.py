import random
import functions
import level1


def game(u, i):
    print("Ostrzeżenie:")
    print("     Nie można wyłączyć gry podczas jej trwania, żeby z niej wyjść trzeba wygrać (lub przegrać).")
    print("     Czy chcesz przejść dalej: y/n")
    k = input()
    if k == 'y':
        ch = 9
        print()
        print("Witamy w Dungeons of Pigs")
        print("W Dungeons of Pigs poruszasz się następującymi znakami: w, s, a, d.")
        print("Wybierając postać, możesz zdecydować czy będziesz grać magiem czy wojownikiem.")
        print("Jeżeli grasz magiem możesz rzucać zaklęcia (m), a naciskając klawisz (t) teleportujesz się do losowo wybranego miejsca.")
        print("A jeśli wojownikiem, atakujesz (t), a klikając (f) kwiczysz i stajesz się przez 3 tury dwukrotnie potężniejszy w ataku i obronie.")
        print("Gdy klikniesz (u) wyświetli twoje umiejętności (nie zadziała podczas walki)")
        print()
        print("Wybierz swojego bohatera:")
        print()
        char0 = ["        /\ ", "/ \ ", "{ }"]
        char1 = ["<-> ___/  \___", "\ /  /\____/\ ", " |    |\/\/|"]
        char2 = [" |---['(..)']", " !---['(..)']", " |---['(..)']"]
        char3 = [" |    _|  |_", "      _|  |_", " |    _|  |_"]

        names0 = ["Czarnoksiężnik Chlewik", "Mag Schab", "Magik Zrazik", "Czarnoksiężnik Kotlecik"]
        names1 = ["Rozbójnik Kiełbaska", "Wojownik Chlewik", "Rycerz Ogromnego Gulaszu", "Mistrz Pulpecik"]
        n = random.randint(0, 3)

        print("          Właściwości postaci:", names0[n])
        print()
        print(char0[0], "   Siła: 0")
        print(char1[0], "Życie: 3")
        print(char2[0], " Obrona: 3")
        print(char3[0], "  Magia: 6")
        print()
        n = random.randint(0, 3)
        print("          Właściwości postaci:", names1[n])
        print()
        print(char0[1], "          Siła: 5")
        print(char1[1], "Życie: 4")
        print(char2[1], " Obrona: 3")
        print(char3[1], "  Magia: 0")
        print()
        print("Wojownik/Mag (w/m)")
        true = 0
        while true == 0:
            k = input()
            if k == "w":
                str = 5
                hearts = 4
                defen = 3
                magic = 0
                power = 12
                true = 1
                false = 1
            elif k == "m":
                str = 0
                hearts = 3
                defen = 3
                magic = 6
                power = 12
                true = 1
                false = 0
            else:
                print("Wojownik/Mag (w/m)")

        lev1 = functions.levelup(str, hearts, defen, magic, power)
        str = lev1[0]
        hearts = lev1[1]
        defen = lev1[2]
        magic = lev1[3]
        power = lev1[4]

        k = "None"
        level1.level1(str, hearts, defen, magic, power, false, char0, char1, char2, char3, n, u, i)