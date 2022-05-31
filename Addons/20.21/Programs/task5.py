
# Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek.


# W mojej opinii warunki zadania źle dobrane bo nie nwd(a,b,c)==1
# tylko nwd par a,b | b,c | a,c == 1, a to co innego.


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# obliczanie nwd dla par a,b |b,c| a,c
def NWD3(a,b,c):
    return NWD(a, b) == 1 and NWD(b, c) == 1 and NWD(a, c) == 1


# arr - tablica
# i - aktualny index w tablicy
# numbers - zbierane liczby po drodze
# skip - czy ostatnia pozycja byla pominięta
def trojki_count(arr, i=0, numbers=[], skip=False):
    if len(numbers) == 3: # jezeli mamy 3 liczby to sprawdzamy warunki
        if NWD3(numbers[0],numbers[1],numbers[2]) == 1: # sprawdzamy warunki
            return 1
        return 0

    if i == len(arr): # jezeli wyszlismy poza tablice to koniec
        return 0

    if skip == True: # jezeli pominelisy ostatni wyraz to musimy brac aktualny
        return trojki_count(arr, i+1, numbers + [arr[i]], False)

    # standardowe zakonczenie albo bierzemy element albo nie
    return trojki_count(arr, i+1, numbers, True) + trojki_count(arr, i+1, numbers + [arr[i]], False)

def trojki(arr):
    return trojki_count(arr)

def program():
    print(trojki([2,3,4,6,7,8,10]))