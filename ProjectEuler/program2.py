import utils

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def sum_even_fib_num(n):
    a = 0
    b = 1
    sum = 0
    while b < n:
        sum += b if b % 2 == 0 else 0
        a, b = b, a + b

    return sum

def program():
    n = utils.get_number()
    print(sum_even_fib_num(n))