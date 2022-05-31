import utils
import math

# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję
# która zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających
# go elementów jest największa.

# Funkcja generuje i zwraca mozliwe pola do zsumowania
def generate_moves(i,j, max_len):
    arr = [(0,1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,-1),(-1,0)]
    rarr = []
    for e in arr:
        a,b = i+e[0],j+e[1]
        if a>0 and b > 0 and b < max_len and a < max_len:
            rarr.append((a,b))
    return rarr

# suma pól
def sum_arr(arr, positions):
    sum = 0
    for e in positions:
        sum += arr[e[0]][e[1]]
    return sum

def task(arr):
    max_sum = 0
    row = 0
    col = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            positions = generate_moves(i, j, len(arr))
            ssum = sum_arr(arr, positions)
            if ssum > max_sum:
                row = i
                col = j
                max_sum = ssum

    return row, col

def program():
    ans = task([[0,1,2],[0,1,0],[0,1,2]])
    print(ans)