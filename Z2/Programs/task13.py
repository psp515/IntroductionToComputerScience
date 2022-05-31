import utils

# Napisz program wczytujący liczbę naturalną z klawiatury i
# odpowiadający na pytanie, czy liczba zakończona jest
# unikalną cyfrą.

def is_last_digit_unical(n):
    if n < 0:
        return False
    last_digit = n % 10
    n = n // 10
    while n > 0:
        if n % 10 == last_digit:
            return False
        n = n // 10
    return True

def program():
    n = utils.get_number()
    print(is_last_digit_unical(n))