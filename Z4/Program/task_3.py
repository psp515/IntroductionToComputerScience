import utils
import math

#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która odpowiada na pytanie, czy istnieje wiersz
# w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę parzystą.

def contains_even_dig(n):
    while n > 0:
        dig = n % 10
        if dig % 2 == 0: return True
        n //= 10
    return False

def every_row_element_contains_even_dig(arr):
    for n in arr:
        if contains_even_dig(n) == False:
            return False
    return True

def task(d_arr):
    for row in d_arr:
        if every_row_element_contains_even_dig(row):
            return True
    return False

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_1_to_n(n, n)))