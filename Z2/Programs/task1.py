import math

import utils
# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający
# na pytanie, czy liczba ta jest iloczynem dowolnych dwóch wyrazów
# ciągu Fibonacciego.

def multi_exists(n):
    if n < 0:
        return False
    if n <= 2:
        return True

    i = 2
    a = utils.get_fibb_by_index(i)
    while a <= n:
        j = 2
        b = utils.get_fibb_by_index(j)
        while a * b < n and b < a:
            b = utils.get_fibb_by_index(j)
            j += 1
        if a*b == n:
            return True
        i += 1
        a = utils.get_fibb_by_index(i)

    return False

def opt_2(num):
    maxi = math.sqrt(num)
    while a1 < maxi:
        if num % a1 == 0:
            b1, b2 = a1, a2
            while a1 * b1 < num:
                b1, b2 = b2, b1 + b2
            if a1 * b1 == num:
                print("da się")
                break
        a1, a2 = a2, a1 + a2
    else:
        print("nie da się")

def program_1():
    n = utils.get_number("Podal liczbe: ")
    has = multi_exists(n)
    print(has)