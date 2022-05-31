import utils
import math

# Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zeruje elementy nie posiadające liczby komplementarnej.

def contains_complimentary(d_arr, n, x,y):
    for i in range(n):
        for j in range(n):
            if (x != i or y != j) and utils.is_prime(d_arr[x][y]+d_arr[i][j]):
                return True
    return False


def task(d_arr, n):
    utils.display_d_arr(d_arr)
    d_arr_copy = d_arr
    for i in range(n):
        for j in range(n):
            if contains_complimentary(d_arr_copy,n, i, j) == False:
                d_arr[i][j] = 0
    print("---")
    return d_arr

def program():
    n = utils.get_number()
    utils.display_d_arr(task(utils.create_d_arr_rand(n, n), n))#([[8,3,3],[5,0,7],[0,1,11]],3)