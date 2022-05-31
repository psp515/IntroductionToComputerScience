import utils
import math
import copy
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która zwraca liczbę par elementów,
# o określonym iloczynie, takich że elementy są odległe o jeden
# ruch skoczka szachowego.

def task(d_arr, n, k):
    # generate posible combinations
    arr = []
    i_arr = [(-2, -1), (-1, -2),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
    for i in range(n):
        for j in range(n):
            for e in i_arr:
                a, b = e
                arr.append((i, j, i+a, j+b))

    # Delete unnecesary combinations
    for e in copy.deepcopy(arr):
        try:
            if e[0] < 0 or e[1] < 0 or e[2] < 0 or e[3] < 0:
                arr.remove(e)
            if e[0] >= n or e[1] >= n or e[2] >= n or e[3] >= n:
                arr.remove(e)
        except:
            continue

    count = 0

    utils.display_d_arr(d_arr)
    # search for value in possible combinatons
    for e in arr:
        a, b, c, d = e
        i = d_arr[a][b]*d_arr[c][d]
        if i == k:
            count += 1

    # each combination is counted twice so
    return int(count/2)

def program():
    n = utils.get_number()
    k = utils.get_number("Iloczyn")
    print(task(utils.create_d_arr_rand(n, n), n, k))