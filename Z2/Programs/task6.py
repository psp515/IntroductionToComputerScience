import utils
import math

# Napisać program wczytujący liczbę naturalną z klawiatury
# i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy.
# Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.

def get_two_divisors(n):
    n_sqrt = int(math.sqrt(n))
    if n_sqrt**2 == n:
        return (n_sqrt, n_sqrt)
    n_sqrt_2 = n_sqrt
    multi = n_sqrt * n_sqrt_2
    while multi != n:
        if multi > n:
            n_sqrt -= 1
        else:
            n_sqrt_2 += 1
        multi = n_sqrt * n_sqrt_2
    return n_sqrt, n_sqrt_2




def program():
    n = utils.get_number("Podal liczbe: ")
    print(get_two_divisors(n))