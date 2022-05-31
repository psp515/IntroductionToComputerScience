import utils
import math

# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
# funkcja powinna zwrócić położenie wież. Uwaga- zakładamy, że wieża szachuje cały wiersz
# i kolumnę z wyłączeniem pola na którym stoi
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

def find_highest_val_in_arr(arr=[]):
    maximal = arr[0]
    save_index = 0
    for i in range(1, len(arr)):
        if arr[i] > maximal:
            maximal = arr[i]
            save_index = i
    return save_index

def task(d_arr, n):
    utils.display_d_arr(d_arr)
    column_sum = columns_sums(d_arr, n)
    rows_sum = rows_sums(d_arr, n)
    #print("R:", rows_sum)
    #print("C:", column_sum)
    h_x, h_y = find_highest_val_in_arr(rows_sum), find_highest_val_in_arr(column_sum)
    #rows_sum[h_x] = 0
    #column_sum[h_y] = 0
    #print("R:", rows_sum)
    #print("C:", column_sum)
    s_x, s_y = find_highest_val_in_arr(rows_sum), find_highest_val_in_arr(column_sum)
    #rows_sum[h_x] = 0
    #column_sum[h_y] = 0
    #print("R:", rows_sum)
    #print("C:", column_sum)
    return [(h_x, h_y), (s_x, s_y)]

def program():
    print(task(utils.create_d_arr_rand(8, 8), 8))