import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def contains_valid_digits(n):
    dig_count_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        dig = n%10
        dig_count_arr[dig] += 1
        if dig_count_arr[dig] > 1:
            return False
        n //= 10
    return True

def cut_first_dig(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10

    new_num = 0
    for i in range(len(arr)-2, -1,-1):
        new_num = arr[i] + new_num * 10

    return new_num


def task(number):
    max_prime = 0
    n_copy = number

    while n_copy > 0:
        n_copy_copy = n_copy
        while n_copy_copy > 0:
            if is_prime(n_copy_copy) and contains_valid_digits(n_copy_copy) and max_prime < n_copy_copy:
                max_prime = n_copy_copy
            n_copy_copy //= 10

        n_copy = cut_first_dig(n_copy)

    return max_prime

def program():
    n = int(input("Podaj liczbe"))
    print(task(n))