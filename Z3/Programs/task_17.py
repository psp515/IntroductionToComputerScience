import math

import utils
##  Dane s� dwie N-elementowe tablice t1 i t2
#zawieraj�ce liczby naturalne. Z warto�ci w obu
#tablicach mo�emy tworzy� sumy. �Poprawna� suma to
#taka, kt�ra zawiera co najmniej jeden element (z
#tablicy t1 lub t2) o ka�dym indeksie. Na przyk�ad
#dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
#poprawnymi sumami s� na przyk�ad 1+3+2+4, 9+7+4+8,
#1+7+3+8, 1+9+7+2+4+8. Prosz� napisa� funkcje
#generuj�c� i wypisuj�ca wszystkie poprawne sumy,
#kt�re s� liczbami pierwszymi. Do funkcji nale�y
#przekaza� dwie tablice, funkcja powinna zwr�ci�
#liczb� znalezionych i wypisanych sum.

def get_dig(n, arr_Len):
    arr = [0 for _ in range(arr_Len)]
    i = 0
    while n > 0:
        arr[i]= n%3
        n//=3
        i+=1
    return arr

def get_sum(t1,t2,i):
    sum = 0
    arr = get_dig(i,len(t1))
    j = 0
    for e in arr:
        if e == 2:
            sum += t1[j]+t2[j]
        if e == 1:
            sum += t2[j]
        if e == 0:
            sum += t1[j]
        j += 1

    return sum, arr

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

def task_func(t1,t2):
    counter = 0
    for i in range(3**len(t1)):
        sum = get_sum(t1,t2,i)
        if is_prime(sum[0]) == True:
            print(sum[0],"   ",sum[1])
            counter += 1

    return counter

def program():
    print("Count: ",task_func([1,3,2,4],[9,7,4,8]))