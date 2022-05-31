import math
import utils

# Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę
# składni- ków. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.

def task(number, removator = 1, sum = ""):
    if number <= 0:
        print(sum[0:-1])
        return
    if number-removator>=0:
        task(number, removator+1, sum+str(removator+1)+"+")
        task(number - removator, removator, sum+str(removator)+"+")

        if len(sum)>1:
            task(number - removator, removator + 1, sum + str(removator+1) + "+")


def program():
    n = utils.get_number()
    task(n, 1, "")