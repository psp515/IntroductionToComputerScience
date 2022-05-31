import utils

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a*b/nwd(a, b)

def get_nww(n):
    nw = nww(n, n-1)
    for i in range(n-1, 0, -1):
        nw = nww(nw, i)
    return nw

def program():
    print(get_nww(20))