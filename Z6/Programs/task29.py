import math
import utils

#Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
# współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać
# funkcję,która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego
# środek ciężkości leży wodległości nie większej niż r od początku układu współrzędnych. Do
# funkcji należy przekazać tablicę T orazpromień r, funkcja powinna zwrócić wartość typu bool.

# funkcja oblicza odleglosc od (0,0,0)
def is_closer_than_r(x,y,z,r):
    return math.sqrt(x*x+y*y+z*z) < r
# arr - tablica
# r -promien max
# i - aktualny index w tablicy
# x_sum - suma wspolrzednych x owych
# z_sum - suma wspolrzednych z owych
# y_sum suma wspolrzednych y owych
# p_count - liczba zsumowanych punktów

def task(arr, r,i =0, x_sum=0,y_sum=0, z_sum=0, p_count=0):
    if i == len(arr): # jezeli doszedles do konca tablicy sprawdz odleglosc jezeli wziales conajmiiej 3 pkt
        return is_closer_than_r(x_sum/p_count, y_sum/p_count, z_sum/p_count, r) if p_count >= 3 else False
    if p_count >= 3: # jezeli masz juz 3 pkt sprawdz czy znalazles takie 3 pk jezeli nie kontynułuj dobieranie
        if is_closer_than_r(x_sum/p_count, y_sum/p_count, z_sum+p_count, r):
            return True
    # kontynuacja dobierania
    return task(arr, r, i+1, x_sum, y_sum, z_sum, p_count) or \
           task(arr, r, i+1, x_sum + arr[i][0], y_sum + arr[i][1], z_sum + arr[i][2], p_count + 1)


def program():
    arr = [(1,1,1), (12,2,0), (2,2,1)]
    print(task(arr, 2))