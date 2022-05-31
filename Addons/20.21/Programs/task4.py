import math


# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N),
# która sprawdza czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy
# z kawałków był liczba pierwszą oraz liczba kawałków też była liczbą pierwszą.
# Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True,
# podział na 23 i 47, natomiast divide(2255)=False.



# czy liczba jest pierwsza
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

# zwraca cyfry liczby
def get_digs(n):
    arr = []
    while n > 0:
        arr.append(n%10)
        n//=10
    return arr[::-1]

# zamien liczbe na bity
def get_bits(n, len):
    bit_arr = [0 for _ in range(len)]
    i=0
    while n>0:
        bit_arr[i] = n % 2
        n //= 2
        i+=1
    return bit_arr

# sprawdza czy kazdy element tablicy jest pierwszy
def are_primes(arr):
    for e in arr:
        if is_prime(e)== False:
            return False
    return True

def divide(n):
    number_len = int(math.log10(n)) # dlugosc liczby - 1
    digs = get_digs(n) # cyfry naszej liczby
    for mask in range(1, 2**number_len): # maska bitowa wybiera miejsce gdzie stoi przerwa np 2|73
        bit_arr = get_bits(mask, number_len)
        num_arr = [] # nowo powstale liczby
        number = 0
        for i in range(len(bit_arr)+1):
            number = number*10 + digs[i] # tworzenie nowej liczby
            print(number)
            if i == len(bit_arr): # jezeli jestes na koncu to dodaj liczbe i wyjdz
                num_arr.append(number)
                break
            if bit_arr[i] == 1: # jezeli przerwa to dodaj do tablicy nowa liczbe i zacznije owrzyc nowa
                num_arr.append(number)
                number = 0

        if is_prime(len(num_arr)) and are_primes(num_arr): # warunki zadania sprawdzane
            return True

    return False


def program():
    #n = int(input("Podaj liczbe:"))
    print(divide(23672))