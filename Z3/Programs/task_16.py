import utils

# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych.
# Proszę napisać funkcję zwracającą wartość typu bool
# oznaczającą, czy w tablicy istnieje dokładnie jeden element
# najmniejszy i dokładnie jeden element największy (liczba
# elementów najmniejszych  oznacza liczbę takich elementów o tej samej
# wartości)

def sign(element, e_max, sign):
    return element > e_max if sign == 0 else e_max > element

def find_element(arr, operation):
    max_element = arr[0]
    max_element_counted = 0
    for element in arr:
        if max_element == element:
            max_element_counted += 1
        elif sign(element, max_element, operation) == True:
            max_element = element
            max_element_counted = 1

    return max_element_counted == 1


def task_func(arr=[]):
    #print(arr)
    return find_element(arr, 0) and find_element(arr, 1)

def program():
    n = utils.get_number()
    print(task_func(utils.random_array(n, 0, 10)))