import utils

# Napisać funkcję, która dla N-elementowej tablicy t wypełnionej
# liczbami naturalnym wyznacza długość najdłuższego, spójnego
# podciągu geometrycznego


# zakladam ze w ciagu nie trafi sie zero
def longest_geometric_draft(arr = []):
    print(arr)
    counter = 2
    max_counted = 0
    q = arr[1] / arr[0]
    for i in range(2, len(arr)):
        if arr[i] / arr[i-1] == q:
            counter += 1
        else:
            counter = 2
            q = arr[i] / arr[i-1]

        max_counted = (counter if counter > max_counted else max_counted)

    return max_counted

def program():
    n = utils.get_number("Arr length: ")
    print(longest_geometric_draft(utils.random_array(n, 0, 10)))
    #[1, 1, 2, 4, 8, 5, 6, 7, 1, 1, 1, 1, 1]))