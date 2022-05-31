import utils

# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający
# na pytanie, czy jej cyfry stanowią ciąg rosnący.

def has_digit_equal_to_length(n):
    length = utils.get_number_length(n)
    while n > 0:
        if n % 10 == length:
            return True
        n = n // 10
    return False

def program():
    n = utils.get_number()
    print(has_digit_equal_to_length(n))
