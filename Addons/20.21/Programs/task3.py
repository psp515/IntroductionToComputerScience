

# Dana jest tablica T[N][N] (reprezentująca szachownicę)
# wypełniona liczbami całkowitymi. Proszę za- implementować
# funkcję chess(T) która ustawia na szachownicy dwie wieże,
# tak aby suma liczb na „szachowanych” przez wieże polach
# była największa. Do funkcji należy przekazać tablicę,
# funkcja powinna zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
# Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.

# odnioslem wrazenie ze pierwszy przyklad jest lipny

def create_arr(n):
    return [0 for _ in range(n)]

def get_max(col,rows):
    max_row_index = 0
    max_col_index = 0
    for i in range(len(col)):
        if col[max_row_index] < col[i]:
            max_row_index = i
        if rows[max_col_index] < rows[i]:
            max_col_index = i

    return max_row_index, max_col_index

def chess(arr):
    row_sum = create_arr(len(arr))
    col_sum = create_arr(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            row_sum[i] += arr[i][j]
            col_sum[i] += arr[j][i]
    print(col_sum,row_sum)
    a, b = get_max(row_sum, col_sum)
    for i in range(len(arr)):
        row_sum[i] -= arr[i][b]

    row_sum[a] = float('-inf')

    for i in range(len(arr)):
        col_sum[i] -= arr[a][i]

    col_sum[b] = float('-inf')
    print(col_sum, row_sum)
    c, d = get_max(row_sum, col_sum)

    return a, b, c, d

def program():
    arr = [[4,0,2],
           [3,0,0],
           [6,5,3]]
    print(chess(arr))