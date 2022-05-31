import utils

# Napisz program wczytujący liczbę naturalną z klawiatury i
# odpowiadający na pytanie, czy liczba ta jest wielokrotnością dowolnego
# wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
# jest równy 2.

def f(index):
    if index == 1:
        return 2
    return 3 * f(index-1) + 1

def is_in_draft(n):
    if n < 7:
        return False
    i = 1
    test = f(i)
    while test <= n:
        if n % test == 0:
            return True
        i += 1
        test = f(i)

    return False


def program():
    n = utils.get_number("Podal liczbę: ")
    print(is_in_draft(n))