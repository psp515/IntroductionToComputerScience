import math
import utils

# Problem 8 Hetmanów (treść oczywista)

# pomysl stowrzenie tablicy 2 wymiarowej i wykreslanie pol ktore nie moga byc uzyte przechodzimy do nastepnego wiersza i to samo
# funkcja wykreslajaca wszystkie pola
# funkcja wstawiajaca w mozliwe pola hetmanów
# 2 - hetman,  1 - pole niemozliwe do uzycia, 0 - puste pole do uzycia

a_count = 0

def task(arr, i=0, pos_count=0, pos=[]):
    global a_count
    if pos_count == 8:
        a_count += 1
        print(pos_count, ".", pos)
        print(utils.display_d_arr(arr))

    for n in range(8):
        if arr[n][i] == False:
            # checkout
            for k in range(8): #wiersz
                arr[n][k] = i

            for k in range(8): # kolumna
                arr[k][i] = i

            z = i-8
            y = n-8
            while True: # skos 1
                if z >= 0 and y >= 0 and y<8 and z < 8:
                    arr[y][z] = i
                if z == 8 or y == 8:
                    break
                z+=1
                y+=1

            z = i - 8
            y = n + 8
            while True: # skos 2
                if z >= 0 and y >= 0 and y<8 and z < 8:
                    arr[y][z] = i
                if z == 8 or y == -1:
                    break
                z+=1
                y-=1

            task(arr, i+1, pos_count+1, pos+[n+1])

            #Clear arr
            for k in range(8): #wiersz
                arr[n][k] = False
            for k in range(8): # kolumna
                arr[k][i] = False

            z = i-8
            y = n-8
            while True: # skos 1
                if z >= 0 and y >= 0 and y<8 and z < 8:
                    arr[y][z] = False
                if z == 8 or y == 8:
                    break
                z+=1
                y+=1

            z = i - 8
            y = n + 8
            while True: # skos 2
                if z >= 0 and y >= 0 and y<8 and z < 8:
                    arr[y][z] = False
                if z == 8 or y == -1:
                    break
                z+=1
                y-=1



    #print("No More:", pos)



def program():
    arr = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
    print(task(arr, 0, 0, []))