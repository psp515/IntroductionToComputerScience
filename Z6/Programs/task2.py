import math
import utils

# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby.
# Na przykład waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1.
# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać
# funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory
# o równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja
# powinna zwrócić wartość typu Bool.

def get_primes_count(number=0):
    primes_count = 0
    i = 2
    while number > 1:
        if number % i == 0:
            primes_count += 1
        while number % i == 0:
            number //= i
        i+=1
    return primes_count

# arr - tablica
# i - indekser
# w1 - suma wagi 1
# w2 - suma wagi 2
# w3 - suma wagi 3

def task(arr, i=0, w1=0, w2=0, w3=0):
    if i == len(arr):
        return w1 == w2 and w1 == w3
    return task(arr, i+1, w1+get_primes_count(arr[i]), w2, w3) or \
           task(arr, i+1, w1, w2+get_primes_count(arr[i]), w3) or \
           task(arr, i+1, w1, w2, w3+get_primes_count(arr[i]))

def program():
    #print(get_primes_count(4))
    print(task([6, 6, 2, 3]))