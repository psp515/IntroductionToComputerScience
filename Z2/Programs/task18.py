import utils






def printing():
    a_a, a_p = 1, 0
    b = 2
    while True:
        n = utils.get_number("Podaj nastepna liczbe an: ")
        if n != a_a:
            break
        print(b)
        temp = a_a
        a_a = a_a - b * a_p
        a_p = temp
        b = b + 2 * temp


def program():
    printing()