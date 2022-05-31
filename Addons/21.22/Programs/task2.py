

def get_4_dig(e):
    arr = [0,0,0,0] # ma 0,1,2,3
    while e > 0:
        dig = e % 4
        e//=4
        arr[dig] += 1
    return arr

def get_10_dig(n):
    arr = [0,0,0,0,0,0,0,0,0,0]
    while n > 0:
        arr[n%10]+=1
        n//=10
    return arr

def is_ok(e):
    num_4 = get_4_dig(e)
    num_10 = get_10_dig(e)

    for i in range(10):
        if i < 4:
            if num_4[i] > 0 and num_10[i] > 0:
                continue
            elif num_10[i] == 0 and num_4[i] == 0:
                continue
            else:
                return False
        else:
            if num_10[i] > 0:
                return False

    return True


def task(arr=[]):
    max_count = 0
    count = 0
    for e in arr:
        if is_ok(e):
            count += 1

        if max_count < count:
            max_count = count

    return count

def program():
    print(task([1,2,3,0,4,5]))