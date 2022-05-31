import utils

# Pewnych liczb nie można przedstawić jako sumy elementów spójnych
# fragmentów ciągu Fibo- nacciego, np. 9,14,15,17,22.
# Proszę napisać program, który wczytuje liczbę naturalną n,
# wylicza i wypisuje następną taką liczbę większą od n. Można
# założyć, że 0 < n < 1000.

def number_not_in_draft(n):
    i = n + 1
    while True:
        if utils.look_in_fib_for_draft(i):
            i += 1
        else:
            return i

def program():
    n = utils.get_number("Podal liczbę: ")
    if n >= 1000:
        n = 999
    print(number_not_in_draft(n))
