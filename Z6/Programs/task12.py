import math
import utils

# Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.

def task(arr, n, s_multi, m = 0, act_multi = 1, i = 0, act_arr=[], global_arr=[]):
    if m == n and s_multi == act_multi:
        global_arr += [act_arr]
        return
    if i == len(arr):
        return
    task(arr, n, s_multi, m+1, act_multi*arr[i], i+1, act_arr+[arr[i]])
    task(arr, n, s_multi, m, act_multi, i+1, act_arr)
    return global_arr

def program():
    n = utils.get_number()
    print(task([1,2,3,4,5,6,4,12], 2, 12, 0, 1, 0))