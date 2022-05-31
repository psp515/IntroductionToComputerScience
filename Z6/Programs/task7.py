import math
import utils

# Dany jest zestaw odważników T[N].
# Napisać funkcję, która sprawdza czy jest możliwe odwa- żenie określonej masy.
# Odważniki można umieszczać tylko na jednej szalce.

def task(arr, ws, wa = 0, i = 0):
    if wa == ws:
        return True
    if wa > ws or len(arr)==i:
        return False

    return task(arr, ws, wa+arr[i], i+1) or task(arr, ws, wa, i+1)

def program():
    n = utils.get_number()
    print("Ans:", task([1,2,3,5,10], n))