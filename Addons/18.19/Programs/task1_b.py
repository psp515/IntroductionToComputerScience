


def is_fib_sum(n):
    counter = 0
    a, b = 1, 1
    sum = 0
    while sum < n:
        sum += a
        a, b = a+b, a
        if sum == n:
            return True
        c, d = 1, 1
        sum_2 = 0
        while sum-sum_2 > 0:
            sum_2 += c
            c, d = c + d, c
            if sum-sum_2 == n:
                return True

    return False


def get_n_fib(n):
    a, b = 0, 1
    sum = 0
    for i in range(n):
        sum += a
        a, b = b, a+b

    return sum


def task(n):
    while True:
        n += 1
        if is_fib_sum(n) == True:
            return n


def program():
    n = int(input())
    print(task(n))