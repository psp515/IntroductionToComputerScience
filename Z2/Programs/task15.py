import utils

# Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
# liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3 .

def print_narcistics(number_of_digits):
    max_number = 10**number_of_digits
    number = int(max_number/10)
    while number < max_number:
        digits = list(map(int, str(number)))
        suma = 0
        for digit in digits:
            suma += digit**number_of_digits
            if suma > number:
                break
        if suma == number:
            print(number)
        number += 1

def program():
    n = utils.get_number("Podaj ilość cyfr: ")
    print_narcistics(n)