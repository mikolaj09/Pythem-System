import functions

def game(u, i, t, e):
    tab = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    functions.printworld1(tab)
    while True:
        print("Gracz 1: ", end = '')
        try:
            k = int(input())
            while tab[k - 1] != 0:
                print("Błąd")
                k = int(input())
        except:
            print("Coś poszło nie tak.")
            return 0
        tab[k - 1] = t
        if functions.checkgame(tab, t, 1) == 0:
            functions.printworld1(tab)
            return 0
        tab = functions.posenemy(u, i, t, e, tab)
        functions.printworld1(tab)
        if functions.checkgame(tab, e, 2) == 0:
            return 0
