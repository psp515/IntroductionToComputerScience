

#  Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje
#  szachownicę. Proszę napisać funkcję, która sprawdza czy da się umieścić
#  w każdym wierszu jednego króla szachowego tak aby żadne dwa króle nie
#  stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo,
#  suma wartości pól zajmowanych przez wszystkie figury była równa zero.

# arr - tablica
# i-aktualny wiersz
# j- poprzednia wybrana kolumna
# sum - suma pozycji
def task(arr, i=0, j=0, sum=0):
    if i == len(arr):
        return sum == 0 #zwraca sume pol

    for k in range(len(arr)):
        if abs(j-k) > 1 or i == 0: # dodatkowy warunek aby dla kazdej pozycji w pierwszym wierszu sprawdzic kombinacje
            if task(arr, i+1, k, sum+arr[i][j]): # jezeli jakas jest prawda to prawda
                return True

    return False

def program():
    arr = [[1,1,1,1],
           [1,1,-3,1],
           [1,1,1,1],
           [-1,1,-1,-1]]
    print(task(arr))