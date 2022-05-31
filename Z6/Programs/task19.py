import math
import utils

#Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z
# pola w,k do któregokolwiek z narożników.

# podaje ostania cyfre liczby
def get_first_dig(n):
    first_dig = 0
    while n > 0:
        first_dig = n % 10
        n //= 10
    return first_dig

# sprawdza czy ostatnia cyfra liczby 1 jest mniejsza od pierwszej cyfry liczby 2
def dig_compare(num1, num2):
    last_dig = num1 % 10
    first_dig = get_first_dig(num2)
    return last_dig < first_dig

# sprawdza i podaje mozliwe ruchy
def moves(arr, w, k):
    possibilities = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 1), (-1, 0), (0, -1)] # sprawdzamy dla 8 mozliwosci
    for e in possibilities:
        n_w, n_k = w + e[0], k + e[1]
        if n_w >= 0 and n_w < 8 and n_k >= 0 and n_k < 8:
            if dig_compare(arr[w][k], arr[n_w][n_k]):
                continue
            else:
                possibilities.remove(e)
    return possibilities

def task(arr, w, k):
    if (w == 7 and k == 7) or (w == 7 and k == 0) or \
            (w == 0 and k == 7) or(w == 0 and k == 0) : # jezeli jestes w rogu to sie udalo
        return True

    if w < 0 or w >= 8 or k < 0 or k >= 8: # jezeli wyszedles poza tablice to false
        return False
    print(w,k)
    is_succ = False
    for e in moves(arr, w, k): # sprawdz co sie dzieje dla innych ruchow
        is_succ = task(arr, w + e[0], k + e[1]) # sprawdzanie drogi
        if is_succ:
            break

    return is_succ


def program():
    arr = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 3, 3, 3, 0, 0],
           [0, 0, 0, 3, 2, 2, 2, 3],
           [0, 0, 0, 3, 2, 4, 2, 3],
           [0, 0, 0, 0, 2, 2, 2, 3],
           [0, 0, 0, 0, 3, 3, 3, 3]]

    print(task(arr, 5, 5))