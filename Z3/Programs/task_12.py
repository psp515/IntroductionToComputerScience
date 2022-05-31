import utils
##  Prosz? napisa? program, kt?ry wype?nia
#N-elementow? tablic? t pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a nast?pnie
#wyznacza i wypisuje r?nic? pomi?dzy d?ugo?ci?
#najd?u?szego znajduj?cego si? w niej ci?gu
#arytmetycznego o dodatniej r?nicy, a d?ugo?ci?
#najd?u?szego ci?gu arytme- tycznego o ujemnej
#r?nicy, przy za?o?eniu, ?e kolejnymi wyrazami
#ci?gu s? elementy tablicy o kolejnych indeksach.

def longest_decreasing(arr = []):
    counter = 2
    max_counted = 0
    r = arr[1] - arr[0]
    for i in range(2, len(arr)):
        n_r = arr[i] - arr[i - 1]
        if n_r < 0:
            if n_r == r:
               counter += 1
               max_counted = (counter if counter > max_counted else max_counted)
            else:
               counter = 2
            r = n_r
    return max_counted

def longest_increasing(arr = []):
    counter = 2
    max_counted = 0
    r = arr[1] - arr[0]
    for i in range(2, len(arr)):
        n_r = arr[i] - arr[i - 1]
        if n_r > 0:
            if n_r == r:
                counter += 1
                max_counted = (counter if counter > max_counted else max_counted)
            else:
                counter = 2
            r = n_r

    return max_counted

def get_ans(arr = []):
    print(arr)
    return abs(longest_decreasing(arr) - longest_increasing(arr))

def program():
    n = utils.get_number("Arr len")
    print(get_ans([1,2,3,4,5,4,3,2,1,0]))#utils.random_array(n, 1, 99)))