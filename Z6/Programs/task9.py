import math
import utils

# Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.


def task(arr, ws, wa=0, i=0, used=["|"]): # zakladam ze na prawej szalce kłade odwaznik do zmierzenia
    if wa == ws:
        return True, used

    if wa > ws or len(arr) == i:
        return False

    return task(arr, ws, wa+arr[i], i+1, [arr[i]]+used) or task(arr, ws, wa, i+1, used) or task(arr, ws+arr[i], wa, i+1, used+[arr[i]])

def program():
    n = utils.get_number()
    print("Ans:", task([1, 2, 3, 10], n, 0, 0, ["|"]))