from operator import itemgetter
import math
from datetime import datetime


def zadania_z_lekcji():
    # pierwsze okolo 16 bit wzor shaunonna
    """
    KOdy Huffmana
    A - 0
    B - 10
    C - 110
    D - 1110
    E - 11110
    itd
    """
    # uleszenie algorytmu z zadania 3 to jest NWD kolo zadania 12
    # rozklad na czynniki pierwsze nw co dodac ale jest inny niz na wykladzie

def rozklad_na_czynniki_pierwsze(number):
    i = 2
    while number > 1 and i <= math.sqrt(number):
        while number % i == 0:
            print(i)
            number //= i
        i += 1

    if number > 1:
        print(number)
def last_z_lekcji(number):
    # nie wiem tego lipa
    # podzial na 3 kiedy liczba jest podzilena przez 2 i nie podzielna przez 2 oraz pierwiastkowalna
    pier = math.sqrt(number)
    if number % pier == 0:
        while number > 0:
            print(pier)
    elif number % 2 == 0:
        for i in range(0,10):
            pass

    else:
        pass

def get_fibonnacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n==2:
        return 1
    return get_fibonnacci(n-1) + get_fibonnacci(n-2)
def zadanie_1():
    a = 0
    i = 0
    while True:
        a = get_fibonnacci(i)
        if a > 1000000:
            return
        i += 1
        print(i,". ",a)

def year_fibbo(n, place_1, place_2):
    if n == 0:
        return 0
    if n == 1:
        return place_1
    if n == 2:
        return place_2
    return year_fibbo(n-1, place_1, place_2) + year_fibbo(n-2, place_1, place_2)
def has_fake_fibbo_a_number(number, place_1, place_2):
    i = 0
    while True:
        a = year_fibbo(i, place_1, place_2)
        if a == number:
            return True, place_1, place_2

        if a > number:
            return False, 0, 0

        i += 1
    return False, 0, 0
def zadanie_2():
    data = []
    i = 2
    while i < 80:
        j = i
        while j < 80:
            has_number = has_fake_fibbo_a_number(2021, j, i)
            if has_number[0]:
                data.append([has_number[1] + has_number[2], has_number[1], has_number[2]])

            j += 1
        i += 1

    data = sorted(data, key=itemgetter(0))
    print(data)
    print(data[0])


def look_in_fib_for_draft(number):
    if number == 0: return True
    end_counter = 0 # upper limit for searching draft
    end_fibo = 0
    while end_fibo < number:
        end_counter += 1
        end_fibo = get_fibonnacci(end_counter)

        # Below is searching function it searches if draft exist
        searching_fibbo = 0
        searching_counter = 0
        while searching_fibbo < end_fibo:
            searching_fibbo = get_fibonnacci(searching_counter)
            if end_fibo - searching_fibbo == number:
                return True
            searching_counter += 1
    return False


    return False
def zadanie_3():
    number = int(input("Podaj liczbe:"))
    has_draft = look_in_fib_for_draft(number)
    print(has_draft)

def zadanie_4():
    number = int(input("Podaj n:"))
    counter = 0
    sum = 1
    while sum != number:
        counter += 1
        sum += counter * 2 - 1

    print(counter)

def zadanie_5():
    number = int(input("Podaj n:"))
    copy = number
    for i in range(10):
        copy = (copy + number/copy)/2
    print(copy)

def function(x):
    return x**x
# a - przedzial dol
# b - predzial gora
def f_bisection(min, max, e, number):
    while max - min > e:
        mid = (max+min)/2
        if f(mid) > number:
            max = mid
        else:
            min = mid
    return mid


def zadanie_6():
    print(f_bisection(100,100, 0.01))


def zadanie_7():
    number = int(input("Podaj liczbe:"))
    a = 0
    b = 1
    counter = 0
    while a*b<number:
        if a*b == number:
            print("Iloczyn 2 wyrazów", a, "i", b)
            return
        counter += 1
        c = a + b
        a = b
        b = c
    print("Nie ma")

def is_prime(number):
    if number <=1:
        return  False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True
def zadanie_8():
    number = int(input("Podaj liczbe: "))
    is_prime_number = is_prime(number)
    print(is_prime_number)

def print_divisors(number):
    for i in range(1, number//2+1):
        if number% i ==0:
            print("Divisor:",i)
    print("Divisor:", number)
def alternatywa(number):
    i = 1
    while i*i<=n:
        if n & i == 0:
            print(i)
            print(n/i)
        i+=1
    if i*i == n:
        print(i)

def zadanie_9():
    number = int(input("Podaj liczbe:"))
    print_divisors(number)

def get_divisors_sum(number):
    sum = 0
    for i in range(1,number//2+1):
        if number % i == 0:
            sum+=i
    return sum
def is_ideal_number(number):
    return number == get_divisors_sum(number)
def print_ideals_to_mln():
    for i in range(1000000):
        if is_ideal_number(i):
            print(i)
def zadanie_10():
    print_ideals_to_mln()

def print_friends_numbers():
    number1 = 1
    while number1 < 1000000:
        number2 = get_divisors_sum(number1)
        number_2_divisors_sum = get_divisors_sum(number2)
        if number_2_divisors_sum == number1 and number1 != number2:
            print("Friend numbers:", number1, number2)
            if number2 > number1:
                number1 = number2 + 1
                continue
        number1 += 1
def zadanie_11():
    print_friends_numbers()

# Tutaj rozwiazne zadanie o algorytmie euklidesa z lekcji !
def NWD(number1,number2):
    # zapamietaj
    print(number1, number2)
    while number2:
        number1, number2 = number2, number1 % number2
        print(number1, number2)
    return number1
def NWD3(number1, number2, number3):
    first_nwd = NWD(number1, number2)
    second_nwd = NWD(first_nwd, number3)
    return first_nwd if first_nwd == second_nwd else -1
def zadanie_12():
    number_1 = int(input("Podaj liczbe:"))
    number_2 = int(input("Podaj liczbe:"))
    number_3 = int(input("Podaj liczbe:"))
    print(NWD3(number_1, number_2, number_3))

def NWW1(number1, number2):
    increasing_number = number1
    while True:
        if increasing_number % number2 == 0:
            return increasing_number
        increasing_number += number1
def NWW2(number1, number2):
    return int(number1 * number2 / NWD(number1, number2))
def zadanie_13():
    number1 = int(input("Podaj liczbe: "))
    number2 = int(input("Podaj liczbe: "))
    nww1 = NWW1(number1, number2)
    nww2 = NWW2(number1, number2)
    print("NWW:", nww1)
    print("NWW:", nww2)

def sqrt_draft(draft_lenght):
    result = math.sqrt(0.5)
    last_element = result
    for i in range(draft_lenght):
        last_element = math.sqrt(0.5 + 0.5 * last_element)
        result *= last_element

    return result
def pi_calculator():
    return 2 / sqrt_draft(19)
def zadanie_15():
    print(pi_calculator())

def maclaurin(n):
    cos = 1
    counter = 1
    factorial = 2
    sign = -1
    for i in range(200):
        counter*= n * n
        cos += sign* counter/factorial
        factorial = factorial * (i + 2) * (i + 3)
        sign *= -1
    return cos

def zadanie_14():
    # szereg maclaurinna
    n = int(input("Number: "))
    print(maclaurin(n))


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1

def get_daft_lenght_to_1(n):
    counter = 0
    a = n
    while a != 1:
        a = collatz(a)
        counter += 1
    return counter

def zadanie_16():
    i = 2
    krotka = (0,0)
    while i < 10000:
        counter = get_daft_lenght_to_1(i)
        if krotka[0] < counter:
            krotka = (counter, i)
        i += 1

    print("Liczba: ", krotka[1], "|  Liczba iteracji:", krotka[0])


def print_border():
    for i in range(40):
        a = get_fibonnacci(i)
        b = get_fibonnacci(i+1)
        print(float(a/b))
def zadanie_17():
    print_border()


# troche nie dziala ale do znalezienia na necie
def wzor_newtona(liczba, stopien_pierwiastka):
    copy = liczba
    for i in range(200):
        copy = ((stopien_pierwiastka-1) * copy + liczba/(copy**(stopien_pierwiastka-1)))/3
    return copy
def sqrt3(number):
    copy = number
    for i in range(100):
        copy = (2 * copy + number / (copy * copy)) / 3
    return copy
def zadanie_18():
    number = int(input("Podaj n:"))
    print(sqrt3(number))


def silnia(number):
    if number == 0:
        return 1
    return number * silnia(number-1)
def get_e():
    e = 1
    for i in range(1, 123):
        e += 1/silnia(i)
    return e
def zadanie_19():
    e = get_e()
    print(e)

def calc_a(a, b):
    return math.sqrt(a * b)

def calc_b(a, b):
    return (a + b) / 2

def avgAG(a,b):
    e = 0.01
    while abs(a - b) > e:
        a_copy = a
        a = calc_a(a,b)
        b = calc_b(a_copy,b)
    return (a + b) / 2

def zadanie_20():
    a = int(input("Podaj liczbe poczatkowa ciagu a:"))
    b = int(input("Podaj liczbe poczatkowa ciagu b:"))
    print(avgAG(a, b))


# Cwiczenia 1: Proste programy z petlami
if __name__ == '__main__':
    print("start")
    #zadanie_1()
    #zadanie_2()
    #zadanie_3()
    #zadanie_4()
    #zadanie_5()
    #zadanie_6()
    #zadanie_7()
    #zadanie_8()
    #zadanie_9()
    #zadanie_10()
    #zadanie_11()
    #zadanie_12()
    #zadanie_13()
    #zadanie_18()
    #zadanie_19()
    #zadanie_15()
    #zadanie_3()
    #zadanie_14()
    #zadanie_16()
    #zadanie_17()
    zadanie_20()
    print("stop")