

def change(n, i):
    if n == 0:
        return [0]
    arr = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    n_arr = []
    while n > 0:
        n_arr.append(arr[n % i])
        n //= i
    return n_arr

def has_any_copy(arr1, arr2):
    for e in arr1:
        for e2 in arr2:
            if e == e2:
                return True

    return False

def task(n, t):
    for i in range(2, 16):
        new_n = change(n, i)
        new_t = change(t, i)
        if has_any_copy(new_n, new_t) == False:
            print(n, "Arr", new_n)
            print(t, "Arr", new_t)
            return i
    return "Brak"




def program():
    n = int(input("Podaj liczbe"))
    t = int(input("Podaj liczbe"))
    print(task(n, t))