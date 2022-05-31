import math
import utils

# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

def task(arr, ws, wa = 0, i = 0):
    if wa == ws:
        return True
    if wa > ws or len(arr) == i:
        return False

    return task(arr, ws, wa+arr[i], i+1) or task(arr, ws, wa, i+1) or task(arr, ws+arr[i], wa, i+1)

def program():
    n = utils.get_number()
    print("Ans:", task([1,2,3,10], n))