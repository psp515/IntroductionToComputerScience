import utils

# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie
# posiada innych czynników niż 2,3,5. Jedynka też jest taką
# liczbą. Napisz program, który wylicza ile takich liczb znajduje
# się w przedziale od 1 do N włącznie.

def count_235_2(max):
    counter = 0
    n_2 = 1
    while n_2 <= max:
        n_3 = n_2
        while n_3 <= max:
            n_5 = n_3
            while n_5 <= max:
                counter += 1
                n_5 *= 5
            n_3 *= 3
        n_2 *= 2
    return counter


def program():
    max = utils.get_number("Podaj max wartość: ")
    #n = count_235(1, max)
    n2 = count_235_2(max)
    print("Liczba 235 liczb w określonym przedziale(1): ", n)
    print("Liczba 235 liczb w określonym przedziale(2): ", n2)