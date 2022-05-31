import utils
import math

#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która odpowiada na pytanie, czy w każdym
# wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.

def contains_only_odd_dig(n):
    while n > 0:
        dig = n % 10
        if dig % 2 == 0: return False
        n //= 10
    return True

def contins_only_odd_dig_number(arr):
    for n in arr:
        if contains_only_odd_dig(n):
            return True
    return False

def task(d_arr, n):
    for row in d_arr:
        if contins_only_odd_dig_number(row) == False:
            return False
    return True

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_1_to_n(n, n), n)) # [[112,21,3],[132,22,3],[2,1,41]] True, [[112,21,3],[132,22,3],[2,4,41]] False