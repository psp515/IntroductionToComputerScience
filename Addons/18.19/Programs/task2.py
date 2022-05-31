

def task(arr=[]):
    max_len = 0
    count = 1
    sum = arr[0]
    index_sum = 0
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            sum += arr[i]
            index_sum += i
            count += 1
            if index_sum == sum and max_len < count:
                max_len = count
        else:
            for j in range(i):
                sum -= arr[j]
                index_sum -= j
                count -= 1
                if index_sum == sum and max_len < count:
                    max_len = count
            sum = arr[i]
            index_sum = i
            count = 1

    return max_len


def program():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(task(arr))