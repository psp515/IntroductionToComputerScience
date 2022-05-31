import utils
import math

#Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość True w przypadku,
# gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku.

def row_contains_0(row):
    for e in row:
        if e == 0:
            return True

    return False

def task(d_arr, n):
    utils.display_d_arr(d_arr)
    count_breaks = 0
    for i in range(n):
        for j in range(n):
            if d_arr[j][i] == 0:
                count_breaks += 1
                break

    for row in d_arr:
        if row_contains_0(row):
            count_breaks += 1
    return count_breaks == 2 * n

def program():
    n = utils.get_number()
    print(task([[0, 1, 2,4],[1, 0, 3,4],[1, 2, 0,4],[1,2,0,0]], 4))#utils.create_d_arr_rand(n, n), n))