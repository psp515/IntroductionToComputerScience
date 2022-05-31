import utils

# Dana jest liczba naturalna o niepowtarzających się cyfrach
# pośród których nie ma zera. Ile różnych liczb podzielnych np.
# przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr
# w tej liczbie. Np. dla 2315 będą to 21, 35, 231, 315

#Podal liczbe: 1234
#Podal dzielnik: 11
#132
#143
#231
#341
#1243
#1342
#2134
#2431
#3124
#3421
#4213
#4312

def get_digits(number): # 1234
    digits = []
    for i in range(utils.get_number_length(number)):
        digits.append(number % 10)
        number = number // 10
    digits.reverse()
    return digits

def has_digts(digits = [], act_sum_digits = []):
    for act_digit in act_sum_digits:
        if any(d == act_digit for d in digits):
            digits.remove(act_digit)
        else:
            return False
    return True

def is_in_order(digits, act_digits):
    i = 0
    counter = 0
    for act_digit in act_digits:
        while i < len(digits):
            if digits[i] == act_digit:
                counter += 1
                break

            i += 1 # 2
        i += 1 # 1

    return counter == len(act_digits)

def get_numbers(n, div):
    sum = div
    digits = get_digits(n)
    i = 0
    while sum <= n:
        if has_digts(digits.copy(), get_digits(sum)) and is_in_order(digits.copy(), get_digits(sum)):
            print(sum)
            i += 1
        sum += div
    return i

def program():
    n = utils.get_number("Podal liczbe: ")
    div = utils.get_number("Podal dzielnik: ")
    number = get_numbers(n, div)
    print("Liczba:",number)
