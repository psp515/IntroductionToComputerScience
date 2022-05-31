import utils
##  Dana jest N-elementowa tablica t jest
#wype³niona liczbami naturalnymi. Proszê napisaæ
#funkcjê, która zwraca d³ugoœæ najd³u¿szego
#spójnego podci¹gu bêd¹cego palindromem z³o¿onym
#wy³¹cznie z liczb nieparzystych. Do funkcji nale¿y
#przekazaæ tablicê, funkcja powinna zwróciæ d³ugoœæ
#znalezionego podci¹gu lub wartoœæ 0 je¿eli taki
#podci¹g nie istnieje.

def only_odd(n):
    while n > 0:
        dig = n % 10
        if dig % 2 == 0:
            return False
        n//=10

    return True

def rev_number(n):
    rev_number = 0
    while n > 0:
        dig = n % 10
        n//=10
        rev_number = rev_number*10+dig
    return rev_number

def arr_odd(arr=[]):
    for e in arr:
        if only_odd(e) == False:
            return False
    return True

def is_palindrome(arr):
    number = 0
    for e in arr:
        get_len = utils.get_number_length(e)
        number = number*10**get_len + e
    print(number)
    return number == rev_number(number)

def task_func(arr = []):
    max_count = 0
    count = 0
    t_arr = []
    for i in range(len(arr)):
        t_arr += [arr[i]]
        count += 1
        print(count)
        if arr_odd(t_arr) and is_palindrome(t_arr):
            if max_count < count:
                max_count = count
        else:
            copy_count = count
            copy_t_arr = t_arr.copy()
            for j in range(0, i-1):
                copy_t_arr.remove(arr[j])
                copy_count = -1
                if arr_odd(copy_t_arr) and is_palindrome(copy_t_arr):
                    if max_count < copy_count:
                        max_count = copy_count

    return max_count

def program():
    print("Ans", task_func([113, 11, 311, 31]))