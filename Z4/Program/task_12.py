import utils
import math

# Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy
# tablicę wypeł- nioną liczbami większymi od zera. Funkcja powinna zwracać wartość True,
# jeżeli na wszystkich poziomach tablicy liczba elementów sąsiadujących (w obrębia poziomu)
# z co najmniej 6 liczbami złożonymi jest jedna- kowa albo wartość False w przeciwnym przypadku.

# sprawdza czy objekt jest zlozony na podstawie tego czy jest pierwszy
def is_complex(n):
    if n <2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return True # nie jest pierwsza

    return False # jest pierwsza


def task(arr):
    f_count = -1
    for k in range(len(arr)): # iteruje po poziomach
        count = 0
        for i in range(len(arr)): #iteracja po tablicach 2 wymiarowych
            for j in range(len(arr)):
                count_close = 0
                arr = [(1,1),(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)]
                for e in arr: # sprawdzam sasiednie pola i zliczam liczby zlozone
                    a,b = i+e[0], j+e[1]
                    if a >0 and b >0 and b < len(arr) and a < len(arr):
                        if is_complex(arr[a][b]):
                            count_close +=1
                if count_close >=6: # jezeli wiecej niz 6 takich otacza liczbe to count +1
                    count += 1

        if f_count == -1: # po sprawdzeniu pierwszego wymiaru ustaw licznik ktory musza spelniac inne wymiary
            f_count = count

        if count != f_count: # sprawdzam liczniki ktory musi byc taki sam dla kadego wymiaru
            return False

    return True

# inny pomysl rozwiazania tego zadania zeby nie zamieniac niektorych liczb po kilka razy
# pierwsze przerobic wszystko na liste boolean
# przegladac liste i sprawdzac otaczajace pola i zliczac tak samo
# oszczedamy czas na wykonywanie obliczen zwiazanych z funkcja is_complex

def program():
    n = utils.get_number()
    print(task(n))