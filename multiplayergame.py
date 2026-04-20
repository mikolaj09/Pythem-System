import functions

def game(t, e):
    tab = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    functions.printworld1(tab)
    while True:
        if functions.check3(tab, 0) == 0:
            print("Remis!")
            print()
            return 0
        print("Gracz 1: ", end = '')
        try:
            k = int(input())
            while tab[k - 1] != 0:
                print("Błąd")
                k = int(input())
        except:
            print("Coś poszło nie tak")
            return 0
        tab[k - 1] = t
        functions.printworld1(tab)
        if functions.checkgame(tab, t, 1) == 0:
            return 0
        if functions.check3(tab, 0) == 0:
            print("Remis!")
            return 0
        print("Gracz 2: ", end = '')
        try:
            k = int(input())
            while tab[k - 1] != 0:
                print("Błąd")
                k = int(input())
        except:
            print("Coś poszło nie tak")
            return 0
        tab[k - 1] = e
        functions.printworld1(tab)
        if functions.checkgame(tab, e, 2) == 0:
            return 0