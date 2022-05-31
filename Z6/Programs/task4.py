import math
import utils

# Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def check_options(t, w, k, i):
    pion = [2, 1, -1, -2, -2, -1, 1, 2]
    poziom = [1, 2, 2, 1, -1, -2, -2, -1]
    new_w = w + pion[i]
    new_k = k + poziom[i]
    if 0 <= new_w < len(t) and 0 <= new_k < len(t) and t[new_w][new_k] == 0:
        return (new_w, new_k)
    return None

def validate_arr(d_arr):
    for arr in d_arr:
        for e in arr:
            if e == 0:
                return False
    return True

def count_0(d_arr):
    counter = 0
    for arr in d_arr:
        for e in arr:
            if e == 0:
                counter += 1
    return counter

is_found = False

def task(arr, i=0, j=0, p=1):
    global is_found

    if is_found:
        return
    if validate_arr(arr):
        utils.display_d_arr(arr)
        is_found = True

    if arr[i][j] != 0:
        return
    print(p)
    #print(f"------------------- {count_0(arr)}")
    #utils.display_d_arr(arr)
    arr[i][j] = p
    for z in range(8):
        x = check_options(arr, i, j, z)
        if x is not None:
            task(arr, x[0], x[1], p + 1)

    arr[i][j] = 0 # musimy wyzerowac pole ktróe okazało sie zlym trafem



def program():
    n = utils.get_number()
    print(task(utils.create_d_arr(n, n), 0, 4))