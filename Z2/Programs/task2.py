import decimal

import utils
# Napisać program wczytujący trzy liczby naturalne a,b,n i
# wypisujący rozwinięcie dziesiętne ułamka a/b z
# dokładnością do n miejsc po kropce dziesiętnej.
# (n jest rzędu 100)


def print_decimal_numbers(a, b, n):
    if a % b == 0:
        print(a/b)
        return
    print(a//b, end=".")
    a = a % b
    while n > 0 and a > 0:
        a *= 10
        print(a//b, end="")
        a = a % b
        n -= 1
        if a == 0:
            return
    print("")

def program_2():
    a = utils.get_number("Podaj a: ")
    b = utils.get_number("Podaj b: ")
    c = utils.get_number("Podaj dokładność: ")
    print_decimal_numbers(a, b, c)
