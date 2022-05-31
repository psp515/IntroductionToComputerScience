

# Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać
# funkcję, która sprawdza czy z tablicy można usunąć jeden wiersz i dwie kolumny,
# tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym posiadał
# nieparzystą liczbę jedynek.

def print_d_arr(arr):
    for e in arr:
        print(e)

# oblicz liczbe jedynek w zapisie binarnym
def calculate_bin_sum(n):
    sum = 0
    while n > 0:
        sum+=n%2
        n //= 2
    return sum

# przelicz tablice zamieniajca liczbe na liczbe 1 w zapisie bin
def calculate_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = calculate_bin_sum(arr[i][j])

    return arr

def task(arr):
    bin_sum_arr = calculate_arr(arr)
    print_d_arr(bin_sum_arr)

    for deleted_col in range(len(arr)): # wybierz kolumne do usuniecia
        for deleted_row in range(len(arr)): # wybierz wiersz do usuniecia
            for deleted_row2 in range(deleted_row+1,len(arr)): # wybierz  2 wiersz do usuniecia ale tylko wiekszy od poprzedniego
                is_suc = True
                for i in range(len(arr)):
                    for j in range(len(arr)): # iterujemy po tablicy i sprawdzamy
                        if j != deleted_col: # czy nie nalezy do wykreslonej kolumny
                            if i != deleted_row2 and i != deleted_row: # czy nie nalezy do usunietych wierszy
                                if arr[i][j] % 2 == 0: # sprawdzam warunki zadania
                                    is_suc = False
                                    break
                if is_suc == True:
                    return True

    return False


def program():
    arr = [[3,2,3],[3,2,3],[3,2,3]]
    arr1 = [[1, 2, 3], [3, 2, 3], [1, 2, 3]]
    arr2 = [[3, 2, 3], [3, 2, 3], [1, 2, 3]]
    print(task(arr))
    print(task(arr1))
    print(task(arr2))


