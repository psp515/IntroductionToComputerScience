import math
import utils

# Dana jest tablica T[N]. Proszę napisać program zliczający
# liczbę “enek” o określonym iloczynie.

# arr - tablica liczb
# i - nastepny index do sprawdzenia
# n - max liczba zabranych wyrazów
# m - zabrana liczba wyrazów
# multi - szukany iloczyn
# count - liczba n wyrazowych ciagów o iloczynie multi

def task(arr, n, s_multi, m = 0, act_multi = 1, i = 0):
    if m == n and s_multi == act_multi:
        return 1
    if i == len(arr) or m > n:
        return 0
    return task(arr, n, s_multi, m+1, act_multi*arr[i], i+1) + task(arr, n, s_multi, m, act_multi, i+1)


def program():
    n = utils.get_number()
    print(task([1,2,3,2,2], 3, 12, 0, 1, 0))