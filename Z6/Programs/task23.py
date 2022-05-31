import math
import utils

# Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbąkΩ.
# Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji
# R (równejcałkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.

# arr - tablica
# arr_len - dlugosc tablicy
# sR szukany opor
# i - pozycja w tablicy
# aR aktualny opor
# count - wybrana liczba opornikow

def task(arr, arr_len, sR, i=0, aR=0, count=0):
    if count == 3: # gdy polacze 3 sprawdzam czy moge osiagnac wskazany wynik
        return sR == aR
    if arr_len == i or count > 3: # jezeli lacze wiecej niz 3 lub skonczy mi sie tablica to false
        return False
    return task(arr, arr_len, sR, i+1, aR, count) or \
           task(arr, arr_len, sR, i+1, aR+arr[i], count+1) or \
           task(arr, arr_len, sR, i+1, ((aR*arr[i])/(aR+arr[i])), count)
    # 1 - pomijam opornik,
    # 2 - łacze szeregowo,
    # 3 - łacze równolegle



def program():
    n = utils.get_number()
    arr = [1, 2, 3, 4, 5]
    print(task(arr, len(arr), n, 0, 0, 0))