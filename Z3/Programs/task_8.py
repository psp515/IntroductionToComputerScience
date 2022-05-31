import math

import utils
import random
# Dana jest N-elementowa tablica t zawieraj¹ca
# liczby naturalne. W tablicy mo¿emy przeskoczyæ z
# pola o indeksie k o n pól w prawo je¿eli wartoœæ n
# jest czynnikiem pierwszym liczby t[k].

# Actual zadanie:
# Napisaæ funkcjê sprawdzaj¹c¹ czy jest mo¿liwe przejœcie z
# pierwszego pola tablicy na ostatnie pole.

def is_prime(n): #
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_jump_possible(arr=[], arr_len=0):
    predicted_jump = arr_len - 1 # skok to musi byc liczba pierwsza bo n jest czynnikiem pierwszym - liczba pierwsza
    # print(predicted_jump)
    if is_prime(predicted_jump) == False:
        return False
    # print(arr[0])
    return arr[0] % predicted_jump == 0


def program():
    n = utils.get_number("Dlugosc tablicy")
    print(is_jump_possible(utils.random_array(n,0,10)))