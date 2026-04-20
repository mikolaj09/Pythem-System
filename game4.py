import random

def game(u, i):
    try:
        print("Witamy w Guess the number!")
        print()
        print("Wybierz tryb:")
        print("     1. Ty zgadujesz")
        print("     2. Komputer zgaduje")
        k = input()
        if k == '1':
            n = random.randint(0, 100)
            while True:
                try:
                    m = int(input())
                    if m == n:
                        print("Brawo zgadłeś!")
                        break
                    elif m < n:
                        print("Za mało")
                    else:
                        print("Za dużo")
                except:
                    print("Coś poszło nie tak")
        else:
            f = 0
            e = 100
            print("Wymyśl jakąś liczbę...")
            while True:
                n = random.randint(f, e)
                print("Czy to twoja liczba:", n, "(y/n)")
                k = input()
                if k == 'y':
                    print("Zgadłem!")
                    break
                else:
                    print("Za dużo, czy za mało (d/m)")
                    k = input()
                    if k == 'd':
                        e = n - 1
                    else:
                        f = n + 1
        print("Czy chcesz jeszcze zagrać? (y/n)")
        k = input()
        if k == 'y':
            game(u, i)
    except:
        print("Coś poszło nie tak")