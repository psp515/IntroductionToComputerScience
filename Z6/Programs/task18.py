import math
import utils

#W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną.
# Na ruchy królanałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól
# jeżeli ostatnia cyfra liczby napolu na którym stoi jest mniejsza od pierwszej cyfry liczby pola
# docelowego, oraz w drodze do obranego celu(np. narożnika) król nie może wykonać ruchu,
# który powoduje oddalenie go od celu. Dana jest globalna tablicaT[8][8] wypełniona liczbami
# naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne w=0 i k=0.
# Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k
# do prawego dolnegonarożnika.

# podaje ostania cyfre liczby
def get_first_dig(n):
    first_dig = 0
    while n > 0:
        first_dig = n % 10
        n //= 10
    return first_dig

# sprawdza czy ostatnia cyfra liczby 1 jest mniejsza od pierwszej cyfry liczby 2
def dig_compare(num1, num2):
    last_dig = num1 % 10
    first_dig = get_first_dig(num2)
    return last_dig < first_dig

# sprawdza i podaje mozliwe ruchy
def moves(arr, w, k):
    possibilities = [(0, 1), (1, 1), (1, 0)] # niby 8 pol ale jezeli zawsze ma sie zblizac do celu to tylko 3 opcje
    for e in possibilities:
        n_w, n_k = w + e[0], k + e[1]
        if n_w >= 0 and n_w < 8 and n_k >= 0 and n_k < 8:
            if dig_compare(arr[w][k], arr[n_w][n_k]):
                continue
            else:
                possibilities.remove(e)
    return possibilities

def task(arr, w, k):
    if w == 7 and k == 7: # jezeli jestes w rogu to sie udalo
        return True

    if w < 0 or w >= 8 or k < 0 or k >= 8: # jezeli wyszedles poza tablice to false
        return False

    is_succ = False
    for e in moves(arr, w, k): # sprawdz co sie dzieje dla innych ruchow
        is_succ = task(arr, w + e[0], k + e[1]) # sprawdzanie drogi
        if is_succ:
            break

    return is_succ


def program():
    arr = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 3, 3, 3, 3],
           [0, 0, 0, 0, 3, 3, 3, 3],
           [0, 0, 0, 0, 3, 3, 3, 3],
           [0, 0, 0, 0, 3, 3, 3, 3]]

    print(task(arr, 5, 5))