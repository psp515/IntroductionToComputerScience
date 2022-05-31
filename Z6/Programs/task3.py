import math
import utils

# Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
# zawie- rającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje
# się w wierszu 0 i kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza
# 7. Proszę napisać funkcję, która wyznaczy minimalny koszt przejścia króla.
# Do funkcji należy przekazać tablicę t oraz startową kolumnę k.
# Koszt przebywania na polu startowym i ostatnim także wliczamy
# do kosztu przejścia.

# arr - tablica kosztów
# k - kolumna
# w - wiersz
# s - suma kosztów

def task(arr, k=0, w=0, s=0):
    if w == 6:
        return s
    if w == 0:
        s += arr[w][k]
    if k == 0:
        return min(task(arr, k, w+1, s+arr[w+1][k]), task(arr, k+1, w+1, s+arr[w+1][k+1]))
    elif k == 7:
        return min(task(arr, k, w + 1, s + arr[w + 1][k]), task(arr, k - 1, w + 1, s + arr[w + 1][k - 1]))
    else:
        return min(task(arr, k, w+1, s+arr[w+1][k]), task(arr, k+1, w+1, s+arr[w+1][k+1]), task(arr, k-1, w+1, s+arr[w+1][k-1]))

def program():
    print(task([[1,2,3,4,5,6,7,8],
                [11,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8],
                [1,2,3,4,5,6,7,8]], 0, 0, 0))