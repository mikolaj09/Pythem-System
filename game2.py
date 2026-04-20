import multiplayergame
import singleplayergame


def game(u, i):
    print()
    print("Witamy w grze ,,Kółko i Krzyżyk''")
    print()
    print("Wybierz: x/o")
    k = input()
    if k == 'x':
        t = 2
        e = 1
    else:
        t = 1
        e = 2
    print("Świetny wybór!")
    print()
    print("Wybierz teraz tryb:")
    print("     Singleplayer (1)")
    print("     Multiplayer (2)")
    k = input()
    if k == '2':
        multiplayergame.game(t, e)
    else:
        singleplayergame.game(u, i, t, e)