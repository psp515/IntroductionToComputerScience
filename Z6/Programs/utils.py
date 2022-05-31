import random
import math

def get_number(text = "Podaj liczbe: "):
    try:
        return int(input(text).strip())
    except:
        return get_number(text)
def get_number_length(n):
    return int(math.log10(n)) + 1

def random_array(n, e_min, e_max):
    return [random.randint(e_min, e_max) for _ in range(n)]

def get_fibonnacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return get_fibonnacci(n - 1) + get_fibonnacci(n - 2)

def crate_arr(n):
    return [0 for _ in range(n)]


def create_d_arr(rows=0, columns=0):
    if columns == 0:
        columns = rows
    return [[0 for _ in range(columns)] for _ in range(rows)]

def create_d_arr_1_to_n(rows=0, columns=0):
    if columns == 0:
        columns = rows
    return [[i for i in range(columns)] for _ in range(rows)]

def create_d_arr_rand(rows=0, columns=0):
    if columns == 0:
        columns = rows
    return [[random.randint(0, 10) for _ in range(columns)] for _ in range(rows)]

def display_d_arr(arr):
    for sub_arr in arr:
        print(sub_arr)

def is_prime(n):
    if n <= 1:return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

# simple sort
def sort(arr = []):
    moves = 1
    while moves > 0:
        moves = 0
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                moves += 1
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