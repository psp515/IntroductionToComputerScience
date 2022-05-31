import math
import utils

# Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
# Można ulepszyc algorytm

# funkcja tworzy mniejsza macierz zgodnie ze wzorem laplacea
def get_new_arr(arr, arr_len, row, col):
    d_arr = []
    for i in range(arr_len):
        sub_arr = []
        if i != row: # pomijamy wybrany rzad
            for j in range(arr_len):
                if j != col:
                    sub_arr += [arr[i][j]] # bierzemy tylko te elementy ktore nie sa w kolumnie col
        if sub_arr != []:
            d_arr += [sub_arr] # powiekaszamy macierz o kolejny rzad
    print(d_arr)
    return d_arr

# arr - tablica
# arr_len - dlugosc tablicy

def task(arr, arr_len):
    if arr_len == 1:
        return arr[0]
    if arr_len == 2: # elementarny przypadek macierzy
        return arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0]

    matrix_sum = 0
    row = 0 # mozna stworzyc funkcje ktora wyskuje najlepszy wiersz ale po co w sumie
    for col in range(arr_len): # obliczanie wyznacznika n na n
        new_arr = get_new_arr(arr, arr_len, row, col)
        matrix_sum += arr[row][col] * task(new_arr, arr_len-1) * (-1)**(row+col)

    return matrix_sum

def program():
    matrix = [[9,2,3],
              [4,0,6],
              [7,8,9]]
    print(task(matrix,3))