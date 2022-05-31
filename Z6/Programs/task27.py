import math
import utils

#Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste
# ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów.
# Proszęnapisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć
# 13 nienachodzących na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.

def calc_field(x1,x2,y1,y2):
    return (y2-y1) * (x2-x1)

def is_ok(sq, arr):


def task(arr, i=0, squares=[], f_sum=0):
    if len(squares) == 13:
        return f_sum == 2012
    if i == len(arr) or len(squares)>=13:
        return False

    if is_ok(arr[i],squares):
        return task(arr,i+1,squares, f_sum) or \
               task(arr,i+1,squares+[arr[i]],f_sum+calc_field(arr[i][0],arr[i][1],arr[i][2],arr[i][3]))

    return  task(arr,i+1,squares,f_sum)


    pass


def program():
    n = utils.get_number()
    print(task())