import math

import utils
##  Dana jest N-elementowa tablica t zawieraj�ca
#liczby naturalne mniejsze od 1000. Prosz� na-
#pisa� funkcj�, kt�ra zwraca d�ugo�� najd�u�szego,
#sp�jnego fragmentu tablicy, dla kt�rego w
#iloczynie jego ele- ment�w ka�dy czynniki pierwszy
#wyst�puje co najwy�ej raz. Na przyk�ad dla tablicy
#t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest
#warto�� 5. 2

def single_prime_members(n):
    i = 2
    while n > 1:
        count_primes = 0
        while n % i == 0:
            count_primes += 1
            n //= i
        if count_primes >= 2:
            return False
        i += 1
    return True

def task_func(arr = []):
    max_count = 0
    count = 0
    iloraz = 1
    for e in arr:
        iloraz *= e
        if single_prime_members(iloraz) == True:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
            iloraz = e
            if single_prime_members(iloraz) == True:
                count += 1
            if max_count < count:
                max_count = count


    return max_count

def program():
    print(task_func([2,23,33,35,7,4,6,7,11,22]))