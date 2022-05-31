import utils
##  Napisa? funkcj?, kt?ra dla N-elementowej
#tablicy t wype?nionej liczbami naturalnym wyznacza
#d?ugo?? najd?u?szego, sp?jnego podci?gu rosn?cego.



def longest_draft(arr = [], arr_len= 0):
    counter = 1
    max_counted = 1
    print(arr)
    for i in range(1, arr_len):
        max_counted = counter if counter > max_counted else max_counted
        counter = (counter + 1 if arr[i-1] < arr[i] else 1)

    return max_counted

def program():
    n = utils.get_number("Arr length: ")
    print(longest_draft(utils.random_array(n, 0, 10), n))