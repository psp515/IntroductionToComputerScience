import math
import utils

# Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k
# jestczynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację
# czy jestmożliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę
# wykonanychskoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.


# zwraca liste mozliwych skoków (liczb pierwszych z rozkladu)
def get_jumps(n):
    n_copy = n
    jump_arr = []
    i = 2
    while n > 1:
        if n % i == 0 and i != n_copy:
            jump_arr.append(i)
        while n % i == 0 and n != 0:
            n //= i
        i += 1

    return jump_arr

# arr - tablica
# arr_Len - dlugosc tablicy
# i - aktualna pozycja w liscie
# counter - liczy skoki

def task(arr, arr_len, i=0, counter=0):
    if i >= arr_len: # jezleli i >= arr_len to nie ma roziwazania
        return -1
    if i == arr_len - 2: # jezeli jestem na pozycji n-1 to zwracam skoki
        return counter

    for e in get_jumps(arr[i]): # dla kazdego skoku sprawdz czy moze dojsc do pozycji n-1
        count = task(arr, arr_len, i + e, counter + 1)
        if count != -1:
            return count # zwroc liczbe skoków

    return -1

def program():
    arr = [4,3,4,5,5,6]
    print(task(arr, len(arr), 0, 0))