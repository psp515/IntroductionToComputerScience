import utils
import math

#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu,
# dla którego iloraz sumy elementów w kolumnie w którym leży element do sumy
# elementów wiersza w którym leży element jest największa.

def rows_sums(d_arr,n):
    row_sum = [0 for _ in range(n)]
    i = 0
    for arr in d_arr:
        for e in arr:
            row_sum[i] += e
        i += 1
    return row_sum

def columns_sums(d_arr,n):
    column_sum = [0 for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            column_sum[k] += d_arr[j][i]
        k += 1
    return column_sum


def task(d_arr, n):
    #d_arr = [[1, 3, 5, 7],[2, 4, 6, 8],[2, 3, 5, 7],[1, 1, 2, 10]]
    row_sum = rows_sums(d_arr, n)
    column_sum = columns_sums(d_arr, n)
    print("Column sums:", column_sum)
    print("Rows sum:",row_sum)

    x, y, div = 0, 0, 0

    for i in range(n):
        for j in range(n):
            t_div = column_sum[i]/row_sum[j]
            if t_div > div:
                div = t_div
                x = i
                y = j

    return x, y, div

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_rand(n, n), n))