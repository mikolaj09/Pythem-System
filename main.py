import random
import functions
import datetime
import help
import game1
import game2
import game3
import game4
import game5
import game6
import game7


# utworzony w piątek, 7 października 2022, 14:22:58

print()
print("Witamy w Pythem, wersji oficjalnej!")
print("Tylko w wersji konsolowej!")
print()

u = []
p = []


print("Wpisz swoje imię: ", end='')
k = input()
while k == '':
    print("Błąd")
    print("Wpisz swoje imię: ", end='')
    k = input()
u.append(k)
print("Wpisz swoje hasło: ", end='')
k = input()
while k == '':
    print("Błąd")
    print("Wpisz swoje hasło: ", end='')
    k = input()
p.append(k)
i = 0
txt = []
chat = []
pyt = []

while True:
    k = ''
    z = input()
    if z == "useradd":
        print("Wpisz hasło użytkownika ", u[i], ": ", sep = '', end = '')
        k = input()
        if k == p[i]:
            print("Wpisz nazwę nowego użytkownika: ", end = '')
            k = input()
            while functions.check3(u, k) != 0:
                print("Błąd! Użytkownik już istnieje!")
                print("Wpisz nazwę nowego użytkownika: ", end='')
                k = input()
            u.append(k)
            print("Wpisz hasło użytkownika ", k, ": ", sep='', end='')
            k = input()
            p.append(k)
            print("Pomyślnie utworzono konto")
        else:
            print("Błędne hasło!")

    elif z == "time":
        print(datetime.datetime.now())

    elif z == "log":
        print("Podaj nazwę użytkownika: ", end='')
        k = input()
        t = functions.check(u, k)
        if t != 'f':
            j = t
            print("Wpisz hasło użytkownika ", u[j], ": ", sep = '', end = '')
            k = input()
            if k == p[j]:
                print("Pomyślnie zalogowano na konto:", u[j])
                i = j
            else:
                print("Błędne hasło!")
        else:
            print("Nie ma takiego użytkownika")

    elif z == "whoami":
        print(u[i])

    elif z == "change_password":
        print("Wpisz hasło użytkownika", u[i], ": ", sep='', end='')
        k = input()
        if k == p[i]:
            print("Wpisz nowe hasło: ", end='')
            k = input()
            p[i] = k
            print("Pomyślnie zmieniono hasło")
        else:
            print("Błędne hasło!")

    elif z == "change_username":
        print("Wpisz hasło użytkownika ", u[i], ": ", sep='', end='')
        k = input()
        if k == p[i]:
            print("Wpisz nową nazwę: ", end='')
            k = input()
            u[i] = k
            print("Pomyślnie zmieniono nazwę")
        else:
            print("Błędne hasło!")

    elif z == "games":
        print("Wybierz:")
        print("     1. Dungeons of Pigs")
        print("     2. Kółko i krzyżyk")
        print("     3. Oblicz")
        print("     4. Guess the number")
        print("     5. The Ball (Single player)")
        print("     6. The Ball (Multiplayer)")
        print("     7. The Digcraft 2D")
        k = input()
        if k == '1':
            game1.game(u, i)
        elif k == '2':
            game2.game(u, i)
        elif k == '3':
            game3.game(u, i)
        elif k == '4':
            game4.game(u, i)
        elif k == '5':
            game5.game(u, i)
        elif k == '6':
            game6.game(u, i)
        elif k == '7':
            game7.game(u, i)

    elif z == "print_users":
        a = 0
        while a < len(u):
            print(u[a])
            a += 1

    elif z == "deluser":
        print("Podaj nazwę użytkownika: ", end='')
        k1 = input()
        if k1 != u[i]:
            if functions.check3(u, k1) == 0:
                print("Błąd! Użytkownik nie istnieje!")
                continue
            print("Wpisz hasło użytkownika ", k1, ": ", sep='', end='')
            k2 = input()
            if functions.check(p, k2) != 'f':
                print("Czy jesteś pewien? (y/n)")
                k = input()
                if k == 'y':
                    j = 0
                    while j < len(u):
                        if u[j] == k1:
                            break
                        j += 1
                    g = 0
                    while g < len(chat):
                        if chat[g] == u[j]:
                            chat[g] = ''
                        g += 1
                    j = 0
                    # odbiorca, piszący, treść
                    while j < len(u):
                        if u[j] == k1:
                            u[j] = [k1]
                            p[j] = random.randint(1, 10000000)
                            break
                        j += 1
                    print("Pomyślnie usunięto użytkownika")
            else:
                print("Błędne hasło!")
        else:
            print("Nie można wykonać działania")

    elif z == "exit":
        print("Wylogowywanie...")
        k = input()
        n = 0
        if k == "exit":
            exit(0)
        while n == 0:
            print("Podaj nazwę użytkownika: ", end='')
            k = input()
            try:
                j = u.index(k)
                print("Wpisz hasło użytkownika ", u[j], ": ", sep='', end='')
                k = input()
                if k == p[j]:
                    print("Pomyślnie zalogowano na konto:", u[j])
                    i = j
                    n = 1
                else:
                    print("Błędne hasło!")
            except:
                print("Nie ma takiego użytkownika")

    elif z == "pycal":
        try:
            print("Podaj 2 liczby:")
            print("     ", end='')
            a = int(input())
            print("     ", end='')
            b = int(input())
            print("Wybierz działanie: + - * / % ^")
            print("     ", end='')
            k = input()
            if k == '+':
                print(a, '+', b, '=', a + b)
            elif k == '-':
                print(a, '-', b, '=', a - b)
            elif k == '*':
                print(a, '*', b, '=', a * b)
            elif k == '/':
                if b != 0:
                    print(a, '/', b, '=', a / b)
                else:
                    print("Nie można wykonać działania")
            elif k == '^':
                print(a, '^', b, '=', pow(a, b))
            else:
                if b != 0:
                    print(a, '%', b, '=', a % b)
                else:
                    print("Nie można wykonać działania")
        except:
            print("Coś poszło nie tak")

    elif z == "txt":
        print("Podaj nazwę pliku: ", end='')
        k = input()
        try:
            k1 = txt.index(k)
            print("Plik już istnieje!")
        except:
            txt.append(k)
            txt.append(i)
            print("Możesz rozpocząć pisanie pliku (exit_txt):")
            k = ''
            txt1 = []
            while k != "exit_txt":
                k = input()
                txt1.append(k)
            txt1.remove(k)
            txt.append(txt1)
            print("Pomyślnie zapisano")

    # nazwa, właściciel, tekst

    elif z == "print_txt":
        print("Podaj nazwę pliku: ", end='')
        k = input()
        m = 0
        try:
            m = txt.index(k)
        except:
            print("Plik nie istnieje!")
            continue
        if txt[m + 1] == i:
            d = txt[m + 2]
            e = 0
            while e < len(d):
                print(d[e])
                e += 1
        else:
            print("Nie masz dostępu!")

    # odbiorca, piszący, treść

    elif z == "pymail":
        k = ''
        print("Witamy w Pymail!")
        print("Co chcesz zrobić:")
        print("     1. Napisać mail'a")
        print("     2. Sprawdzić mail'e")
        print("     3. Wyjść")

        while k != '3':
            k = input()
            if k == '1':
                print("Odbiorca: ", end='')
                k = input()
                t = functions.check(u, k)
                if t != 'f' and k != u[i]:
                    chat.append(k)
                    chat.append(i)
                    print("Możesz rozpocząć pisanie wiadomości (exit_pymail):")
                    k = ''
                    chat1 = []
                    while k != "exit_pymail":
                        k = input()
                        chat1.append(k)
                    chat1.remove(k)
                    chat.append(chat1)
                    print("Pomyślnie wysłano wiadomość")
                elif t == 'f':
                    print("Nie ma takiego użytkownika")
                else:
                    print("Nie można wysłać wiadomości do siebie")

            if k == '2':
                j = 0
                m = 0
                while j < len(chat):
                    if chat[j] == u[i]:
                        d = chat[j + 2]
                        e = 0
                        print("Nadawca:", u[chat[j + 1]])
                        while e < len(d):
                            print(d[e])
                            e += 1
                        print()
                        m = 1
                    j += 1

                print("Nie ma żadnych nowych wiadomości dla Ciebie")

        print("Pomyślnie zakończono działanie programu")

    elif z == "help":
        help.help()
    else:
        print("Nieznane polecenie (help)")