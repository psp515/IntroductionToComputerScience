import utils


# Find the sum of all the multiples of 3 or 5 below 1000.

def sum(n):
    sum_3 = (3 + int(n/3)*3) * int(n/3) * 0.5
    sum_5 = (5 + int(n/5)*5) * int(n/5) * 0.5
    sum_15 = (15 + int(n/15)*15) * int(n/15) * 0.5
    print(sum)
    return int(sum_3 + sum_5 - sum_15)

def program():
    n = utils.get_number()
    print(sum(n))
