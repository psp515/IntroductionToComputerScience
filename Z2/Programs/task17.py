import math

import utils

# x^x metoda stycznych

def f_prim(x):
    return (x**x) * (math.log(math.e, x) + 1)

def f(x, val):
    return x**x - val

def calculate(max = 5, val = 2020):
    point = max
    while abs(f(point,val)) > 0.01:
        print(point)
        point = point - (f(point, val)/f_prim(point))

    return point


def program():
    n = utils.get_number("Liczba która chcemy obliczyć: ")
    k = utils.get_number("Liczba dla która daje wiekszy wynik np 5 bo 5^5 > 2020 (gdy wyliczamy 2020)")
    print(calculate(k, n))