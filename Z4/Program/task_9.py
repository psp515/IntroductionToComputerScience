import utils
import math

# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w poszukuje w
# tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól narożnych
# wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje czy
# udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

def get_sizes(n):
    s = 3
    arr = []
    while s <= n:
        arr.append(s)
        s+=2
    return arr

def task(d_arr, n, k):
    utils.display_d_arr(d_arr)
    sq_sizes = get_sizes(n)
    for size in sq_sizes:
        for i in range(n-size+1):
            for j in range(n-size+1):
                val = d_arr[i][j]*d_arr[i+size-1][j+size-1]*d_arr[i+size-1][j]*d_arr[i][j+size-1]
                if val == k:
                    return i + (size-1)/2, j+(size-1)/2

    return False

def program():
    n = utils.get_number()
    k = utils.get_number("k: ")

    print(task([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,4,4,5]], n, k))#utils.create_d_arr_rand(n, n)