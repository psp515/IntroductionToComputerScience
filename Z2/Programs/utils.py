from math import log10

def get_number_length(n):
    return int(log10(n)) + 1

def get_number(text = "Podaj liczbe: "):
    try:
        return int(input(text))
    except:
        get_number(text)

def get_fibb_by_index(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return get_fibb_by_index(index-1) + get_fibb_by_index(index-2)

def look_in_fib_for_draft(number):
    if number == 0: return True
    end_counter = 0 # upper limit for searching draft
    end_fibo = 0
    while end_fibo < number:
        end_counter += 1
        end_fibo = get_fibb_by_index(end_counter)

        # Below is searching function it searches if draft exist
        searching_fibbo = 0
        searching_counter = 0
        while searching_fibbo < end_fibo:
            searching_fibbo = get_fibb_by_index(searching_counter)
            if end_fibo - searching_fibbo == number:
                return True
            searching_counter += 1
    return False

def is_fibbonacci_number(n):
    if n < 3:
        return True
    a = 3
    b = 2
    while a <= n:
        if a == n:
            return True
        a, b = a+b, a
