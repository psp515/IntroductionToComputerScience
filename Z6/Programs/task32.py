import math
import utils

# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa
# podzbiory ojednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k.
# Do funkcji należy przekazaćwyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna
# zwrócić wartość typu bool.

# arr - tablica
# k - suma mocy zbiorow
# i - pozycja w tablicy
# s1,s2 - sumy zbiorów
# c1,c2 - liczby elementów w zbiorach

def task(arr, k, i = 0, s1=0, c1 = 0, s2=0, c2 =0):

    if c1+c2 == k and s1 == s2: # jezeli spelniaja warunki prawda
        return True

    if c1+c2 > k or i == len(arr): # jezeli tablica sie skonczy albo suma mocy jest wieksza false
        return False

    return task(arr, k, i+1, s1, c1, s2, c2) or \
           task(arr, k, i+1, s1+arr[i], c1+1, s2, c2) or\
           task(arr, k, i+1, s1, c1, s2+arr[i], c2+1)
    # 1 - nie biore do rzadnego zbioru,
    # 2 - biore do zbioru 1,
    # 3 - biore do zbioru 2



def program():
    #n = utils.get_number()
    arr = [2, 2, 2, 2]
    print(task(arr, 4))