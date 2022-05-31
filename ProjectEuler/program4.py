import utils

#Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    sum = 0
    copy = n
    while copy > 0:
        digit = copy % 10
        copy //= 10
        sum = sum * 10 + digit
    return sum == n

def is_divisible(n):
    for i in range(100, 1000):
        if n % i == 0 and n/i < 1000:
            print(i)
            return True
    return False

def palindrome():
    for i in range(998001, 0, -1):
        print(i)
        if is_palindrome(i) and is_divisible(i):
            return i
    return 0

def program():
    print(palindrome())