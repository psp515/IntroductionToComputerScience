import utils
import math

#Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą
# liczbę jedynek, np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1]
# T2[N2][N2], gdzie N2<N1. Proszę napisać funkcję, która sprawdza czy istnieje
# takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
# elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2.
# Obie oryginalne tablice powinny pozostać nie zmieniane.

# fukcja sumuje zapis binarny + suma jedynek w zapisie binarnym
def count_ones(n):
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    return count

# fukcja porównuje 2 liczby na podstawie liczby 1 w zapisie binarnym
def same_one_count(n,m):
    return count_ones(n) == count_ones(m)

def task(arr1, arr2):
    val = math.ceil(2*len(arr2)*0.33) # minimalna liczba elementow ktore musimy miec aby moc zwrocic True
    max_skip = len(arr1) - len(arr2) # o ile mozemy przesowac miejsza tablice
    for i in range(max_skip+1):
        for j in range(max_skip+1):
            count = 0 # liczba zgodnych pozycji
            for k in range(len(arr2)):
                for m in range(len(arr2)):
                    if same_one_count(arr2[k][m], arr1[k+i][m+j]):
                        count += 1
                    if count >= val:
                        return True

    return False

def program():

    arr1 = [[5,5,5],
            [5,5,5],
            [2,2,3]]

    arr2 = [[0,0],
            [2,2]]
    print(task(arr1, arr2))