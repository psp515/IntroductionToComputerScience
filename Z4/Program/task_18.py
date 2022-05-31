import utils
import math

#Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję,
# która wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie.
# Maksymalna długość podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T,
# funkcja powinna zwrócić sumę maksymalnego podciągu.



def task(arr, n):
    sum_max = 0
    count_max = 0
    for i in range(len(arr)):
        sum = 0
        count = 0
        for j in range(len(arr)):
            sum += arr[i][j]
            count += 1
            if sum_max < sum:
                sum_max = sum
                count_max = count
            c_copy = count
            s_copy = sum
            s_index = k - count
            for k in range(count):
                s_copy -= arr[s_index+k]
                c_copy -= 1
                if sum_max < s_copy:
                    sum_max = s_copy
                    count_max = c_copy

    #to samo zrobic dla kolumn kwestia zamiany i oraz j miejsami

    return count_max

def program():
    n = utils.get_number()
    print(task([], n))