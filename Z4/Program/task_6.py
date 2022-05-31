import utils
import math

#Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# T1[N][N] i T2[M], gdzie M=N*N. W każdym wierszu tablicy T1 znajdują
# się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne. Proszę napisać
# funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz)
# z tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco.
# Pozostałe elementy tablicy T2 powinny zawierać zera.

def task(d_arr, n):
    arr = []
    utils.display_d_arr(d_arr)
    for row in d_arr:
        arr += row

    utils.sort(arr)
    print(arr)
    arr2 = utils.crate_arr(n*n)
    j = 0
    count = 1
    for i in range(n*n-1):
        if arr[i] == arr[i+1]:
            count += 1
        elif count > 1:
            count = 1
        else:
            arr2[j] = arr[i]
            j += 1

    if arr[n*n-2] != arr[n*n-1]:
        arr2[j] = arr[n*n-1]
    return arr2

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_rand(n, n), n))#([[1, 2, 3, 4], [1, 1, 2, 3], [1, 1, 2, 2], [4, 4, 5, 6]], n))