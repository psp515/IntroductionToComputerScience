import math

import utils

# What is the largest prime factor of the number 600851475143 ?

def biggest_prime_factor(n):
    if utils.is_prime(n):
        return n

    factor = int(math.sqrt(n)) + 1
    while factor >= 1:
        if n % factor == 0 and utils.is_prime(factor):
            return factor
        factor -= 1

def program():
    n = utils.get_number()
    print(biggest_prime_factor(n))
