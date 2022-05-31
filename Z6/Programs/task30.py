import math
import utils

# Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
# współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę
# napisać funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n<k oraz n
# jest wielokrotnością liczby 3, którego środek ciężkości leży w odległości mniejszej niż r od
# początku układu współrzędnych. Do funkcjinależy przekazać dokładnie 3 parametry: tablicę t,
# promień r, oraz ograniczenie k, funkcja powinna zwrócićwartość typu bool.

# sprawdz odleglosc sordka masy od (0,0,0)
def is_closer_than_r(x,y,z,r):
    return math.sqrt(x*x+y*y+z*z) < r


# Zadanie prawie takie samo jak poprzednio
# arr - tablica
# r -promien max
# i - aktualny index w tablicy
# x_sum - suma wspolrzednych x owych
# z_sum - suma wspolrzednych z owych
# y_sum suma wspolrzednych y owych
# p_count - liczba zsumowanych punktów
# k - max liczba punktów

def task(arr, k,r,i =0, x_sum=0,y_sum=0, z_sum=0, p_count=0):
    if k == p_count: # dodatek jezeli mamy max pkt to na pewno false
        return False

    if i == len(arr): # zmiana jezeli przeszlismy przez cala tablice to sprawdzamy dodatkowe warunki
        if k > p_count and p_count%3==0 and p_count>0:
            return is_closer_than_r(x_sum/p_count, y_sum/p_count, z_sum/p_count, r)
        else:
            return False

    if p_count >= 3 and p_count % 3 == 0: # dodatkowy warunek
        if is_closer_than_r(x_sum/p_count, y_sum/p_count, z_sum+p_count, r):
            print(p_count)
            return True
    return task(arr, k, r, i+1, x_sum, y_sum, z_sum, p_count) or \
           task(arr, k, r, i+1, x_sum + arr[i][0], y_sum + arr[i][1], z_sum + arr[i][2], p_count + 1)


def program():
    arr = [(1,1,1), (1,1,1), (1,1,1)]
    print(task(arr, 5, 5))