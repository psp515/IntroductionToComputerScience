import math
import utils

# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy
# możnawybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby
# żadne dwa wybraneelementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy
# przekazać wyłącznie tablicę orazwartość sumy, funkcja powinna zwrócić wartość typu bool.

def task(arr,expected_sum, sum, i, columns=[]):
    if expected_sum == sum:
        return True

    if i == len(arr) or expected_sum > sum:
        return False
    else:
        for k in range(i,8):
            for j in range(8):
                if columns[j] == 0:
                    columns[j] = 1
                    res = task(arr,expected_sum,sum+arr[k][j],i+1,columns)
                    if res == True:
                        return True

        return False


def program():
    arr = [[2,2], [2,2]]
    print(task(arr, len(arr),10,0,0,0))