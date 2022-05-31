import utils
##  Napisaæ program wczytuj¹cy dwie liczby
#naturalne i odpowiadaj¹cy na pytanie czy s¹ one
#zbudowane z takich samych cyfr, np. 123 i 321,
#1255 i 5125, 11000 i 10001.

def get_digits(n):
    digits = [0 for _ in range(utils.get_number_length(n))]
    for i in range(utils.get_number_length(n)):
        digits[i] = n % 10
        n //= 10
    return digits

def digits_compare(dig_a = [],dig_b = []):
    for dig in dig_a:
        if any(d == dig for d in dig_b):
            dig_b.remove(dig)
        else:
            return False
    return True

def contains_the_same_digits(a=0, b=0):
    if utils.get_number_length(a) != utils.get_number_length(b):
        return False
    return digits_compare(get_digits(a), get_digits(b))

def program():
    a = utils.get_number()
    b = utils.get_number()
    print(contains_the_same_digits(a, b))
