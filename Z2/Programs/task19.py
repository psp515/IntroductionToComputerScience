import utils

#Napisać program wczytujący dwie liczby naturalne a,b i
# wypisujący rozwinięcie dziesiętne ułamka a/b w postaci
# ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)

# NOT WORKING

def contains_sequence(arr):
    arr_len =len(arr)
    if arr_len % 2 == 1:
        return False
    arr_len //= 2
    arr_c = arr.copy()
    contains_2 = False
    for k in range(arr_len-1):
        n_l = len(arr_c)
        if n_l%2==1:continue
        n_l//=2
        contains_2 = True
        for i in range(n_l):
            if arr_c[i] != arr_c[i + n_l]:
                contains_2 = False
                break
        if contains_2:
            return arr_c
        arr_c.pop(0)

    return False

def print_decimal_numbers(a, b):
    if a % b == 0:
        print(a/b)
        return
    print(a//b, end=".")
    a = a % b
    arr = []
    while True:
        a *= 10
        arr.append(a//b)
        a = a % b
        if len(arr)>=2:
            ans = contains_sequence(arr)
            if ans != False:
                arr = ans
                break
    print("(",end="")
    for i in range(int(len(arr)/2)):
        print(arr[i], end="")

    print(")", end="")

def program():
    a = utils.get_number("Podaj a: ")
    b = utils.get_number("Podaj b: ")
    print_decimal_numbers(a, b)