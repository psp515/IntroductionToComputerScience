import math
import random

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
    if n == 0:
        return 0
    if n == 1:
        return 1

    return get_fibonnacci(n - 1) + get_fibonnacci(n - 2)