import math

def is_multi(element=""):
    for i in range(1, int((len(element)-1)/2)):
        if len(element) % i == 0:
            arr = [element[n:n+i] for n in range(0, len(element), i)]
            is_mul = True
            for i in range(1,len(arr)):
                if arr[1] != arr[i]:
                    is_mul = False
                    break
            if is_mul == True:
                return True
    return False

def multi2(T=[]):
    max_len = 0
    for e in T:
        e_len = len(e)
        if is_multi(e):
            if max_len < e_len:
                max_len = e_len

    return max_len

def program():
    print(multi2(["ABCABC","AAAAAAAAAAAAA","ABAABA","DABDABDAB"]))