import utils
import math

# Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą
# tablicę kolejnymi liczbami naturalnymi po spirali.



def task(d_arr, n):
    steps = ((1, 0), (0, 1), (-1, 0), (0, -1))
    x, y = 0, 0
    num = 1
    line_len = n-1
    while line_len > 0:
        for step in steps:
            xp, yp = step
            for i in range(line_len):
                d_arr[y][x] = num
                x, y = x + xp, y + yp
                num += 1
        line_len -= 2
        x, y = x + 1, y + 1

    if n % 2 == 1:
        d_arr[int((n-1)/2)][int((n-1)/2)] = n*n

    return d_arr

def program():
    n = utils.get_number()
    utils.display_d_arr(task(utils.create_d_arr(n), n))