import utils

# Napisz program wczytujący liczbę naturalną z klawiatury i
# odpowiadający na pytanie, czy liczba ta jest wielokrotnością
# dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

def f(n):
    return n * n + n + 1

def is_in_draft(n):
    act_n = 1
    i = 1
    while act_n <= n:
        if act_n == n:
            return True
        i += 1
        act_n = f(i)
    return False

def program():
    n = utils.get_number("Podal liczbe: ")
    print(is_in_draft(n))