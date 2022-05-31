import utils
import math

# Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są
# identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N]
# wypełniona liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca
# ile elementów tablicy sąsiaduje wyłącznie z przyjaciółkami

# zapytaj jak sasiaduja czy wszystkie w kwadracie  czy z gory,dolu,lewo.prawo tylko

def get_dig(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10
    return utils.sort(arr)

def generate_neighbour(a, b):
    return [(a-1,b-1),(a-1,b),(a,b-1),(a+1,b-1),(a-1,b+1),(a,b+1),(a+1,b),(a+1,b+1)]

def is_valid(e=(),n=0):
    a,b = e
    return (a>=0 and b >= 0) and (a < n and b < n)

def compare_arr(arr, arr2):
    if len(arr)!= len(arr2): return False
    for i in range(len(arr)):
        if arr[i] != arr[i]:
            return False
    return True

def task(d_arr, n):
    utils.display_d_arr(d_arr)
    count = 0
    for i in range(n):
        for j in range(n):
            is_succes = True
            digarr = get_dig(d_arr[i][j])
            arr = generate_neighbour(i, j)
            for e in arr:
                if is_valid(e, n):
                    a, b = e
                    if compare_arr(digarr,get_dig(d_arr[a][b])) == False:
                        is_succes = False
                        break
            if is_succes:
                count += 1

    return count

def program():
    n = utils.get_number()
    print(task([[1,1,1],[1,1,1],[1,1,2]],3))