import math
import utils

#Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr
# wszystkich liczb występujących w jej rozkładzie na czynniki pierwsze.
# Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący liczby Smitha
# mniejsze od 1000000.

def get_dig(n):
    arr = []
    while n>0:
        arr.append(n%10)
        n //= 10
    return arr

def get_divs(n):
    arr = []
    i=1
    while n>1:
        i += 1
        while n % i == 0:
            arr.append(i)
            n //= i

    return arr

def is_smith(n):
    arr = get_dig(n)
    arr2 = []
    for e in get_divs(n):
        arr2 += get_dig(e)
    return sum(arr2) == sum(arr)

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def print_smith():
    for i in range(2, 1000000):
        if is_prime(i) == False and is_smith(i):
            print(i)

def program():
    print_smith()