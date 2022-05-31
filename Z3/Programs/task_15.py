import math

import utils
##  Dana jest du�a tablica t. Prosz� napisa�
#funkcj�, kt�ra zwraca informacj� czy w tablicy
#zachodzi nast�puj�cy warunek: �wszystkie elementy,
#kt�rych indeks jest elementem ci�gu Fibonacciego
#s� liczbami z�o�onymi, a w�r�d pozosta�ych
#przynajmniej jedna jest liczb� pierwsz��
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_not_fib_index(n):
    if n == 0:
        return False
    fib = 1
    prev_fib = 1
    while fib <= n:
        if fib == n:
            return False
        fib, prev_fib = fib+prev_fib, fib

    return True

def has_prime(arr):
    for i in range(len(arr)):
        if is_prime(arr[i]) and is_not_fib_index(i):
            #print("Any prime index: (not fib index)", i)
            return True

    return False

def fib_index_complex(arr = []):
    i = 0
    fib = utils.get_fibonnacci(i)
    while fib < len(arr):

        if is_prime(arr[fib]):
            #print("Prime number on fib index",fib)
            return False
        i+=1
        fib = utils.get_fibonnacci(i)
    return True


def task_func(arr=[]):
    #print(arr)
    return has_prime(arr) and fib_index_complex(arr)

def program():
    n = utils.get_number()
    print(task_func(utils.random_array(n, 0, 100)))