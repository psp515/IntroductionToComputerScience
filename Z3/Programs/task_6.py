import random

import utils
##  Napisa� program wype�niaj�cy N-elementow�
#tablic� t liczbami naturalnymi 1-1000 i spraw-
#dzaj�cy czy ka�dy element tablicy zawiera co
#najmniej jedn� cyfr� nieparzyst�.

def has_valid_digit(element = 0):
    while element > 0:
        if element % 2 == 1: # sprawdzam ostatni element
            return True
        element //= 10
    return False

def validate_array(arr = []):
    for el in arr:
        if has_valid_digit(el) == False:
            return False
    return True

def program():
    n = utils.get_number()
    validate_array([random.randint(0, 1000) for _ in range(n)])