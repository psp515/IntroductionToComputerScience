import utils
import math

#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która w poszukuje w tablicy najdłuższego ciągu geometrycznego
# leżącego ukośnie w kierunku prawo-dół, liczącego co najmniej 3 elementy.
# Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje
# czy udało się znaleźć taki ciąg oraz długość tego ciągu.

def task(d_arr,n):
    # starting index in first row
    j = 0 # columns
    geo_len_max = 0
    utils.display_d_arr(d_arr)
    for i in range(0, n - 2): # row
        counter = 0
        _len = 2
        q = d_arr[i+1][j+1]/d_arr[i][j]
        while counter < n-i-1:
            q2 = d_arr[i + 1][j + 1] / d_arr[i][j]
            if q2 == q:
                _len += 1
                if _len > geo_len_max:
                    geo_len_max = _len
            else:
                q = q2
                _len = 2

            i, j = i + 1, j + 1
            counter += 1
        j = 0

    # starting index in first column

    for i in range(0, n - 2): # row
        counter = 0
        _len = 2
        q = d_arr[j+1][i+1]/d_arr[j][i]
        while counter < n-i-1:
            q2 = d_arr[j + 1][i + 1] / d_arr[j][i]
            if q2 == q:
                _len += 1
                if _len > geo_len_max:
                    geo_len_max = _len
            else:
                q = q2
                _len = 2

            i, j = i + 1, j + 1
            counter += 1
        j = 0

    return ( (True, geo_len_max) if geo_len_max >= 3 else False)

def program():
    n = utils.get_number()
    print(task([[1,2,3,4],[2,3,2,2],[4,4,4,4],[8,8,8,8]],n))#utils.create_d_arr_rand(n, n), n))