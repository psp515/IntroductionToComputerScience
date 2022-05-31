import utils
import math

# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która odpowiada na pytanie, czy w tablicy
# każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z
# cyfr będących liczbami pierwszymi?

def is_dig_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    return False

def number_contains_only_prime_dig(n):
    while n > 0:
        if is_dig_prime(n % 10) == False:
            return False
        n //= 10
    return True

def row_anynumber_contains_onlyprimes(row):
    for e in row:
        if number_contains_only_prime_dig(e):
            return True
    return False

def task(d_arr, n):
    utils.display_d_arr(d_arr)
    for row in d_arr:
        if row_anynumber_contains_onlyprimes(row) == False:
            return False
    return True

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_rand(n, n), n))