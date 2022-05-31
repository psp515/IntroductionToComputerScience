import utils
##  Napisa? funkcj?, kt?ra dla N-elementowej
#tablicy t wype?nionej liczbami naturalnym wyzna-
#cza d?ugo?? najd?u?szego, sp?jnego podci?gu
#arytmetycznego.

def longest_draft(arr = []):
    print(arr)
    counter = 2
    max_counted = 1
    r = arr[1] - arr[0]
    for i in range(2, len(arr)):
        n_r = arr[i] - arr[i-1]
        if n_r == r:
            counter += 1
        else:
            counter = 2
            r = n_r
        max_counted = (counter if counter > max_counted else max_counted)

    return max_counted

def program():
    n = utils.get_number("Arr length: ")
    print(longest_draft(utils.random_array(n, 0, 20)))