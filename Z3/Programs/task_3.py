import math

import utils
##  Napisaæ program generuj¹cy i wypisuj¹cy liczby
#pierwsze mniejsze od N metod¹ Sita Eratostenesa.

def sito(n):
    _sito = [True for _ in range(n)]

    for i in range(2, int(math.sqrt(n))+1):
        j = 2*i
        while j < n+1:
            _sito[j] = False
            j += i

    for i in range(2, n):
        if _sito[i] == True:
            print(i)

def program():
    n = utils.get_number()
    sito(n)