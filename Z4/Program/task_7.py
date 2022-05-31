import utils
import math

# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M],
# gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco
# (w obrębie wiersza) liczby naturalne. Proszę napisać funkcję przepisującą wszystkie
# liczby z tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane niemalejąco.



def task(d_arr, n):
    arr = []
    for row in d_arr:
        arr += row
    print(d_arr)
    return utils.sort(arr)

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_rand(n, n), n))