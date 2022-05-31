import utils

# Napisać program, który oblicza pole figury pod wykresem
# funkcji y = 1/x w przedziale od 1 do k, metodą prostokątów.

def f(x):
    return 1/x

def calculate_field(k, e= 0.01):# koniec przedzialu ,dlugosc przedzialu
    sum = 0.0
    x_lower = 1.0
    while x_lower < k:
        sum += f((x_lower + x_lower+e) / 2)*0.01
        x_lower += e

    return sum

def program():
    k = utils.get_number("Podaj koniec przedzialu: ")
    print(calculate_field(k))
    print(calc_area(k))