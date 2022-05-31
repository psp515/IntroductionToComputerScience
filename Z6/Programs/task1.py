import math
import utils

# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i
# wypisuje wszystkie co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez
# wykreślenie z liczby pierwotnej co najmniej jednej cyfry.

def is_prime(n):
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(5, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def get_digs(arr_len,n, d):
    arr = [0 for _ in range(arr_len)]
    i = 0
    while n > 0:
        arr[i] = n % d
        n //= d
        i += 1
    return arr[::-1]

def is_valid(integer,bit_mask):
    bit_arr = get_digs(utils.get_number_length(integer), bit_mask, 2)
    dig_arr = get_digs(utils.get_number_length(integer), integer, 10)
    new_num = 0
    for i in range(0, len(bit_arr)):
        if bit_arr[i] == 1:
            new_num = new_num * 10 + dig_arr[i]

    return 1 if is_prime(new_num) and new_num>9 else 0

# integer - liczba calkowita
# bit_mask - maska bitowa na ktorej podsawie usuwamy cyfry odrzucamy wariant 00...0 i 11...1

def task(integer, bit_mask = 1):
    if bit_mask >= (2**(utils.get_number_length(integer))-1):
        return 0
    return is_valid(integer, bit_mask) + task(integer, bit_mask+1)


def program():
    n = utils.get_number()
    print(task(n, 1))