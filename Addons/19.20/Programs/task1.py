import math


def sum_arr(arr=[]):
    sum = 0
    for e in arr: sum+=e
    return sum

def get_num_multi(num):
    arr = [0 for _ in range(int(math.sqrt(num))+1)]
    for i in range(2, int(math.sqrt(num))+1):
        while num % i == 0:
            num //= i
            arr[i] += 1
    return arr


def is_sum_valid(sum):
    arr = get_num_multi(sum)
    sum = sum_arr(arr)
    return any(sum == e for e in arr)


def get_avalible_parts(arr,sum_arr):
    avalible = []
    for i in range(arr):
        sum_copy = sum_arr
        j = 0
        n_sum = 0
        while j<i:
            sum_copy -= arr[j]
            n_sum += arr[j]
            if is_sum_valid(sum_copy) and is_sum_valid(n_sum):
                avalible.append(i-j)
            j += 1
    return avalible

def task(t1 = [],t2 = []):
    if len(t1)+len(t2) < 24:
        return False

    sum_t1 = sum_arr(t1)
    avalible_t1 = get_avalible_parts(t1, sum_t1)

    sum_t2 = sum_arr(t2)
    avalible_t2 = get_avalible_parts(t2, sum_t2)

    for e in avalible_t1:
        for e2 in avalible_t2:
            if e + e2 == 24:
                return True

    return False



def program():
    print(task([],[]))