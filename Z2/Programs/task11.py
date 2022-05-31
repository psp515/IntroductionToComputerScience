import utils

# Napisz program wczytujący liczbę naturalną z klawiatury i
# odpowiadający na pytanie, czy jej cyfry stanowią ciąg rosnący.

def is_increasing(n):
    if utils.get_number_length(n) > 9 or n <= 0:
        return False

    prev_r = 10
    while n > 0:
        r = n % 10
        n = n // 10
        if r > prev_r:
            return False
        prev_r = r

    return True



def program():
    n = utils.get_number()
    print(is_increasing(n))