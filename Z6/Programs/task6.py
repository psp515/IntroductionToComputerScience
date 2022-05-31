import math
import utils

#Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
#liczebności) podzbiór elementów tablicy, dla którego suma elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę,
# funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.


# arr - tablica
# arr_len - dlugosc tablicy
# mask maska bitowa

# sprawdza czy sumy sie zgadzaja jezli tak zwraca krotke(liczba 1, suma)
def sum_check(arr, n):
    i = 0
    sum = 0
    index_sum = 0
    one_count = 0
    while n > 0:
        if n % 2 == 1:
            sum += arr[i]
            index_sum += i
            one_count += 1
        n //= 2
        i += 1
    return (one_count, sum) if sum == index_sum else (-1, -1)

# arr - tablca
# arr_Len - dlugosc tablicy
# mask - maska bitwa odpowiada zakombinacje liczb z tablicy
# ans_arr - tablica poprwanych odpowiedzi
def task(arr, arr_len, mask=1, ans_arr = (-1,-1)):
    if mask == 2**arr_len:
        if len(ans_arr) == 0:
            return -1
        return ans_arr[1]
    sum_val = sum_check(arr, mask)
    if sum_val[0] != -1:
        if ans_arr[0] >= sum_val[0] or ans_arr[0] == -1:
            if sum_val[1] > ans_arr[1] or ans_arr == -1:
                ans_arr = sum_val

    return task(arr, arr_len, mask + 1, ans_arr)

def program():
    arr = [0, 1, 2, 3,]
    print(task(arr, len(arr), 1))