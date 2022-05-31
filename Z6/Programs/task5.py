import math
import utils

#Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
#na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
#każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
#110100 nie jest możliwe.

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
def get_bits(len, n):
    arr = [0 for _ in range(len-1)]
    i = 0
    while n > 0:
        arr[i] = n % 2
        n//=2
        i += 1
    return arr
# przerwa pomiedzy bitami to max 30
def validate_bits(bit_arr):
    counter = 1
    for e in bit_arr:
        if counter > 30:
            return False
        if e == 1:
            counter = 0
        counter += 1
    return True
def are_primes(nums):
    for e in nums:
        if is_prime(e)==False:
            return False
    return True

def get_nums(arr, bit_arr):
    bit_str = "" + str(arr[0])
    for i in range(len(bit_arr)):
        if bit_arr[i] == 1:
            bit_str += "|"
        bit_str += str(arr[i+1])

    str_arr = bit_str.split("|")
    int_arr = []
    for i in str_arr:
        int_arr.append(int(i,2))
    return int_arr


# arr -tablica
# arr_len - dlugosc tablicy
# mask -> miejsce przerwy w ciagu bitowym np dla 111 i makski 1 to 1|11 => 1|3
def task(arr, arr_len, mask=1):
    if mask == 2**(arr_len-1):
        return False

    bit_arr = get_bits(arr_len, mask)
    if validate_bits(bit_arr) == True:
        nums = get_nums(arr, bit_arr)
        if are_primes(nums):
            return True
    return task(arr, arr_len, mask+1)

def program():
    #print(get_nums([1, 1, 1, 0, 1, 1],[0,0,0,0,1]))
    arr = [1, 1, 1, 0, 1, 1]
    print(task(arr, len(arr), 1))