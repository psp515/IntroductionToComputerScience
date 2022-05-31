import math
import utils

# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów
# elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby.
# Można założyć,że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym
# etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej. Przykład:
# 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

# zwraca podzielniki funkcji
def get_divisors(n):
    arr = []
    i = 2
    while n > 1:
        if n % i == 0:
            arr.append(i)
        while n % i == 0:
            n //= i
        i += 1
    return arr

# zwraca tablice od dlugosci max_len bitów (wybranych elementów)
def get_bin_arr(n, max_len):
    arr = [0 for _ in range(max_len)]
    i = 0
    while n > 0:
        arr[i] = n % 2
        n //= 2
        i+=1

    return arr

# zwraca iloczyn wybranych elementow z tablicy
def get_multi(arr, mask):
    multi = 1
    bit_arr = get_bin_arr(mask, len(arr))
    for i in range(len(bit_arr)):
        if bit_arr[i] == 1:
            multi *= arr[i]
    return multi if multi != 1 else 0

# n - liczba
# arr - tablica podzielnikow
# mask - maska bitowa

def task(n, arr=[], mask=0):
    if 2**len(arr) == mask:
        return 0
    if len(arr) == 0:
        arr = get_divisors(n)
    return task(n, arr, mask+1) + get_multi(arr, mask)

def program():
    n = utils.get_number()
    print(task(n))