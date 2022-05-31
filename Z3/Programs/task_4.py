import utils
##  Napisaæ program obliczaj¹cy i wypisuj¹cy sta³¹
#e z rozwiniêcia w szereg e = 1/0! + 1/1! + 1/2! +
#1/3! + ... z dok³adnoœci¹ N cyfr dziesiêtnych (N
#jest rzêdu 1000).

def calc_level(factorial, tab):
    a, b = 1, factorial
    for i in range(1, len(tab)):
        try:
            a *= 10
            tab[i] += a // b
            a %= b
            if a == 0:
                break
        except IndexError:
            print(i)
            exit()


def aproximate_e(n, prec=1000):
    if n > 1000:
        n = 1000
    additional_multiplayer = 1
    digits = [1] + [0] * int(n * additional_multiplayer + 10)
    n += 1

    factorial = 1
    for i in range(1, prec):
        factorial *= i
        calc_level(factorial, digits)

    # print(digits)
    for i in range(-1, -len(digits), -1):
        digits[i - 1] += digits[i] // 10
        digits[i] %= 10

    return digits[:n]

# wersja 2


def aproximate_e2(n):
    s = [0 for _ in range(n+1)]
    w = [0 for _ in range(n+1)]
    w[0] = 1
    s[0] = 1

    i = 1
    while max(w)>0:
        p = 0
        for j in range(n,-1,-1):
            tmp = s[j] + w[j] + p
            p //= 10
            s[j] = tmp % 10
        i += 1
        r = 0
        for j in range(n+1):
            r *= 10 + w[j]
            w[j] = r//i
            r %= i

    return s


def program():
    n = utils.get_number("dokladnosc: ")
    print(aproximate_e2(n))