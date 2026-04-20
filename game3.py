import random

def game(u, i):
    print()
    print("Witamy w grze ,,Oblicz''")
    print()
    d = 100
    e = -100
    n = 0
    t = 0
    print("Ilość zadań:", end = ' ')
    try:
        z = int(input())
        while z > 0:
            c = random.randint(0, 5)
            if c == 0 or c == 1:
                d = 100
                e = -100
            elif c == 2 or c == 3:
                d = 20
                e = -20
            elif c == 5:
                d = 5
                e = 0
            else:
                d = 50
                e = 50
            a = random.randint(e, d)
            b = random.randint(e, d)
            if b == 0 and c == 3 or b == 0 and c == 4:
                b = 5
            if c == 0:
                print(a, '+', b, '=', end = ' ')
                k = int(input())
                if k == a + b:
                    t += 1
                while k != a + b:
                    print("Błąd!", a + b)
                    n += 1
                    print(a, '+', b, '=', end=' ')
                    k = int(input())
            if c == 1:
                print(a, '-', b, '=', end = ' ')
                k = int(input())
                if k == a - b:
                    t += 1
                while k != a - b:
                    n += 1
                    print("Błąd!", a - b)
                    print(a, '-', b, '=', end=' ')
                    k = int(input())
            if c == 2:
                print(a, '*', b, '=', end = ' ')
                k = int(input())
                if k == a * b:
                    t += 1
                while k != a * b:
                    n += 1
                    print("Błąd!", a * b)
                    print(a, '*', b, '=', end=' ')
                    k = int(input())
            if c == 3:
                print(a, ':', b, '=', end = ' ')
                k = int(input())
                if k == a // b:
                    t += 1
                while k != a // b:
                    n += 1
                    print("Błąd!", a // b)
                    print(a, ':', b, '=', end=' ')
                    k = int(input())
            if c == 4:
                print(a, '%', b, '=', end = ' ')
                k = int(input())
                if k == a % b:
                    t += 1
                while k != a % b:
                    n += 1
                    print("Błąd!", a % b)
                    print(a, '%', b, '=', end=' ')
                    k = int(input())
            if c == 5:
                print(a, '^', b, '=', end = ' ')
                k = int(input())
                if k == pow(a, b):
                    t += 1
                while k != pow(a, b):
                    n += 1
                    print("Błąd!", pow(a, b))
                    print(a, '^', b, '=', end=' ')
                    k = int(input())
            z -= 1
        print()
        print("Poprawne odpowiedzi:", t)
        print("Złe odpowiedzi:", n)
        print()
    except:
        print("Coś poszło nie tak")