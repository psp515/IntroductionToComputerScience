import math
import utils

# Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanychwartościami
# typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości 2
# niepustych podzbiorów tego zbioru.


# funkcaj zwraca odleglosc 2 punktów od siebie
def get_mid_len(x1,y1,x2,y2):
    return abs(math.sqrt((x1-x2)**2+(y1-y2)**2))

# arr - tablica
# i - pozycja w tablicy
# x1,x2 - suma wspolrzednych x w jedynm zbiorze
# y1,y2 - suma wspolrzednych y w jedynm zbiorze
# p1,p2 - liczba punktów w jednym zbiorze

def task(arr, i=0, x1=0, y1=0, p1=0, x2=0, y2=0, p2=0):

    if i == len(arr): # jezeli doszlismy do konca tablicy
        if p2 != 0 and p1 != 0: # sprawdzam czy jest min po 1 pkt
            return get_mid_len(x1/p1, y1/p1, x2/p2, y2/p2) # jezeli tak to zwracam ich odleglosc
        else:
            return math.inf # jezeli nie zwracam nieskonczonosc

    return min(task(arr, i+1, x1, y1, x2, y2),
           task(arr, i+1, x1+arr[i][0], y1+arr[i][1], p1+1, x2, y2, p2),
           task(arr, i+1, x1, y1, p1, x2 + arr[i][0], y2 + arr[i][1], p2+1))
    # 1 - nie wybieram punktu,
    # 2 - wybieram pkt do zbioru 1
    # 3 - wybieram pkt do zbioru 2

def program():
    arr = [(1,1), (1,0)]
    print(task(arr))