import math


def get_number(text="Podaj liczbe: "):
    try:
        return int(input(text))
    except:
        return get_number(text)

def get_float_number(text="Podaj liczbe: "):
    try:
        return int(input(text))
    except:
        return get_number(text)

def get_fibbonacci_by_index(n):
    if n == 0: return 0
    if n == 1: return 1
    return get_fibbonacci_by_index(n-1) + get_fibbonacci_by_index(n-2)


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
