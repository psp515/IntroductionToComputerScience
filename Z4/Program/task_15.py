import utils
import math

# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba
# zawiera co najmniej jedną cyfrę będącą liczbą pierwszą?

def is_dig_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    return False

def number_contains_prime_dig(n):
    while n > 0:
        if is_dig_prime(n % 10):
            return True
        n //= 10
    return False

def row_numbers_contains_primes(row):
    for e in row:
        if number_contains_prime_dig(e) == False:
            return False
    return True

def task(d_arr, n):
    utils.display_d_arr(d_arr)
    for row in d_arr:
        if row_numbers_contains_primes(row):
            return True
    return False

def program():
    n = utils.get_number()
    print(task(utils.create_d_arr_rand(n, n), n))