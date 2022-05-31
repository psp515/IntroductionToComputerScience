


def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i

    print(fact)

    while fact % 10 == 0:
        fact //= 10

    return fact % 10

def program():
    n = int(input("Podaj liczbe"))
    print(factorial(n))