import utils

# What is the 10 001st prime number?

def return_nth_prime(n):
    i = 2
    counter = 0
    biggest_prime = 2
    while counter < n:
        if utils.is_prime(i):
            counter += 1
            biggest_prime = i
        i += 1
    return biggest_prime

def program():
    print(return_nth_prime(10001))